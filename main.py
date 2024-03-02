from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from utils import flights
from schemas import flights as flight_schemas
from typing import Optional

app = FastAPI()

#Add clients
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/show_flights", status_code=200)
def show_flights() -> list[flight_schemas.FlightDetail]:
    return flights.get_flights()

@app.get("/show_fastest_route", status_code=200)
def show_fastest_route() -> flight_schemas.FastFlightDetailedList:
    return flights.get_fastest_flight_route()

@app.get("/sort_flights_by_price", status_code=200)
def sort_flights_by_price(sorting_asc: bool, limit: Optional[int] = None) -> list[flight_schemas.FlightDetail]:
    return flights.get_sorted_flights_by_price(sorting_asc, limit)

@app.get("/show_flights_by_company", status_code=200)
def show_flights_by_company(company_id: str) -> list[flight_schemas.FlightDetail]:
    return flights.get_flights_by_company(company_id)

# Error handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = []
    for error in exc.errors():
        error_message = error["msg"]
        error_messages.append(f"{error_message}")
    return JSONResponse(status_code=400, content={"detail": error_messages})
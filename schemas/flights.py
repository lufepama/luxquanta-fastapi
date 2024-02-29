from pydantic import BaseModel, constr

class FlightDetail(BaseModel):
    id: constr(max_length=105) | None = None
    legs: list
    pricing_options: list
    deeplink: constr(max_length=450) | None = None


class FastFlightDetail(BaseModel):
    flight_id: constr(max_length=100) | None = None
    flight_deeplink: constr(max_length=450) | None = None
    trip: dict

class FastFlightDetailedList(BaseModel):
    min_duration: int | None = None
    data: list[FastFlightDetail]
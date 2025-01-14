import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestFlights:
    @pytest.fixture
    def api_client(self):
        return TestClient(app)
    
    def test_show_flights(self, api_client):
        expected_response = [
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                {
                    "id": "13870-2208011240--32222-0-12712-2208011455",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 495,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T12:40:00",
                    "arrival": "2022-08-01T14:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011240-2208011455--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "durationInMinutes": 495,
                        "flightNumber": "6251",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208152100--32222-0-13870-2208161020",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T21:00:00",
                    "arrival": "2022-08-16T10:20:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208152100-2208161020--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "durationInMinutes": 440,
                        "flightNumber": "6252",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1559.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                {
                    "id": "13870-2208011240--32222-0-12712-2208011455",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 495,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T12:40:00",
                    "arrival": "2022-08-01T14:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011240-2208011455--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "durationInMinutes": 495,
                        "flightNumber": "6251",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151700--32222-0-13870-2208160625",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 445,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T17:00:00",
                    "arrival": "2022-08-16T06:25:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151700-2208160625--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "durationInMinutes": 445,
                        "flightNumber": "6250",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1604.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                {
                    "id": "13870-2208011620--32317-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32317,
                        "name": "Finnair"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32317",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "5655",
                        "marketingCarrier": {
                        "id": -32317,
                        "name": "Finnair",
                        "alternate_di": "AY",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151700--32222-0-13870-2208160625",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 445,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T17:00:00",
                    "arrival": "2022-08-16T06:25:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151700-2208160625--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "durationInMinutes": 445,
                        "flightNumber": "6250",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "finn",
                        "name": "Finnair",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.3,
                        "feedback_count": 1304,
                        "rating_breakdown": {
                        "reliable_prices": 2.761956,
                        "clear_extra_fees": 3.917272,
                        "customer_service": 4.863896,
                        "ease_of_booking": 4.352984,
                        "other": 2.284648
                        }
                    }
                    ],
                    "price": {
                    "amount": 1617.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CAELIGHT01&carriers=-32317%2C-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1617.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                {
                    "id": "13870-2208011620--32222-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "6253",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208152100--32222-0-13870-2208161020",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T21:00:00",
                    "arrival": "2022-08-16T10:20:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208152100-2208161020--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "durationInMinutes": 440,
                        "flightNumber": "6252",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1559.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                {
                    "id": "13870-2208011620--32222-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "6253",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151850--32317-0-13870-2208160810",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T18:50:00",
                    "arrival": "2022-08-16T08:10:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32317,
                        "name": "Finnair"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151850-2208160810--32317",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "durationInMinutes": 440,
                        "flightNumber": "4008",
                        "marketingCarrier": {
                        "id": -32317,
                        "name": "Finnair",
                        "alternate_di": "AY",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32573,
                        "name": "American Airlines",
                        "alternate_di": "AA",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "finn",
                        "name": "Finnair",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.3,
                        "feedback_count": 1304,
                        "rating_breakdown": {
                        "reliable_prices": 2.761956,
                        "clear_extra_fees": 3.917272,
                        "customer_service": 4.863896,
                        "ease_of_booking": 4.352984,
                        "other": 2.284648
                        }
                    }
                    ],
                    "price": {
                    "amount": 1532.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                {
                    "id": "13870-2208011240--32222-0-12712-2208011455",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 495,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T12:40:00",
                    "arrival": "2022-08-01T14:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011240-2208011455--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "durationInMinutes": 495,
                        "flightNumber": "6251",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151850--32317-0-13870-2208160810",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T18:50:00",
                    "arrival": "2022-08-16T08:10:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32317,
                        "name": "Finnair"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151850-2208160810--32317",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "durationInMinutes": 440,
                        "flightNumber": "4008",
                        "marketingCarrier": {
                        "id": -32317,
                        "name": "Finnair",
                        "alternate_di": "AY",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32573,
                        "name": "American Airlines",
                        "alternate_di": "AA",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "finn",
                        "name": "Finnair",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.3,
                        "feedback_count": 1304,
                        "rating_breakdown": {
                        "reliable_prices": 2.761956,
                        "clear_extra_fees": 3.917272,
                        "customer_service": 4.863896,
                        "ease_of_booking": 4.352984,
                        "other": 2.284648
                        }
                    }
                    ],
                    "price": {
                    "amount": 1532.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                {
                    "id": "13870-2208011620--32317-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32317,
                        "name": "Finnair"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32317",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "5655",
                        "marketingCarrier": {
                        "id": -32317,
                        "name": "Finnair",
                        "alternate_di": "AY",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151850--32317-0-13870-2208160810",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T18:50:00",
                    "arrival": "2022-08-16T08:10:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32317,
                        "name": "Finnair"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151850-2208160810--32317",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "durationInMinutes": 440,
                        "flightNumber": "4008",
                        "marketingCarrier": {
                        "id": -32317,
                        "name": "Finnair",
                        "alternate_di": "AY",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32573,
                        "name": "American Airlines",
                        "alternate_di": "AA",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "finn",
                        "name": "Finnair",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.3,
                        "feedback_count": 1304,
                        "rating_breakdown": {
                        "reliable_prices": 2.761956,
                        "clear_extra_fees": 3.917272,
                        "customer_service": 4.863896,
                        "ease_of_booking": 4.352984,
                        "other": 2.284648
                        }
                    }
                    ],
                    "price": {
                    "amount": 1519.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1519.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                {
                    "id": "13870-2208011620--32222-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "6253",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151850--32222-0-13870-2208160810",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T18:50:00",
                    "arrival": "2022-08-16T08:10:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151850-2208160810--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "durationInMinutes": 440,
                        "flightNumber": "4000",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32573,
                        "name": "American Airlines",
                        "alternate_di": "AA",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1529.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                {
                    "id": "13870-2208011240--32222-0-12712-2208011455",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 495,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T12:40:00",
                    "arrival": "2022-08-01T14:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011240-2208011455--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "durationInMinutes": 495,
                        "flightNumber": "6251",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151850--32222-0-13870-2208160810",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 440,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T18:50:00",
                    "arrival": "2022-08-16T08:10:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151850-2208160810--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "durationInMinutes": 440,
                        "flightNumber": "4000",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32573,
                        "name": "American Airlines",
                        "alternate_di": "AA",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1529.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                {
                    "id": "13870-2208011620--32222-0-12712-2208011855",
                    "origin": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "destination": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "durationInMinutes": 515,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-01T16:20:00",
                    "arrival": "2022-08-01T18:55:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "13870-12712-2208011620-2208011855--32222",
                        "origin": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "durationInMinutes": 515,
                        "flightNumber": "6253",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                },
                {
                    "id": "12712-2208151700--32222-0-13870-2208160625",
                    "origin": {
                    "id": 12712,
                    "name": "New York John F. Kennedy",
                    "displayCode": "JFK"
                    },
                    "destination": {
                    "id": 13870,
                    "name": "Madrid",
                    "displayCode": "MAD"
                    },
                    "durationInMinutes": 445,
                    "stopCount": 0,
                    "isSmallestStops": True,
                    "departure": "2022-08-15T17:00:00",
                    "arrival": "2022-08-16T06:25:00",
                    "timeDeltaInDays": 0,
                    "carriers": {
                    "marketing": [
                        {
                        "id": -32222,
                        "name": "Iberia"
                        }
                    ],
                    "operationType": "fully_operated"
                    },
                    "segments": [
                    {
                        "id": "12712-13870-2208151700-2208160625--32222",
                        "origin": {
                        "flightPlaceId": "JFK",
                        "parent": {
                            "flightPlaceId": "NYC",
                            "name": "New York",
                            "type": "City"
                        },
                        "name": "New York John F. Kennedy",
                        "type": "Airport"
                        },
                        "destination": {
                        "flightPlaceId": "MAD",
                        "parent": {
                            "flightPlaceId": "MAD",
                            "name": "Madrid",
                            "type": "City"
                        },
                        "name": "Madrid",
                        "type": "Airport"
                        },
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "durationInMinutes": 445,
                        "flightNumber": "6250",
                        "marketingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        },
                        "operatingCarrier": {
                        "id": -32222,
                        "name": "Iberia",
                        "alternate_di": "IB",
                        "allianceId": -32000
                        }
                    }
                    ]
                }
                ],
                "pricing_options": [
                {
                    "agents": [
                    {
                        "id": "iber",
                        "name": "Iberia",
                        "is_carrier": True,
                        "update_status": "current",
                        "optimised_for_mobile": True,
                        "live_update_allowed": True,
                        "rating_status": "available",
                        "rating": 3.32,
                        "feedback_count": 899,
                        "rating_breakdown": {
                        "reliable_prices": 2.330344,
                        "clear_extra_fees": 4.6778,
                        "customer_service": 5,
                        "ease_of_booking": 3.7112,
                        "other": 2.575832
                        }
                    }
                    ],
                    "price": {
                    "amount": 1604.31,
                    "update_status": "current",
                    "last_updated": "2022-07-08T16:26:00",
                    "quote_age": 169
                    },
                    "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            }
            ]

        response = api_client.get("/show_flights")

        assert response.status_code == 200
        assert response.json() == expected_response
    
    def test_show_fastest_route(self, api_client):
        expected_response = {
            "min_duration": 440,
            "data": [
                {
                    "flight_id": "13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                },
                {
                    "flight_id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810",
                    "flight_deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1",
                    "trip": {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                }
            ]
        }
        
        response = api_client.get("/show_fastest_route")
        assert response.status_code == 200
        assert response.json() == expected_response
    
    def test_sort_flights_by_price_ascending(self, api_client):
        expected_response = [
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1519.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1519.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1529.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1529.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1559.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1559.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1604.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1604.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1617.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CAELIGHT01&carriers=-32317%2C-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1617.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            }
        ]
        
        response = api_client.get("/sort_flights_by_price?sorting_asc=true")

        assert response.status_code == 200
        assert response.json() == expected_response
    
    def test_sort_flights_by_price_ascending_limit(self, api_client):
        limit = 3
        response = api_client.get(f"/sort_flights_by_price?sorting_asc=true&limit={limit}")
        assert response.status_code == 200
        assert len(response.json()) == limit


    def test_sort_flights_by_price_descending(self, api_client):
        expected_response = [
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1617.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CAELIGHT01&carriers=-32317%2C-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1617.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1604.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1604.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1604.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1559.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208152100--32222-0-13870-2208161020",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T21:00:00",
                        "arrival": "2022-08-16T10:20:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208152100-2208161020--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T21:00:00",
                                "arrival": "2022-08-16T10:20:00",
                                "durationInMinutes": 440,
                                "flightNumber": "6252",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1559.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C6252%7C12712%7C2022-08-15T21%3A00%7C13870%7C2022-08-16T10%3A20%7C440%7CNHX4C7B4%7CN%7CESAJNB&carriers=-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1559.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208152100--32222-0-13870-2208161020?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1529.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32222-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4000",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "iber",
                                "name": "Iberia",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.32,
                                "feedback_count": 899,
                                "rating_breakdown": {
                                    "reliable_prices": 2.330344,
                                    "clear_extra_fees": 4.6778,
                                    "customer_service": 5,
                                    "ease_of_booking": 3.7112,
                                    "other": 2.575832
                                }
                            }
                        ],
                        "price": {
                            "amount": 1529.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/iber/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CESAJNB%2Cflight%7C-32222%7C4000%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CESAJNB&carriers=-32222&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=false&ticket_price=1529.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32222-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1519.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1519.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            }
        ]
        
        response = api_client.get("/sort_flights_by_price?sorting_asc=false")
        
        assert response.status_code == 200
        assert response.json() == expected_response

    def test_sort_flights_by_price_descending_limit(self, api_client):
        limit = 3
        response = api_client.get(f"/sort_flights_by_price?sorting_asc=false&limit={limit}")
        assert response.status_code == 200
        assert len(response.json()) == limit

    def test_get_flights_by_company(self, api_client):
        expected_response = [
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151700--32222-0-13870-2208160625",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 445,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T17:00:00",
                        "arrival": "2022-08-16T06:25:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151700-2208160625--32222",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T17:00:00",
                                "arrival": "2022-08-16T06:25:00",
                                "durationInMinutes": 445,
                                "flightNumber": "6250",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1617.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32222%7C6250%7C12712%7C2022-08-15T17%3A00%7C13870%7C2022-08-16T06%3A25%7C445%7CSHX4C7B4%7CS%7CAELIGHT01&carriers=-32317%2C-32222&operators=-32222%2C-32222&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1617.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151700--32222-0-13870-2208160625?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32222-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "6253",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6253%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32222-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011240--32222-0-12712-2208011455",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 495,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T12:40:00",
                        "arrival": "2022-08-01T14:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32222,
                                    "name": "Iberia"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011240-2208011455--32222",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T12:40:00",
                                "arrival": "2022-08-01T14:55:00",
                                "durationInMinutes": 495,
                                "flightNumber": "6251",
                                "marketingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1532.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32222%7C6251%7C13870%7C2022-08-01T12%3A40%7C12712%7C2022-08-01T14%3A55%7C495%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32222%2C-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1532.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011240--32222-0-12712-2208011455|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            },
            {
                "id": "13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810",
                "legs": [
                    {
                        "id": "13870-2208011620--32317-0-12712-2208011855",
                        "origin": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "destination": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "durationInMinutes": 515,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-01T16:20:00",
                        "arrival": "2022-08-01T18:55:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "13870-12712-2208011620-2208011855--32317",
                                "origin": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-01T16:20:00",
                                "arrival": "2022-08-01T18:55:00",
                                "durationInMinutes": 515,
                                "flightNumber": "5655",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32222,
                                    "name": "Iberia",
                                    "alternate_di": "IB",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    },
                    {
                        "id": "12712-2208151850--32317-0-13870-2208160810",
                        "origin": {
                            "id": 12712,
                            "name": "New York John F. Kennedy",
                            "displayCode": "JFK"
                        },
                        "destination": {
                            "id": 13870,
                            "name": "Madrid",
                            "displayCode": "MAD"
                        },
                        "durationInMinutes": 440,
                        "stopCount": 0,
                        "isSmallestStops": True,
                        "departure": "2022-08-15T18:50:00",
                        "arrival": "2022-08-16T08:10:00",
                        "timeDeltaInDays": 0,
                        "carriers": {
                            "marketing": [
                                {
                                    "id": -32317,
                                    "name": "Finnair"
                                }
                            ],
                            "operationType": "fully_operated"
                        },
                        "segments": [
                            {
                                "id": "12712-13870-2208151850-2208160810--32317",
                                "origin": {
                                    "flightPlaceId": "JFK",
                                    "parent": {
                                        "flightPlaceId": "NYC",
                                        "name": "New York",
                                        "type": "City"
                                    },
                                    "name": "New York John F. Kennedy",
                                    "type": "Airport"
                                },
                                "destination": {
                                    "flightPlaceId": "MAD",
                                    "parent": {
                                        "flightPlaceId": "MAD",
                                        "name": "Madrid",
                                        "type": "City"
                                    },
                                    "name": "Madrid",
                                    "type": "Airport"
                                },
                                "departure": "2022-08-15T18:50:00",
                                "arrival": "2022-08-16T08:10:00",
                                "durationInMinutes": 440,
                                "flightNumber": "4008",
                                "marketingCarrier": {
                                    "id": -32317,
                                    "name": "Finnair",
                                    "alternate_di": "AY",
                                    "allianceId": -32000
                                },
                                "operatingCarrier": {
                                    "id": -32573,
                                    "name": "American Airlines",
                                    "alternate_di": "AA",
                                    "allianceId": -32000
                                }
                            }
                        ]
                    }
                ],
                "pricing_options": [
                    {
                        "agents": [
                            {
                                "id": "finn",
                                "name": "Finnair",
                                "is_carrier": True,
                                "update_status": "current",
                                "optimised_for_mobile": True,
                                "live_update_allowed": True,
                                "rating_status": "available",
                                "rating": 3.3,
                                "feedback_count": 1304,
                                "rating_breakdown": {
                                    "reliable_prices": 2.761956,
                                    "clear_extra_fees": 3.917272,
                                    "customer_service": 4.863896,
                                    "ease_of_booking": 4.352984,
                                    "other": 2.284648
                                }
                            }
                        ],
                        "price": {
                            "amount": 1519.31,
                            "update_status": "current",
                            "last_updated": "2022-07-08T16:26:00",
                            "quote_age": 169
                        },
                        "url": "https://www.skyscanner.net/transport_deeplink/4.0/UK/en-GB/EUR/finn/2/13870.12712.2022-08-01,12712.13870.2022-08-15/air/airli/flights?itinerary=flight%7C-32317%7C5655%7C13870%7C2022-08-01T16%3A20%7C12712%7C2022-08-01T18%3A55%7C515%7CBHX0C0B4%7CB%7CAELIGHT01%2Cflight%7C-32317%7C4008%7C12712%7C2022-08-15T18%3A50%7C13870%7C2022-08-16T08%3A10%7C440%7CQHX4C7B4%7CQ%7CAELIGHT01&carriers=-32317&operators=-32222%2C-32573&passengers=1&channel=website&cabin_class=economy&facilitated=true&ticket_price=1519.31&is_npt=false&is_multipart=false&client_id=skyscanner_website&q_sources=JACQUARD&commercial_filters=false&q_datetime_utc=2022-07-08T16%3A26%3A00&pqid=false"
                    }
                ],
                "deeplink": "https://www.skyscanner.net/transport/flights/mad/jfk/220801/220815/config/13870-2208011620--32317-0-12712-2208011855|12712-2208151850--32317-0-13870-2208160810?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&originentityid=27544850&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            }
        ]

        response = api_client.get("/show_flights_by_company?company_id=finn")
        
        assert response.status_code == 200
        assert response.json() == expected_response

    def test_sort_flights_by_price_failed(self, api_client):
        response = api_client.get("/sort_flights_by_price?sorting_asc=not_boolean_value")
        assert response.status_code == 400
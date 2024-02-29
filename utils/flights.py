import json


data_flights = [
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

def get_flights():
  return data_flights

def get_fastest_flight_route():
    fastest_flights, min_duration = [], float('inf')

    for flight in data_flights:
        for leg in flight['legs']:
            if leg['durationInMinutes'] < min_duration:
                min_duration = leg['durationInMinutes']
                fastest_flights = [_adapt_flight_trip_data(flight['id'], flight['deeplink'], leg)]
            elif leg['durationInMinutes'] == min_duration:
                fastest_flights.append(_adapt_flight_trip_data(flight['id'], flight['deeplink'], leg))
    return {
       "min_duration": min_duration,
       "data": fastest_flights
    }

def get_sorted_flights_by_price(is_descending: bool):
  return sorted(data_flights, key=lambda flight: flight['pricing_options'][0]['price']['amount'], reverse=not is_descending)

def get_flights_by_company(company_id: str):
  return list(filter(lambda flight: flight['pricing_options'][0]['agents'][0]['id'] == company_id, data_flights))

def _adapt_flight_trip_data(flight_id, flight_deeplink, flight_leg):
  return {
    "flight_id": flight_id,
    "flight_deeplink": flight_deeplink,
    "trip": flight_leg
  }

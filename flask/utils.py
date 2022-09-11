def search_flight(id, flights):
    return [flight for flight in flights if flight["flight_id"] == id]
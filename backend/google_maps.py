import os, requests
KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_route_waypoints(src, dest):
    r = requests.get("https://maps.googleapis.com/maps/api/directions/json",
        params={"origin":src,"destination":dest,"key":KEY})
    return [(st['end_location']['lat'],st['end_location']['lng'])
            for st in r.json()['routes'][0]['legs'][0]['steps']]

def get_stations_on_route(src, dest):
    pts = get_route_waypoints(src, dest)
    seen = {}
    for lat,lng in pts:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params={
            "location":f"{lat},{lng}", "radius":5000,
            "type":"charging_station", "key":KEY
        }).json()
        for p in r["results"]:
            seen[p["place_id"]] = {
                "name": p["name"],
                "place_id": p["place_id"],
                "location": p["geometry"]["location"],
                "price": 12,
                "wait_time": "low",
                "distance": None
            }
    return list(seen.values())

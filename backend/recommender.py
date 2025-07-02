from google_maps import get_stations_on_route
from availability import get_slot_status
from db import prefs_collection

def recommend(user_email, battery, src, dest):
    prefs = prefs_collection.find_one({"email":user_email}) or {}
    stations = get_stations_on_route(src,dest)
    best = sorted(stations, key=lambda s:
        ((battery/100)*prefs.get("vehicle_range",300) >= s["distance"])*10 +
        (s["price"] <= prefs.get("price_threshold",15))*3 +
        (s["wait_time"]=="low")*5, reverse=True)[0]
    best["availability"] = get_slot_status(best["place_id"])
    return best

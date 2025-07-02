import random
def get_slot_status(place_id):
    n = random.randint(0,5)
    return {"free":n, "occupied":5-n, "status": "🟢" if n>3 else "🟡" if n>0 else "🔴"}

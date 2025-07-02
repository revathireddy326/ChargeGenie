from fastapi import FastAPI, Depends
from auth import router as auth_router, get_current_user
from recommender import recommend
from gpt_explainer import explain
from models import Preferences
from db import prefs_collection

app = FastAPI()
app.include_router(auth_router, prefix="/auth")

@app.post("/user/preferences")
def save_prefs(prefs: Preferences, user=Depends(get_current_user)):
    prefs_collection.update_one(
        {"email": user},
        {"$set": prefs.dict()},
        upsert=True
    )
    return {"msg": "Preferences saved successfully."}

@app.get("/recommendation")
def get_recommend(
    battery: int,
    src: str,
    dest: str,
    email=Depends(get_current_user)
):
    station = recommend(email, battery, src, dest)
    explanation = explain(email, station, battery, dest)
    return {"station": station, "explanation": explanation}

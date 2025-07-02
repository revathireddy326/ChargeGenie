from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import UserRegister, UserLogin
from db import users_collection
from passlib.context import CryptContext
import jwt, os

# Initialize router
router = APIRouter(tags=["auth"])

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# HTTP bearer token security
security = HTTPBearer()

# ------------------ 🔐 AUTH ROUTES ------------------

@router.post("/register")
def register(u: UserRegister):
    if users_collection.find_one({"email": u.email}):
        raise HTTPException(status_code=400, detail="User already exists.")
    hashed = pwd_context.hash(u.password)
    user_data = u.dict()
    user_data["password"] = hashed
    users_collection.insert_one(user_data)
    return {"msg": "Registered successfully."}

@router.post("/login")
def login(u: UserLogin):
    user = users_collection.find_one({"email": u.email})
    if not user or not pwd_context.verify(u.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token = jwt.encode({"email": u.email}, os.getenv("JWT_SECRET"), algorithm="HS256")
    return {"access_token": token}


# ------------------ ✅ TOKEN VALIDATION DEPENDENCY ------------------

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        return payload["email"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token.")

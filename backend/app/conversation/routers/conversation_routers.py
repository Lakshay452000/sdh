from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)
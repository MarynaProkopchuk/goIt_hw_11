from fastapi import APIRouter, HTTPException, Depends, status, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db


router = APIRouter(prefix="/contacts", tags=["contacts"])

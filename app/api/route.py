from app.core.fs_router import FSRoute
from fastapi import APIRouter

def get_router():
   return APIRouter(route_class=FSRoute)




from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class RequestUpdate(BaseModel):
    new_string: str

@router.get("/get_map")
def get_game_map():
    file = open("game_map.txt","r")
    string = file.read()
    return {"status": string}

@router.patch("/update_map")
def update_game_map(body: RequestUpdate):
    file = open("game_map.txt","w")
    file.write(body.new_string)
    return {"status": body.new_string}


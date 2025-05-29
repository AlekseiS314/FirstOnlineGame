from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class RequestUpdate(BaseModel):
    new_string: str

@router.get("/get_map")
def get_map():
    file = open("game_map.txt","r")
    string = file.read()
    return {"status": string}

@router.patch("/update_map")
def update_map(body: RequestUpdate):
    file = open("game_map.txt","w")
    file.write(body.new_string)
    return {"status": body.new_string}

@router.post("/set_name/{name}")
def set_name(name : str):
    file = open("Name_players.txt","a")
    file.write("\n"+name)
    return {"status": "\n"+name}
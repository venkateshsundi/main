from fastapi import APIRouter
from models.todos import Todo
from config.database import collections_name
from schemas.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get('/')
async def get_todos():
    todos = list_serial(collections_name.find())
    return todos


@router.post("/")
async def postTODO(todo: Todo):
    collections_name.insert_one(dict(todo))

from fastapi import APIRouter
from database.classroomservice import *

class_router = APIRouter(prefix='/classroom', tags=['Classroom API'])


@class_router.post('/create_class')
async def create_class(name: str, description: str):
    result = create_classrooom_db(name=name, descr=description)
    return {'status': 1, 'result': result}


@class_router.get('/get_class')
async def get_class(cid: int):
    result = get_all_or_exact_class(cid=cid)
    return {'status': 1, 'message': result}


@class_router.put('/update_class')
async def update_class(cid: int, name: str, description: str):
    result = update_class_db(cid=cid, name=name, descr=description)
    return {'status': 1, 'message': result}


@class_router.delete('/delete_class')
async def delete_class(cid: int):
    result = delete_class_db(cid=cid)
    return {'status': 1, 'message':result}
from fastapi import APIRouter
from database.hwservice import *


hw_router = APIRouter(prefix='/homework', tags=['Homework API'])


@hw_router.post('/create_homework')
async def create_homework_api(name: str, description: str, group_id: int, uid: int, points: int):
    result = create_hw_db(name=name, descr=description, group_id=group_id, uid=uid, points=points)
    return {'status': 1, 'message': result}

@hw_router.get('/get_homework')
async def get_hw(hid: int):
    result = get_all_or_exact_hw_db(hwid=hid)
    return {'status': 1, 'message': result}

@hw_router.delete('/delete_homework')
async def delete_hw(hid: int):
    result = delete_hw_db(hwid=hid)
    return {'status': 1, 'message': result}

@hw_router.put('/update_homework')
async def update_hw(hid: int, change_info: str, new_info: str):
    result = update_homewrok(hid=hid, change_info=change_info, new_info=new_info)
    return {'status': 1, 'message': result}

@hw_router.post('/create_upload_homework')
async def create_upload_hw(text: str, uid: int, hid: int, points: int):
    result = create_upload_hw_db(text=text, uid=uid, hid=hid, points=points)
    return {'status': 1, 'message': result}

@hw_router.get('/get_exact_task')
async def get_exact_task(hid: int):
    result = get_exact_task_db(hid=hid)
    return {'status': 1, 'message': result}

@hw_router.delete('/delete_task')
async def delete_task(hid: int):
    result = delete_task_db(hid=hid)
    return {'status': 1, 'message': result}

@hw_router.put('/update_task')
async def update_task(hid: int, change_info: str, new_info: str):
    result = update_hw_task_db(hid=hid, change_info=change_info, new_info=new_info)
    return {'status': 1, 'message': result}
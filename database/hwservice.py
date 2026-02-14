from database import get_db
from database.models import HomeWork, HomeWorkUpload


"""
HomeWork
1. Добавление дз
2. Получение всех дз и определенного
3. Удаление дз
4. Изменение
HomeWorkUpload
1. Добавление задания
2. Изменение
3. Получение определенног
4. Удаление
"""


def create_hw_db(name, descr, group_id, uid, points):
    db = next(get_db())
    new_hw = HomeWork(name=name, descr=descr, group_id=group_id, uid=uid, points=points)
    db.add(new_hw)
    db.commit()
    return True


def get_all_or_exact_hw_db(hwid):
    db = next(get_db())
    if hwid:
        exact_hw = db.query(HomeWork).filter_by(id=hwid).first()
        if exact_hw:
            return exact_hw
        return False
    all_hw = db.query(HomeWork).all()
    return all_hw


def delete_hw_db(hwid):
    db = next(get_db())
    delete_hw = db.query(HomeWork).filter_by(id=hwid).first()
    if delete_hw:
        db.delete(delete_hw)
        return True
    return False



def update_homewrok(hid, change_info, new_info):
    db = next(get_db())
    exact_hw = db.query(HomeWork).filter_by(id=hid).first()
    if exact_hw:
        if change_info == 'name':
            exact_hw.name = new_info
        elif change_info == 'description':
            exact_hw.description = new_info
        elif change_info == 'points':
            change_info.points = new_info
        db.commit()
        return True
    return False

            
            
def create_upload_hw_db(text, uid, hid, points):
    db = next(get_db())
    new_task = HomeWorkUpload(text=text, uid=uid, hw_id=hid, points=points)
    db.add(new_task)
    db.commit()
    return True


def get_exact_task(hid):
    db = next(get_db())
    exact_task = db.query(HomeWorkUpload).filter_by(hw_id=hid).first()
    if exact_task:
        return exact_task
    return False


def delete_task_db(hid):
    db = next(get_db())
    exact_task = db.query(HomeWorkUpload).filter_by(hw_id=hid).first()
    if exact_task:
        db.delete(exact_task)
        db.commit()
        return True
    return False

    
def update_hw_task_db(hid, change_info, new_info):
    db = next(get_db())
    exact_task = db.query(HomeWorkUpload).filter_by(hw_is=hid).first()
    if exact_task:
        if change_info == 'text':
            exact_task.text = new_info
        elif change_info == 'points':
            change_info.points = new_info
        db.commit()
        return True
    return False

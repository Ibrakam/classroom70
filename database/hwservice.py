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


def get_all_or_exact_hw(hwid):
    db = next(get_db())
    if hwid:
        exact_hw = db.query(HomeWork).filter_by(id=hwid).first()
        if exact_hw:
            return exact_hw
        return False
    all_hw = db.query(HomeWork).all()
    return all_hw



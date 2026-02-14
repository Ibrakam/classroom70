"""
1. Добавление класса
2. получение всех и определенного класса
3. изменение
4. удаление

"""
from database import get_db
from database.models import ClassRoom


def create_classrooom_db(name, descr):
    db = next(get_db())
    new_class = ClassRoom(name=name, descr=descr)
    db.add(new_class)
    db.commit()
    return True


def get_all_or_exact_class(cid = 0):
    db = next(get_db())
    if cid:
        exact_class = db.query(ClassRoom).filter_by(id=cid).first()
        if exact_class:
            return exact_class
        return False
    all_class = db.query(ClassRoom).all()
    return all_class


def update_class_db(cid, name=None, descr=None):
    db = next(get_db())
    exact_class = db.query(ClassRoom).filter_by(id=cid).first()
    if exact_class:
        if name:
            exact_class.name = name
        elif descr:
            exact_class.descr = descr
        db.commit()
        return True
    return False

def delete_class_db(cid):
    db = next(get_db())
    exact_class = db.query(ClassRoom).filter_by(id=cid).first()
    if exact_class:
        db.delete(exact_class)
        db.commit()
        return True
    return False


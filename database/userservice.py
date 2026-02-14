from database import get_db
from database.models import User


def create_user_db(name, email, password, group_id, status = "student"):
    db = next(get_db())
    new_user = User(name=name, email=email, password=password, 
                    group_id=group_id, status=status)
    db.add(new_user)
    db.commit()
    return True



# def get_all_users_db():
#     db = next(get_db())
#     all_users = db.query(User).all()
#     return all_users

# def get_exact_user_db(uid):
#     db = next(get_db())
#     exact_user = db.query(User).filter_by(id=uid).first()
#     if exact_user:
#         return exact_user
#     return False

def get_all_or_exact_user(uid = 0):
    db = next(get_db())
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first()
        if exact_user:
            return exact_user
        return False
    all_users = db.query(User).all()
    return all_users


def get_users_by_group(group_id):
    db = next(get_db())
    all_users = db.query(User).filter_by(group_id=group_id).all()
    return all_users


def delete_user_db(uid):
    db = next(get_db())
    delete_user = db.query(User).filter_by(id=uid).first()
    if delete_user:
        db.delete(delete_user)
        db.commit()
        return True
    return False


def update_user_db(uid, change_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=uid).first()
    if exact_user:
        if change_info == "name":
            exact_user.name = new_info
        elif change_info == "email":
            exact_user.email = new_info
        elif change_info == "password":
            exact_user.password = new_info
        db.commit()
        return True
    return False




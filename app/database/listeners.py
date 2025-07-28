from sqlalchemy import event
from sqlalchemy.orm import Session

from app.database.models import Permission, User


def handle_role_change(mapper, connection, target: User):
    db = Session(bind=connection)

    existing_permission = db.query(Permission).filter(Permission.user_id == target.id).first()

    if target.role == "admin":
        if not existing_permission:
            new_permission = Permission(user_id=target.id)
            db.add(new_permission)
            db.commit()
    else:
        if existing_permission:
            db.delete(existing_permission)
            db.commit()

    db.close()


event.listen(User, "before_update", handle_role_change)

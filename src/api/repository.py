from src.api.db import get_db_session


def get_by_id(model_class, obj_id):
    """Fetch a single record by ID."""
    with get_db_session() as session:
        return session.query(model_class).filter_by(id=obj_id).one_or_none()


def get_all(model_class):
    """Fetch all records of a model."""
    with get_db_session() as session:
        return session.query(model_class).all()


def create(model_instance):
    """Create and persist a new model instance."""
    with get_db_session() as session:
        session.add(model_instance)
        session.commit()
        session.refresh(model_instance)
        return model_instance


def update(model_class, obj_id, data: dict):
    """
    Generic update function for SQLAlchemy models.
    - model_class: SQLAlchemy ORM class
    - obj_id: primary key of the object to update
    - data: dictionary of fields to update
    """
    with get_db_session() as session:
        obj = session.query(model_class).filter_by(id=obj_id).one_or_none()
        if not obj:
            return None

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        session.commit()
        session.refresh(obj)
        return obj


def delete(model_class, obj_id):
    """Delete an object by ID."""
    with get_db_session() as session:
        obj = session.query(model_class).filter_by(id=obj_id).one_or_none()
        if not obj:
            return None
        session.delete(obj)
        session.commit()
        return obj

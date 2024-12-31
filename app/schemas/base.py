from pydantic import BaseModel


class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True,  # Позволяет работать с объектами SQLAlchemy
        "extra": "forbid"
    }

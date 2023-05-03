from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Jane Doe"


user = User(id=123)
user_x = User(id=123.45)

assert user.id == 123
assert user_x.id == 123
assert isinstance(user_x.id, int)
assert user.name == "Jane Doe"
assert user.__fields_set__ == {"id"}
assert user.dict() == dict(user) == {"id": 123, "name": "Jane Doe"}

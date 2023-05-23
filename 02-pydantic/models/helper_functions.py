import pickle
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime = None


# parse_obj: dict -> model
model = User.parse_obj({"id": 123, "name": "James"})
print(model)  # id=123 signup_ts=None name='James'

try:
    User.parse_obj(["not", "a", "dict"])
except ValidationError as err:
    print(err)
    # 1 validation error for User
    # __root__
    #   User expected dict not list (type=type_error)


# parse_raw: str | bytes -> dict -> model
model = User.parse_raw('{"id": 123, "name": "James"}')
print(model)  # id=123 signup_ts=None name='James'


pickle_data = pickle.dumps(
    {"id": 123, "name": "James", "singup_ts": datetime(2017, 7, 14)}
)
model = User.parse_raw(
    pickle_data, content_type="application/pickle", allow_pickle=True
)
print(model)  # id=123 signup_ts=None name='James'


# parse_file: file -> bytes -> dict -> model
path = Path("data.json")
path.write_text('{"id": 123, "name": "James"}')
model = User.parse_file(path)
print(model)  # id=123 signup_ts=None name='James'

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

# __fields_set__: 모델 인스턴스 초기화 시 설정되는 필드의 이름 목록
assert user.__fields_set__ == {"id"}

# dict(): 모델의 필드와 값을 딕셔너리로 반환
assert user.dict() == dict(user) == {"id": 123, "name": "Jane Doe"}

# schema: 모델 스키마를 딕셔너리로 반환
target_schema = {
    "title": "User",
    "type": "object",
    "properties": {
        "id": {"title": "Id", "type": "integer"},
        "name": {"title": "Name", "default": "Jane Doe", "type": "string"},
    },
    "required": ["id"],
}
assert user.schema() == target_schema

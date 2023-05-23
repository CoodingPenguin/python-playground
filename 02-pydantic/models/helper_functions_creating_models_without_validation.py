from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int
    name: str = "John Doe"


original_user = User(id=123, age=32)

user_data = original_user.dict()
print(user_data)  # {'id': 123, 'age': 32, 'name': 'John Doe'}

fields_set = original_user.__fields_set__
print(fields_set)  # {'age', 'id'}

# 완전 검증된 데이터일 때만 construct 사용
new_user = User.construct(_fields_set=fields_set, **user_data)
print(repr(new_user))  # User(id=123, age=32, name='John Doe')
print(new_user.__fields_set__)  # {'age', 'id'}

# 검증하지 않기 떄문에 유효하지 않은 데이터가 들어가 버림
bad_user = User.construct(id="dog")
print(repr(bad_user))  # User(id='dog', name='John Doe')

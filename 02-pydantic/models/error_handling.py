from pydantic import BaseModel, ValidationError, conint


class Location(BaseModel):
    latitude = 0.1
    longitude = 10.1


class Model(BaseModel):
    is_required: float
    gt_int: conint(gt=42)
    list_of_ints: list[int] = None
    a_float: float = None
    recursive_model: Location = None


data = dict(
    list_of_ints=["1", 2, "bad"],
    a_float="not a float",
    recursive_model={"latitude": 4.2, "longitude": "New York"},
    gt_int=21,
)

try:
    Model(**data)
except ValidationError as err:
    print(err)
    # 5 validation errors for Model
    # is_required
    #   field required (type=value_error.missing)
    # gt_int
    #   ensure this value is greater than 42 (type=value_error.number.not_gt; limit_value=42)
    # list_of_ints -> 2
    #   value is not a valid integer (type=type_error.integer)
    # a_float
    #   value is not a valid float (type=type_error.float)
    # recursive_model -> longitude
    #   value is not a valid float (type=type_error.float)


try:
    Model(**data)
except ValidationError as err:
    print(err.json())
    # [
    #   {
    #     "loc": [
    #       "is_required"
    #     ],
    #     "msg": "field required",
    #     "type": "value_error.missing"
    #   },
    #   {
    #     "loc": [
    #       "gt_int"
    #     ],
    #     "msg": "ensure this value is greater than 42",
    #     "type": "value_error.number.not_gt",
    #     "ctx": {
    #       "limit_value": 42
    #     }
    #   },
    #   {
    #     "loc": [
    #       "list_of_ints",
    #       2
    #     ],
    #     "msg": "value is not a valid integer",
    #     "type": "type_error.integer"
    #   },
    #   {
    #     "loc": [
    #       "a_float"
    #     ],
    #     "msg": "value is not a valid float",
    #     "type": "type_error.float"
    #   },
    #   {
    #     "loc": [
    #       "recursive_model",
    #       "longitude"
    #     ],
    #     "msg": "value is not a valid float",
    #     "type": "type_error.float"
    #   }
    # ]

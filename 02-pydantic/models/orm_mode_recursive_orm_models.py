from pydantic import BaseModel


class PetCls:
    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species


class PersonCls:
    def __init__(self, *, name: str, age: float = None, pets: list[PetCls]):
        self.name = name
        self.age = age
        self.pets = pets


class Pet(BaseModel):
    name: str
    species: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    name: str
    age: float = None
    pets: list[Pet]

    class Config:
        orm_mode = True


bones = PetCls(name="Bones", species="dog")
orion = PetCls(name="Orion", species="cat")
anna = PersonCls(name="Anna", age=20, pets=[bones, orion])

# Pet을 from_orm 하지 않아도 알아서 recursive하게 파싱해줌
anna_model = Person.from_orm(anna)
print(anna_model)
# name='Anna' age=20.0 pets=[Pet(name='Bones', species='dog'), Pet(name='Orion', species='cat')]

import typing as t
from collections.abc import Iterable


class WrongFormatError(Exception):

    def __init__(self, errors: dict = '') -> None:
        self.msg = 'Invalid data type'
        self.errors = errors
        super().__init__(self.msg)


class BaseModel:

    def __init__(self, **kwargs: t.Any) -> None:
        errors: dict = {}

        for key in kwargs:
            value: t.Any = kwargs[key]
            type_: list[type] | type = self.__annotations__[key]

            try:
                if hasattr(type_, '__args__'):
                    if type(value) not in type_.__args__:
                        errors[key] = (f'{key} has invalid type:',
                                       f'{type(key)}. Need: {type_}')
                        type_ = type_.__args__[-1]
                    else:
                        type_: type = type(value)
                value: type = type_(value)

            except ValueError:
                errors[key] = (f'{key} has invalid type: {type(key)}.',
                               'Need: {type_}')

            else:

                if hasattr(self, key):
                    val: t.Any = getattr(self, key)

                    if isinstance(val, Iterable) and type(val) != str:
                        if value not in val:
                            errors[key] = f'{key} doesn\'t match {val}'
                            continue

                    elif value != val:
                        errors[key] = f'{key} doesn\'t match {val}'
                        continue

                setattr(self, key, type_(value))

        if errors:
            raise WrongFormatError(errors)


class Human(BaseModel):
    name: str = 'zxczxczxc'
    age: int = range(17, 22)
    height: float = 170
    smth: tuple

    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.height} {self.smth}'


data = {
    'name': 'zxczxczxc',
    'age': '18',
    'height': 170,
    'smth': [1,2,3,4]
}

try:
    human: Human = Human(**data)
    print(human)
except WrongFormatError as err:
    print(err.errors)


class Any(BaseModel):
    any: int | float


data = {
    'any': 21.57
}

try:
    any_: Any = Any(**data)
    print(any_.any)
except WrongFormatError as err:
    print(err.errors)

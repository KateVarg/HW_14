import dataclasses


@dataclasses.dataclass
class User:
    name: str
    mail: str
    phone: str
    question: str

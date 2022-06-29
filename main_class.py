"""
Sukurti programą, kuri:
Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
import datetime

engine = create_engine('sqlite:///employees.db')
Base = declarative_base()


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birthday = Column(String)
    position = Column(String)
    salary = Column(Integer)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name: str, surname: str, birthday: str, position: str, salary: int):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname}, {self.birthday}, {self.position}, {self.salary}, {self.start_date}"


Base.metadata.create_all(engine)

import json
from abc import ABC, abstractmethod
from src.mixin_comparison_vacancy import ComparisonVacancy

from config import JSON_HH
from src.verification import SalaryVerify


class Vacancy(ABC):
    """Абстрактный класс для всех вакансий"""

    @classmethod
    @abstractmethod
    def get_data(cls):
        pass


class VacancyHH(Vacancy, ComparisonVacancy, SalaryVerify):
    """Класс для вакансий с сайта HH"""

    def __init__(self, title: str, link: str, description: str, salary: int) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: {self.salary} \n\n"
        )

    @classmethod
    def get_data(cls) -> None:
        with open(JSON_HH, "r") as file:
            vacancy = json.load(file)
            vacancy_s = []
            for i in vacancy:
                vacancy_s.append(
                    VacancyHH(
                        i["name"],
                        i["alternate_url"],
                        i["snippet"]["responsibility"],
                        i["salary"],
                    )
                )
        vacancy_s = sorted(vacancy_s, key=lambda x: x.salary, reverse=True)
        for vacancy in vacancy_s:
            print(vacancy)


class VacancySJ(Vacancy, ComparisonVacancy, SalaryVerify):
    """Класс вакансий с сайта SuperJob"""

    def __init__(self, title: str, link: str, description: str, salary: str):
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: {self.salary} \n\n"
        )

    @classmethod
    def get_data(cls) -> None:
        with open(JSON_HH, "r") as file:
            vacancy = json.load(file)
            vacancy_s = []
            for i in vacancy:
                vacancy_s.append(
                    VacancySJ(
                        i["profession"],
                        i["link"],
                        i["candidat"],
                        i["payment_from"],
                    )
                )
        vacancy_s = sorted(vacancy_s, key=lambda x: x.salary, reverse=True)
        for vacancy in vacancy_s:
            print(vacancy)
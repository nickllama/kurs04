class SalaryVerify:
    """Verification the salary attribute of the Vacancy class."""

    def __init__(self, salary):
        self.salary = salary

    @classmethod
    def verify_salary(cls, salary):
        if isinstance(salary, dict):
            if (salary["from"] is not None) and (salary["to"] is not None):
                if salary["from"] <= salary["to"]:
                    return salary["from"]
                elif salary["from"] >= salary["to"]:
                    return salary["to"]
            elif salary["from"] is None:
                return salary["to"]
            else:
                return salary["from"]
        elif isinstance(salary, (int, float)):
            return salary
        else:
            return 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        salary = self.verify_salary(salary)
        self.__salary = salary
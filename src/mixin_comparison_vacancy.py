class ComparisonVacancy:
    """To compare salaries for vacancies."""

    def __init__(self, salary):
        self.salary = salary

    def __lt__(self, other):
        """For comparison 'less'."""
        if isinstance(other, self.__class__):
            return self.salary < other.salary

    def __gt__(self, other):
        """For comparison 'more'."""
        if isinstance(other, self.__class__):
            return self.salary > other.salary

    def __le__(self, other):
        """For comparison 'less or equal'."""
        if isinstance(other, self.__class__):
            return self.salary <= other.salary

    def __ge__(self, other):
        """For comparison 'more or equal'."""
        if isinstance(other, self.__class__):
            return self.salary >= other.salary

    def __eq__(self, other):
        """For comparison 'equal'."""
        if isinstance(other, self.__class__):
            return self.salary == other.salary

    def __ne__(self, other):
        """For comparison 'unequal'."""
        if isinstance(other, self.__class__):
            return self.salary != other.salary
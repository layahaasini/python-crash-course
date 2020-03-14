class Employee():
    """Stores default and custom raises."""
    def __init__(self, first, last, salary):
        """Initializes the first, last and salary attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, annual_raise = ''):
        """Adds 5000 to the salary by default, but can also add custom raises."""
        if annual_raise:
            self.salary = int(self.salary) + int(annual_raise)
        else:
            self.salary = int(self.salary) + 5000
        print(self.salary)
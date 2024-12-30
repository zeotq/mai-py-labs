vacancies = {
    "Junior": {"payments": 10, "next": "Middle"},
    "Middle": {"payments": 15, "next": "Senior"},
    "Senior": {"payments": 20, "next": "Senior"}
}


class Programmer(object):
    def __init__(self, 
                 name: str | None = "NULL",
                 vacancie_key: str | None = None):
        self.name = name
        self.vacancie = vacancie_key
        self.hours = 0
        self.money = 0
        self.pay = vacancies[self.vacancie]['payments']

    def work(self, hours: int | None = 0):
        self.hours += hours
        self.money += hours * self.pay

    def rise(self):
        if self.vacancie == vacancies[self.vacancie]['next']:
            self.pay += 1
        else:
            self.vacancie = vacancies[self.vacancie]['next']
            self.pay = vacancies[self.vacancie]['payments']

    def info(self):
        return f"{self.name} {self.hours}ч. {self.money}тгр."
    

def main():
    programmer = Programmer('Васильев Иван', 'Junior')
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())


if __name__ == "__main__":
    main()
from enum import Enum


roles = ["Junior", "Middle", "Senior"]

salary = {
    roles[0]: 10,
    roles[1]: 15,
    roles[2]: 20
}



class Programmer:

    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.role_index = roles.index(job)
        self.time = 0
        self.rise_count = 0
        self.current_salary = salary[job]
        self.current_money = 0

    def work(self, time):
        self.time += time
        self.current_money += time * self.current_salary

    def rise(self):
        if self.role_index != len(roles) - 1:
            self.role_index += 1
            self.job = roles[self.role_index]
            self.current_salary = salary[self.job]
        else:
            self.current_salary = salary[self.job] + 1

    def get_money(self):
        return self.current_salary * self.time

    def info(self):
        return f"{self.name} {self.time}ч. {self.current_money}тгр."



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


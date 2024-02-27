
class IATERSTUFF:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Programmer(IATERSTUFF):
    def __init__(self, name, age, level, salary):
        super().__init__(name, age)
        self.levle = level
        self.salary = salary
    
    def showData(self):
        return ('name: ', self.name, 'age: ', self.age, 'level: ', self.levle, 'salary: ', self.salary)

done = Programmer('Done', 19, 'year 1', 5_00_000)
yao = Programmer('Yao', 19, 'year 1', 5_00_000)

print(done,'/n',yao)

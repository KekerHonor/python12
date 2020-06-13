class Person: #Tom usgeer ehelne
    def __init__(self, name: str, age: int):
        self.__name=name
        self.__age=age
    def say_hi(self):
        print("Hi I am",self.__name, self.__age)

class Student(Person):
    def __init__(self, name, age, code):
        super().__init__(name, age)
        self.code = code

class Worker(Person):
    def __init__(self, name:str, age, profession):
        super().__init__(name, age)
        self.profession = profession
w1 = Worker("Bold", 23, "Programmist")
w1.say_hi()
print("And I am",w1.profession)
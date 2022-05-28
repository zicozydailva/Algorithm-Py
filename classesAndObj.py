class Student: 
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

Student1 = Student("Bob", 28, "FE", 90.0)
Student2 = Student("Paul", 24, "UI", 85.0)

print(Student1.name)
print(Student1.age)
print(Student1.track)
print(Student1.score)

print(Student2.name)
print(Student2.age)
print(Student2.track)
print(Student2.score)
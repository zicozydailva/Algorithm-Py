class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name (self, new_name):
        old_name = self.name
        self.name = new_name
        print(f"Name was chanced from {old_name} to {new_name}")

    def change_age (self, new_age):
        if type(new_age) != int:
            print(f"{new_age} is not an integer so age remains {self.age}")
        else:
            old_age = self.age
            self.age = new_age
            print(f"Age was chanced from {old_age} to {new_age}")
    
    def add_track (self, new_track):
        self.tracks.append(new_track)
        updated_list = ",".join(self.tracks)
        print(f"{new_track} was added to list of tracks so tracks enrolled in are {updated_list}")

    def get_score (self):
        print(f"Student's score is {self.score}")

    def change_score (self, new_score):
        if type(new_score) != int and type(new_score) != float:
            print(f"{new_score} is not a number so score remains {self.score}")
        else:
            old_score = self.score
            self.score = new_score
            print(f"Score was chanced from {old_score} to {new_score}")



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
Bob.change_score(30.0)
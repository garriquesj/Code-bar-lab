
class Member:
    def __init__(self,full_name):
        self.full_name = full_name
    def welcome(self):
        print(f"Hello {self.full_name}!")
jason = Member("jay")
jason.welcome()

class Student(Member):
    def __init__(self, full_name, reason ):
        super().__init__(full_name)
        self.reason= reason
    def about_me(self):
        print(f"{self.full_name} codes because {self.reason}")

stephen = Student("Stephen", "he like to learn")
stephen.about_me()
class Instructor(Member):
    def __init__(self, full_name, bio, skills=[]):
        super().__init__(full_name)
        self.bio = bio
        self.skills = ["Python", "Javascript", "C++"]
    def add_skill(self, new_skills):
        self.skills.extend(new_skills)
    def test(self):
        print(f"My name is {self.full_name} I like {self.bio} my skills are {self.skills}") 

eric = Instructor("Eric", "Duke and puppies", "")
eric.test()
class Workshops:
    def __init__(self, date, subject, instuctors, students):
        self.date = date
        self.subject = subject
        self.instructor = instructor
        self.students = students






# ______________________________________________________

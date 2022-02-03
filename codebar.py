
class Member:
    def __init__(self,full_name, introduce):
        self.full_name = full_name
        self.introduce = introduce
    def welcome(self):
        print(f"Hello {self.full_name}!")
jason = Member("jay","Whatsup")
jason.welcome()

class Student:
    def __init__(self,full_name, reason ):
        super().__init__(full_name)
        self.reason= reason
        print(f'{full_name} codes because ')
jason = Students("jay", "I like to learn")

class Instructor:
    def __init__(self, full_name, bio, skills):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self,new_skills):
        self.skills.extend(new_skills)
    def test(self):
        print(f'My name is {full_name} I like {bio} my skills are{skills}')    
eric = Instructor("Eric", "Duke and puppies",["coding","teaching","holding puppies"])
class Workshops:
    def __init__(self, date, subject, instuctors, students):
        self.date=date
        self.subject=subject
        self.instructor=instructor
        self.students=students






# ______________________________________________________


class Member:
    def __init__(self,full_name, introduce)
        self.full_name=full_name#SELF LINKS PARAM TO KEY
        self.introduce=introduce
# ______________________________________________________
class Student:
    def __init__(self,full_name, reason )
        super().__init__(full_name)#calls full name in MEMBER CLASS
        self.reason= reason
# ______________________________________________________
class Instructor:
    def __init__(self, full_name, bio, skills)#maybe I should tell it the parameter is a list
        super().__init__(full_name)
        self.bio=bio
        self.skills=[]#incase of multiple skills?
# ______________________________________________________
    def add_skill(self,new_skills):#take param of skills and self?do put this in or above instructor
        self.skills.extend(skills)#should extend skill array *****
# ______________________________________________________

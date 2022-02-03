
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
    def __init__(self, full_name, bio, skils)#maybe I should tell it the parameter is a list
        super().__init__(full_name)
        self.bio=bio
        self.skils=[]#incase of multiple skills?

# ______________________________________________________

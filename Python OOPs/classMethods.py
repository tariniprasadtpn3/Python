class Student:

    school = "SSVM"

    @classmethod
    def info(cls):
        return cls.school
    
print(Student.info())
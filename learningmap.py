class LearningMap(object):
    def __init__(self, user):
        self.name = name
        

    def add_skills(self, value):
        global my_skills = []
        count  = 0
        while count <= 10:
            value = raw_input("Add a skill:")
            my_skills.append(value)
            count += 1
        
    def view_skills(self):
        for i,skill in enumerate(my_skills):
            return (i+1, skill)

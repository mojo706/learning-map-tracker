class LearningMap(object):
    def __init__(self, user):
        self.user = user
        my_skills=[]

    def add_skills(self):
        count  = 0
        value = ''
        while count <= 5:
            value = raw_input("Add a skill:")
            my_skills.append(value)
            count += 1
        
    def view_skills(self):
        for i,skill in enumerate(my_skills):
            return (i+1, skill)


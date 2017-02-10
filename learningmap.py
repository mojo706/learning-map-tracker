class LearningMap(object):

  def __init__(self, user): # initilize the class
    self.user = user
    self.my_skills = []
    
  def add_skills(self):

    count  = 0
    value = ''
    while count <= 4:
      value = raw_input("Add a skill:")
      self.my_skills.append(value)
      count += 1
        
  def view_skills(self):
    for i,skill in enumerate(self.my_skills): # Added the enumerate function to get the index and value from my_skills
      print '%d. %s' % (i+1, skill) # Add formatters for better output


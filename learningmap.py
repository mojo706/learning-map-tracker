class LearningMap(object):

  def __init__(self, user):
    self.user = user
    self.my_skills = []
    self.studied_skills = []
    
  def add_skills(self):

    count  = 0
    value = ''
    while count <= 4:
      value = raw_input("Add a skill:")
      self.my_skills.append(value)
      count += 1
        
  def view_skills(self):
    for i,skill in enumerate(self.my_skills): # Loop through my_skills getting index and 
      print '%d. %s' % (i+1, skill) # Added String formatters
      
  def skills_studied(self):
    studied_skills = []
    value2 = 'Yes'
    
    while value2 == "Yes":
      value1 = raw_input("Enter skill completed:")
      self.studied_skills.append(value1)
      value2 = raw_input("Any other skill? (Yes or No)" )
      
  def skills_not_studied(self):
    setMySkills = set(self.my_skills)
    setStudiedSkills = set(self.studied_skills)
    set_skills_not_studied = setMySkills - setStudiedSkills
    list_skills_not_studied = list(set_skills_not_studied)
    print ('skills not studied')
    for i,skill in enumerate(list_skills_not_studied):
      print '%d. %s' % (i+1, skill) # Add string formatters

  def progress(self):
        a = len(self.my_skills)
        b = len(self.studied_skills)
        c = (float(b)/a) * 100
        print ('you have completed '+ str(c)+ '%')


class student:
  def sum(self,a=None,b=None,c=None):
    if a!= None and b!= None and c!= None:
      print (a+b+c)
    elif a!= None and b!= None:
      print (a+b)
    else: 
      print (a)
    
a = student()
a.sum(5,2,9)

class topten:
  def __init__(self) -> None:
    self.num = 1
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.num <= 10:
      var = self.num
      self.num += 1
      return var
    else:
      raise StopIteration

values = topten()

for i in values:
  print (i)
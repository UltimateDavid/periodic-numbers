class Number:
  def __init__(self, number):
    self.number = number
  
  # Find the path from this number onwards for a few iterations
  def printNumber(self,iterations):
    result = str(self.number)
    num = self.number
    for i in range(0,iterations):
      volgend = self.Func(num)
      result += "->" + str(nextnum)
      num = nextnum
    print(result)
      
  # Find the next periodic number in the current row
  def periodic(self,iterations):
    arr = []
    num = self.number
    arr.append(num)
    # Loop the function often enough until coming across a periodic number
    for i in range(0,iterations):
      nextnum = self.Func(num)
      # Check if this number was already seen before
      boolean = 0
      for member in arr:
        if nextnum == member: boolean = 1
      if boolean == 0:
        # If not, add it to the list
        arr.append(nextnum)
        num = nextnum
      else:
        # If found before, return this periodic number
        return nextnum
        break
  
  # Calculate the period of a number (USE ONLY FOR ACTUAL PERIODIC NUMBERS)
  def period(self):
    num = self.number
    nextnum = None
    i = 0
    # Iterate while the number has not seen itself again
    while nextnum != self.number:
      nextnum = self.Func(num)
      num = nextnum
      # Count the period
      i += 1
    return i
  
  # The actual function that is iterated upon every turn
  def Func(self,number):
  result = (number*2)%360
  return result

# [ MAIN ]
# Initialisation
# Two arrays where the position matches
arrNum= [] # containing all the periodic numbers
arrPeriod = [] # containing their periods
iterations = 20

# We will be checking every number between 0 and 360.
for i in range (0,360):
  n = Number(i)
  # Calculate the first periodic number in # iterations
  periodicNum = n.periodic(iterations)
  # Make this an object and check if it has been found before
  p = Number(periodicNum)
  boolean = 0
  for member in arrNum:
    if periodicNum == member: boolean = 1
  if boolean == 0:
    # If it is a new one, add it
    arrNum.append(periodicNum)
    # Sort the array in ascending order
    arrNum.sort()
    # Add the period in the same position as this number
    arrPeriod.insert(arrNum.index(periodicNum), p.periode())

# [ PRINT ]
# Print the periodic numbers with their period
for i in range(0, len(arrNum)):
  print(str(arrNum[i])+' with period '+str(arrPeriod[i]))
print('---------------------------')
print('Periodic points: '+ str(arrNum))
print('Total numbers: '+str(len(arrNum)))
# Print the period for every number
for j in range(1,20):
  # If there are no numbers with a specific period, ignore them
  if arrPeriod.count(j)!=0:
    print('# numbers with period '+str(j)+': '+str(arrPeriod.count(j)))

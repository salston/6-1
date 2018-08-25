import random

#
# CLASSES -----------------------------------
#

class Results:

  def __init__(self):
    self.total = 0
    self.count = 0

  def addCorrect(self):
    self.total += 1
    self.count += 1

  def addWrong(self):
    self.count += 1

  def result(self):
    a = self.total / self.count
    return a

  def print(self):
    print(self.total, self.count)
    print(self.result())

#
# FUNCTIONS ----------------------------------
#

def readData(file):
  with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

  print("File lines:", len(lines))

  data = []
  for line in lines[1:]: #do not include header line
    j = line.split(',')
    for n in j[4:11]:
      data.append(int(n))
      #print(n)
  print("Numbers in Data:", len(data))  #should be 1 less than file lines time 7 because of header
  print("Check:", (len(lines)-1)*7, '\n')
  return data

#
# Random
#

def randomDraw():
  s = list(range(1,50))
  return random.choice(s)

def randomTrial(winners):
  # train algorythm with first 5000
  #     do nothing this is not a trained algorythim

  r = Results()
  for w in winners[5000:]:
    p = randomDraw()
    if p == w:
      r.addCorrect()
    else:
      r.addWrong()
  return r

#
# Converted to here
#

#
# Least
#

def leastPickedDraw(tallies):
  # get a list of tallies keys revrse ordered by value
  s = sorted(tallies, key=tallies.__getitem__, reverse=True)
  p = []
  for i in s[:6]:
    p.append(i)
  return(p)

def leastPickedTrail(winners):
  # train algorythm with first 2000
  #     count up # times each number is picked
  tallies = {x: 0 for x in range(1, 50)}
  for w in winners[:1999]:
    for n in w.numbers:
      tallies[n] = tallies[n] +1
    tallies[w.bonus] = tallies[w.bonus] +1 

  # Picks
  r = Results()
  for w in winners[2000:]:
    p = leastPickedDraw(tallies)
    win = winnings(p, w.numbers, w.bonus)
    r.add(win)
    # update tallies 
    for n in w.numbers:
      tallies[n] = tallies[n] +1
    #tallies[w.bonus] = tallies[w.bonus] +1 
  return r

#
# Most
#

def mostPickedDraw(tallies):
  # get a list of tallies keys revrse ordered by value
  s = sorted(tallies, key=tallies.__getitem__)
  p = []
  for i in s[:6]:
    p.append(i)
  return(p)

def mostPickedTrail(winners):
  # train algorythm with first 2000
  #     count up # times each number is picked
  tallies = {x: 0 for x in range(1, 50)}
  for w in winners[:1999]:
    for n in w.numbers:
      tallies[n] = tallies[n] +1
    tallies[w.bonus] = tallies[w.bonus] +1 

  # Picks
  r = Results()
  for w in winners[2000:]:
    p = mostPickedDraw(tallies)
    win = winnings(p, w.numbers, w.bonus)
    r.add(win)
    # update tallies 
    for n in w.numbers:
      tallies[n] = tallies[n] +1
    tallies[w.bonus] = tallies[w.bonus] +1 
  return r

#
# Trials
#

def trials(winners, method, n=1):
  random.seed()

  rTotals = Results()
  
  for i in range(n):
    # create trial and add it to total
    r = method(winners)
    for k, v in r.results.items():
      rTotals.add(k, v)
  # Find and print the average values
  rAvg = Results()
  for k, v in rTotals.results.items():
      rAvg.add(k, v/n)
  print(method.__name__, '# Trials:', n)
  rAvg.pr()
  #print(rAvg.results)  


#
# MAIN ------------------------------------------
#

def main():
  winners = readData('data.csv')

  r = randomTrial(winners)
  r.print()

  #trials(winners, randomTrial, 100)

  #trials(winners, leastPickedTrail)

  #trials(winners, mostPickedTrail)
        


if __name__ == "__main__":
    main()

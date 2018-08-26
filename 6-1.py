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

  def pr(self):
    print(self.total, self.count)
    print(self.result())


class Tally:

  def __init__(self):
    self.tallies = {x: 0 for x in range(1, 50)}

  def add(self, n):
    # count up # times each number is picked
    self.tallies[n] = self.tallies[n] + 1

  def least(self):
    # get a list of tallies keys reverse ordered by value
    s = sorted(self.tallies, key=self.tallies.__getitem__, reverse=True)
    return s[0]

  def most(self):
    # get a list of tallies keys ordered by value
    s = sorted(self.tallies, key=self.tallies.__getitem__)
    return s[0]

  def rank(self, n):
    # get a list of tallies keys reverse ordered by value
    s = sorted(self.tallies, key=self.tallies.__getitem__, reverse=True)
    return s.index(n) + 1


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
      # zero's in the draw numbers indicate there was no bonus #
      # we ignore these
      if (n!='0'):
        data.append(int(n))
      #print(n)
  print("Numbers in Data:", len(data))  #should be 1 less than file lines time 7 because of header
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
# Least
#

def leastPickedTrail(winners):
  # train algorythm with first 5000
  #     count up # times each number is picked
  t = Tally()
  for n in winners[:4999]:
    t.add(n)

  # Picks
  r = Results()
  for w in winners[5000:]:
    p = t.least()
    if (p == w):
      r.addCorrect()
    else:
      r.addWrong()
    # update tallies
    t.add(w) 
  return r

#
# Most
#

def mostPickedTrail(winners):
  # train algorythm with first 5000
  #     count up # times each number is picked
  t = Tally()
  for n in winners[:4999]:
    t.add(n)

  # Picks
  r = Results()
  for w in winners[5000:]:
    p = t.most()
    if (p == w):
      r.addCorrect()
    else:
      r.addWrong()
    # update tallies
    t.add(w) 
  return r


#
# Trials
#

def trials(winners, method, n=1):

  rTotals = Results()

  rSum = 0
  for i in range(n):
    # create trial and add it to total
    r = method(winners)
    #r.pr()
    rSum += r.result()
    
  # Find and print the average values
  print(method.__name__, '- Trails:', n, '- Average:', rSum / n)  

#
# Ranks
#

def ranks(winners):
  # train algorythm with first 5000
  #     count up # times each number is picked
  t = Tally()
  for n in winners[:4999]:
    t.add(n)

  # Rank rest of numbers
  rs = []
  for w in winners[5000:]:
    rs.append(t.rank(w))
    t.add(w)
  a = sum(rs) / len(rs)
  return a
  

#
# MAIN ------------------------------------------
#

def main():
  random.seed()
  
  winners = readData('data.csv')

  trials(winners, randomTrial, 10)

  trials(winners, leastPickedTrail)

  trials(winners, mostPickedTrail)

  print('average rank:', ranks(winners))


if __name__ == "__main__":
    main()

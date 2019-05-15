import time
from datetime import date, timedelta


def logHit(id, time):
  global userVisits

  if id not in userVisits:
    userVisits[id] = [time]
  else:
    userVisits[id][len(uservisits)-1] = time


def getHitLast5Min():
  now = date.today()
  count = 0

  for user in userVisits:
    for time in user:
      if now - time <= 5*60*1000:
        count += 1

  return count



def testVisits():
  global userVisits

  for i in range(100):
    #time.sleep(100)
    logHit('user'+str(i), date.today())

  n = getHitLast5Min()

  if n != 1000:
    print(n)
    return "Failure"

  return "Success"


userVisits = {}
testVisits()
print("Hello")



# Your last JavaScript (Node) code is saved below:
# //Desing and implement 2 functions
# //1. logHit => no args, return null
# //2. getHitlast5Min => no args, return number
# //teechip.com
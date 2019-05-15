# Your last JavaScript (Node) code is saved below:
# //Desing and implement 2 functions
# //1. logHit => no args, return null
# //2. getHitlast5Min => no args, return number
# //teechip.com
import time
import datetime


def logHit(id, time):
  global userVisits

  if id not in userVisits:
    userVisits[id] = [time]
  else:
    userVisits[id][len(uservisits)-1] = time


def getHitLast5Min():
  global userVisits
  now = datetime.datetime.now()
  count = 0

  for user, times in userVisits.items():
    for time in times:
      if ((now - time).total_seconds() / 60) <= 5:
        count += 1

  return count



def testVisits(num_users=1000, sleep_sec=1):
  global userVisits

  for i in range(num_users):
    time.sleep(sleep_sec) # one user per second, i.e. 60 users per minute
    logHit('user_'+str(i), datetime.datetime.now())
    
  n = getHitLast5Min()

  if n != 5*60: # 60*5 users in five minutes expected.
    print(n)
    print("Failure")

  print("Success")


userVisits = {}
testVisits()

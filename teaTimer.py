#Timer
import math
import time
import sys
x=60

#Output requesting input:
teaType = input('What tea are you brewing? Green, Earl Grey, or Chai?')
teaType = str.lower(teaType)

#Variable Time Changer
if teaType == "green":
    AftBoil = x * 2.68
    steep = x * 3.68
elif teaType == "earl grey":
    AftBoil = x * 1.68
    steep = x * 4.68
elif teaType == "chai":
    AftBoil = x * 3.18
    steep = x * 4.68
    pass

#Output to screen:
print('\n')
minutes = int((AftBoil-(AftBoil%x))/x)
seconds = int(AftBoil%x)
print(math.ceil(seconds))
print("Boiling! Current time is " + time.ctime() + ".")
print('\n')
for i in range(minutes,0,-1):
    for j in range(seconds,0,-1):
        print(time.time(), time.clock())
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        sys.stdout.write(str(j)+' ')
        sys.stdout.flush()
        time.sleep(1)
        #print(i)
        #print(j)
        

print("Time to steep! Current time is " + time.ctime() + ".")
print('\n')
for i in range(minutes,0,-1):
    for j in range(seconds,0,-1):
        time.sleep(1)
#time.sleep(steep)

print("Done steeping. Squeeze the bag with the wrapper and throw them away.  Current time is " + time.ctime() + ".")
print('\n')
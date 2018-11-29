
# coding: utf-8

# In[1]:


import datetime;

def init(sList):
    global startTime
    startTime = 1543503400

    global startList
    startList = sList

    minutesSinceStart()
    global latestList 
    latestList = startList
    global latestTime
    latestTime = startTime
    currentChannel(latestTime, latestList)




# In[2]:


def currentEpoch():
    return int(datetime.datetime.now().timestamp())
def currentMinute():
    curr = currentEpoch()
    return curr-curr%60
def minutesSince(newTime, oldTime):
    return int((newTime-oldTime)/60)
def minutesSinceStart():
    return minutesSince(currentMinute(), startTime)


# In[3]:




# In[4]:


def updateList(latestTime, latestList):
    newTime = currentMinute()
    minSinceUpdate = minutesSince(newTime, latestTime)
    if(minSinceUpdate >= len(latestList)):
        latestTime, latestList = reorder(latestTime, latestList)
        print("Update Time! :)")
    else:
        print("Same Time, same list :/")
    return latestTime, latestList


def updateListToTime(latestTime, latestList, newTime):
    minSinceUpdate = minutesSince(newTime, latestTime)
    if(minSinceUpdate >= len(latestList)):
        latestTime, latestList = reorder(latestTime, latestList)
        print("Update Time! :)")
    else:
        print("Same Time, same list :/")
    return latestTime, latestList


# ---

# In[5]:


import random


# In[6]:


def getSeed(latestList):
    subList = latestList[-5:]
    newSeed = ord(subList[0][0])*100+ord(subList[1][0])*10+ord(subList[2][0])+ord(subList[3][0])*1000+ord(subList[4][0])*10000
    return newSeed


# In[7]:


def randomizeBySeed(latestList, seed, verbose=False):
    localList = latestList.copy()
    random.seed(seed)
    newList = []
    for i in range(0, len(localList)):
        newIndex = random.randint(0, len(localList)-1)
        newList.append(localList.pop(newIndex))
    if(verbose):
        print("******"*2)
        print(latestList)
        print("*** becomes ***")
        print(newList)  
        print("******"*2)
    return newList


# In[8]:


def reorder(latestTime, latestList, verbose=False):
    minutesSinceReorder = minutesSince(currentMinute(), latestTime)
    seed = getSeed(latestList)
    newTime = latestTime+(60*len(latestList))

    newList = randomizeBySeed(latestList, getSeed(latestList), verbose)
    minutesSinceReorder=minutesSince(currentMinute(), newTime)
    if(minutesSinceReorder>= len(newList)):
        if(verbose):
            print("Its been too long! "+ str(minutesSinceReorder)+" minutes remaining, Running Again...")
            print("Minutes remaining must be less than "+ str(len(newList))+"\n")
        newTime, newList = reorder(newTime, newList)
    else: 
        if(verbose):
            print("Success!", minutesSinceReorder,"minutes since reorder!")

    return newTime, newList


# ---

# In[9]:



def currentChannel(latestTime, latestList):
    latestTime, latestList = updateList(latestTime, latestList)
    print(latestTime, latestList)
    return latestList[0]


# In[10]:


class Activity:         #create template for activity objects
    def __init__(self,activity,pointsGain,count=0):
        self.Activity=activity
        self.Points=pointsGain
        self.Count=count

class Reward:       #create template for reward objects
    def __init__(self,reward,pointNeed,count=0):
        self.Reward=reward
        self.Points=pointNeed
        self.Count=count

#reads activity file and compile all activity objects in a list for easy updating
def activities_get():

    with open("Activities.txt","r") as actFile:
        actList=[]
        for i in range(2):
            actFile.readline()

        for line in actFile:
            line=line.strip()
            details=line.split("|")
            activity=Activity(details[0],int(details[1]),int(details[2]))
            actList.append(activity)


    return actList


# reads reward file and compile all reward objects in a list for easy updating
def rewards_get():
    with open("Rewards.txt", "r") as rewFile:
        rewList = []
        for i in range(2):
            rewFile.readline()
        for line in rewFile:
            line = line.strip()
            details = line.split("|")
            reward = Reward(details[0], int(details[1]), int(details[2]))
            rewList.append(reward)

    return rewList

#reads inventory and compile in list
def inventory_get():

    with open("RewardInventory.txt","r") as file:
        inv=[]

        for line in file:
            item=line.strip()
            inv.append(item)

    return inv

#read point file for points
def get_myPoints():
    with open("PointRecord.txt") as file:   #no need "r" works too apparently
        myPoints=file.readline().strip().split(":")[1].strip()
    return int(myPoints)

def get_TotalPoints():
    with open("PointRecord.txt") as file:
        file.readline()
        TotPoints=file.readline().strip().split(":")[1].strip()
    return int(TotPoints)

# overwrites points file to save updated points
def update_pointsFile(thelist, step, index, prevPoints, prevTot):
    realIndex = index - 1
    if step == "add":
        with open("PointRecord.txt", "w") as file:
            curPoints = prevPoints + int(thelist[realIndex].Points)
            curPointsLine = "My Current Points: " + str(curPoints) + "\n"
            file.write(curPointsLine)

            curTotal = prevTot + int(thelist[realIndex].Points)
            curTotalLine = "My Accumulated Total Points: " + str(curTotal)
            file.write(curTotalLine)

    elif step == "minus":
        with open("PointRecord.txt", "w") as file:
            curPoints = prevPoints - int(thelist[realIndex].Points)
            curPointsLine = "My Current Points: " + str(curPoints) + "\n"
            file.write(curPointsLine)

            curTotalLine = "My Accumulated Total Points: " + str(prevTot)
            file.write(curTotalLine)


# takes updated lists that store activity/reward objects and overwrites/saves in text file
def update_activityFile(actList):
    with open("Activities.txt", "w") as file:
        header = "Activity|Points|Count" + "\n" * 2
        file.write(header)

        for activity in actList:
            line = activity.Activity + "|" + str(activity.Points) + "|" + str(activity.Count) + "\n"
            file.write(line)


def update_rewardFile(rewList):
    with open("Rewards.txt", "w") as file:
        header = "Reward|Points|Count" + "\n" * 2
        file.write(header)

        for reward in rewList:
            line = reward.Reward + "|" + str(reward.Points) + "|" + str(reward.Count) + "\n"
            file.write(line)


# create timestamp and logs all actions into log file
from datetime import datetime


def log_action(action):
    now = "[" + str(datetime.now()) + "] "
    with open("Log.txt", "a") as file:
        line = now + action + "\n"
        file.write(line)
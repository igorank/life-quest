#Point Reward Sytem
#new edit
def main():

    cont=True
    option=1

    while option!=8 and cont==True:

        #update any changes
        curPoints=get_myPoints()            #Points have already been dir updated in file, so retrieve from file again
        curTotal=get_TotalPoints()
        rewList=rewards_get()
        actList=activities_get()
        inv=inventory_get()
        
        default_display(curPoints,rewList,inv)
        print()
        print("-"*10+"MENU SELECTION"+"-"*10)
        option=menu()

        action="NIL"
        
        if option==1:
            DisplayActivities(actList)
            print()
            choice=input("What did you do? Select index: ")
            if choice.isalpha==True:        #method 1 for error-proofing
                gotError()
                main()
            elif int(choice)<1 or int(choice)>len(actList):
                gotError()
                main()
            do_activity(actList,int(choice))
            update_pointsFile(actList,"add",int(choice),curPoints, curTotal)
            action="Did activity: "+str(actList[int(choice)-1].Activity)+". +"+str(actList[int(choice)-1].Points)+" points!"

        elif option==2:
            choice=input("What would you like? Select index: ")
            result=choose_reward(rewList,curPoints,int(choice))
            if result=="success":       #method 2 for error-proofing
                update_pointsFile(rewList,"minus",int(choice),curPoints, curTotal)
                action="Received reward: "+str(rewList[int(choice)-1].Reward)+". -"+str(rewList[int(choice)-1].Points)+" points!"

        elif option==3:
            if len(inv)!=0:
                choice=input("Which did you use? Select index: ")
                if int(choice)<1 or int(choice)>len(inv):
                    gotError()
                    main()
                use_reward(inv,int(choice))
                action="Used reward: "+str(rewList[int(choice)-1].Reward)+"."
            else:
                print("You don't have any rewards!")

        elif option==4:
            DisplayActivities(actList)
            DisplayRewards(rewList)
            action="Displayed activities and rewards details."
        elif option==5:
            print("-"*10+"MY POINTS"+"-"*10)
            with open("PointRecord.txt") as file:
                for line in file:
                    line=line.strip()
                    print(line)
            action="Display points."

        elif option==6:
            DisplayActivities(actList)
            print()
            newAct=input("What new activity would you like to add? Type: ")
            newPoints=input("How many points would this gain? Type: ")
            add_activity(newAct,newPoints)
            actList=activities_get()    #so that actList updates to have the new activities
            action="Add activity: "+newAct+"."

        elif option==7:
            DisplayRewards(rewList)
            print()
            newRew=input("What new reward would you like to add? Type: ")
            newPoints=input("How many points would this require? Type: ")
            add_reward(newRew,newPoints)
            rewList=rewards_get()
            action="Add reward: "+newRew+"."


        #still within while loop, ask if want to continue
        if 1<=option<8:
            print()
            select=input("Would you like to continue? Type 'y' or 'n': ")
            if select=="n":
                cont=False

        elif option<1 or option>8:
            print("-"*10+"Update!"+"-"*10)
            print("Error! Option does not exist. Try again!")
            print("-"*27)
            main()

        print()
        log_action(action)

        update_activityFile(actList)    #activities/rewards only updated in their lists previously, so overwrite the files with the lists
        update_rewardFile(rewList)


    if option==8 or cont==False:
        action="Exit program."
        print("Bye bye~ See you again! :)")

    log_action(action)      #Log action to log file


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

#reads reward file and compile all reward objects in a list for easy updating
def rewards_get():
    
    with open("Rewards.txt","r") as rewFile:
        rewList=[]
        for i in range(2):
            rewFile.readline()
        for line in rewFile:
            line=line.strip()
            details=line.split("|")
            reward=Reward(details[0],int(details[1]),int(details[2]))
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

#display current points, reward list and number of points to reach reward, my reward inventory
def default_display(curPoints,rewList,inv):
    print("-"*10+"MY POINTS"+"-"*10)
    print("My current points:",curPoints)
    print("-"*10+"REWARDS LIST"+"-"*10)
    print("{:5}   {:20}{}".format("Index","Reward","How many more points needed?"))
    i=0
    for item in rewList:
        i+=1
        if curPoints>=item.Points:
            how="Get?"
        else:
            how=item.Points-curPoints
        print("{:5}   {:20}{}".format(i,item.Reward,how))

    print("-"*10+"MY REWARD INVENTORY"+"-"*10)
    i=0
    for item in inv:
        i+=1
        print(i," ",item)

def gotError():
    print("Input error >_< Retry!")
    print()
        
def menu():
    print("1. I did something!\n2. Choose reward\n3. Use reward\n4. Display Activity/Reward list\n5. Display points accumulated\n6. Add activity\n7. Add reward\n8. Exit")
    print()
    option=int(input("Select: "))
    return option

def DisplayActivities(actList):
    print("-"*10+"ACTIVITIES DETAILS"+"-"*10)
    print("{:5}   {:25}{:15} {}".format("Index","Activity","Points to gain","Count"))
    i=0
    for act in actList:
        i+=1
        print("{:5}   {:25}{:<15} {}".format(i,act.Activity,act.Points,act.Count))

def DisplayRewards(rewList):
    print("-"*10+"REWARDS DETAILS"+"-"*10)
    print("{:5}   {:20}{:15} {}".format("Index","Reward","Points required","Count"))
    i=0
    for rew in rewList:
        i+=1
        print("{:5}   {:20}{:<15} {}".format(i,rew.Reward,rew.Points,rew.Count))

#adds new activity to the activity file directly
def add_activity(activity,points):
    print("-"*10+"Update!"+"-"*10)
    with open("Activities.txt","a") as actFile:
        newAct=activity+"|"+str(points)+"|"+"0"+"\n"
        actFile.write(newAct)
    print("New activity has been added!")
    print("-"*27)

#adds new reward to the reward file directly
def add_reward(rew,points):
    print("-"*10+"Update!"+"-"*10)
    with open("Rewards.txt","a") as rewFile:
        newRew=rew+"|"+str(points)+"|"+"0"+"\n"
        rewFile.write(newRew)
    print("New reward has been added!")
    print("-"*27)

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

#log activity, add points, update count
def do_activity(actList,index):
    realIndex=index-1
    activity=actList[realIndex].Activity
    actList[realIndex].Count+=1
    
    pointsGain=actList[realIndex].Points
    print("-"*10+"Update!"+"-"*10)
    print("You have done this activity:",activity+"!")
    print("You will gain +"+str(pointsGain),"points!")
    print("-"*27)

#choosing rewards: select number, add to inventory, update count
def choose_reward(rewList,curPoints,index):
    realIndex=index-1
    print("-"*10+"Update!"+"-"*10)
    if index>len(rewList):
        print("Reward does not exist!")
        print("-"*27)
        return "fail"
    elif curPoints<rewList[realIndex].Points:
        print("Sorry! You don't have enough points.")
        print("-"*27)
        return "fail"
    else:
        reward=rewList[realIndex].Reward
        rewList[realIndex].Count+=1
        
        pointsUsed=rewList[realIndex].Points

        print("You have chosen this reward:",reward+"!")
        print("You will use up",pointsUsed,"points!")
        with open("RewardInventory.txt","a") as file:
            line=reward+"\n"
            file.write(line)
        print("-"*27)
        return "success"

#use up reward, delete from inventory
def use_reward(invList,num):
    used=invList.pop(num-1)
    print("-"*10+"Update!"+"-"*10)
    print("You have used up this reward: ",used+"!")
    print("-"*27)
    with open("RewardInventory.txt","w") as file:
        for item in invList:
            line=item+"\n"
            file.write(line)

#overwrites points file to save updated points
def update_pointsFile(thelist,step,index,prevPoints, prevTot):
    realIndex=index-1
    if step=="add":
        with open("PointRecord.txt","w") as file:
            curPoints=prevPoints+int(thelist[realIndex].Points)
            curPointsLine="My Current Points: "+str(curPoints)+"\n"
            file.write(curPointsLine)

            curTotal=prevTot+int(thelist[realIndex].Points)
            curTotalLine="My Accumulated Total Points: "+str(curTotal)
            file.write(curTotalLine)

    elif step=="minus":
        with open("PointRecord.txt","w") as file:
            curPoints=prevPoints-int(thelist[realIndex].Points)
            curPointsLine="My Current Points: "+str(curPoints)+"\n"
            file.write(curPointsLine)

            curTotalLine="My Accumulated Total Points: "+str(prevTot)
            file.write(curTotalLine)
            
#takes updated lists that store activity/reward objects and overwrites/saves in text file
def update_activityFile(actList):
    with open("Activities.txt","w") as file:
        header="Activity|Points|Count" + "\n"*2
        file.write(header)

        for activity in actList:
            line=activity.Activity+"|"+str(activity.Points)+"|"+str(activity.Count)+"\n"
            file.write(line)

def update_rewardFile(rewList):
    with open("Rewards.txt","w") as file:
        header="Reward|Points|Count" + "\n"*2
        file.write(header)

        for reward in rewList:
            line=reward.Reward+"|"+str(reward.Points)+"|"+str(reward.Count)+"\n"
            file.write(line)


#create timestamp and logs all actions into log file
from datetime import datetime
def log_action(action):
    now="["+str(datetime.now())+"] "
    with open("Log.txt","a") as file:
        line=now+action+"\n"
        file.write(line)


main()










                
        



    
        
        
    

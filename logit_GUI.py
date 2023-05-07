#LOGIT GUI
#random edit

from tkinter import *
root = Tk()

root.geometry("900x500")

    ## Import classes
from logitClasses import *


    ##Functions

#function to read activity note file and display onto displayFrame, in label

def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    #frame.pack_forget()

def DisplayActivities():

    clearFrame(scrollFrame)     #call function to clear the frame & hides it


    actList = activities_get()

    frame=ScrollableFrame(scrollFrame)      #Create object frame from the imported Class, within scrollable frame

    # Create labels within the frame of the scrollable frame
    titleLabel = Label(frame.scrollable_frame, text="-"*10+"ACTIVITIES DETAILS"+"-"*10)
    titleLabel.grid(row=0,column=0,columnspan=4,sticky=NSEW)

    heading1 = Label(frame.scrollable_frame, text="Index")
    heading2 = Label(frame.scrollable_frame, text= "Activity")
    heading3 = Label(frame.scrollable_frame, text= "Points to gain")
    heading4 = Label(frame.scrollable_frame, text= "Count")

    heading1.grid(row=1,column=0)
    heading2.grid(row=1, column=1)
    heading3.grid(row=1, column=2)
    heading4.grid(row=1, column=3)


    # For loop to create labels for each item (use grid system)
    i=1
    dispRow=2
    for act in actList:

        item1=Label(frame.scrollable_frame, text=i)
        item2= Label(frame.scrollable_frame, text=act.Activity)
        item3 = Label(frame.scrollable_frame, text=act.Points)
        item4 = Label(frame.scrollable_frame, text=act.Count)

        item1.grid(row=dispRow,column=0)
        item2.grid(row=dispRow,column=1)
        item3.grid(row=dispRow,column=2)
        item4.grid(row=dispRow,column=3)

        i+=1
        dispRow+=1

    frame.pack()        #REMEMBER TO PACK THE FRAME

def DisplayRewards():

    clearFrame(scrollFrame)  # call function to clear the frame & hides it

    rewList = rewards_get()

    frame = ScrollableFrame(scrollFrame)  # Create object frame from the imported Class, within scrollable frame

    # Create labels within the frame of the scrollable frame
    titleLabel = Label(frame.scrollable_frame, text="-"*10+"REWARDS DETAILS"+"-"*10)
    titleLabel.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    heading1 = Label(frame.scrollable_frame, text="Index")
    heading2 = Label(frame.scrollable_frame, text="Rewards")
    heading3 = Label(frame.scrollable_frame, text="Points required")
    heading4 = Label(frame.scrollable_frame, text="Count")

    heading1.grid(row=1, column=0)
    heading2.grid(row=1, column=1)
    heading3.grid(row=1, column=2)
    heading4.grid(row=1, column=3)

    # For loop to create labels for each item (use grid system)
    i = 1
    dispRow = 2
    for rew in rewList:
        item1 = Label(frame.scrollable_frame, text=i)
        item2 = Label(frame.scrollable_frame, text=rew.Reward)
        item3 = Label(frame.scrollable_frame, text=rew.Points)
        item4 = Label(frame.scrollable_frame, text=rew.Count)

        item1.grid(row=dispRow, column=0)
        item2.grid(row=dispRow, column=1)
        item3.grid(row=dispRow, column=2)
        item4.grid(row=dispRow, column=3)

        i += 1
        dispRow += 1

    frame.pack()  # REMEMBER TO PACK THE FRAME

def DisplayInventory():

    clearFrame(scrollFrame)  # call function to clear the frame & hides it

    inv = inventory_get()

    frame = ScrollableFrame(scrollFrame)  # Create object frame from the imported Class, within scrollable frame

    # Create labels within the frame of the scrollable frame
    titleLabel = Label(frame.scrollable_frame, text="-"*10+"INVENTORY"+"-"*10)
    titleLabel.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    i=1
    dispRow=1
    for item in inv:
        item1 = Label(frame.scrollable_frame, text = str(i)+".")
        item2 = Label(frame.scrollable_frame, text = item)

        item1.grid(row = dispRow, column = 0)
        item2.grid(row = dispRow, column = 1)

        i+=1
        dispRow+=1

    frame.pack()  # REMEMBER TO PACK THE FRAME

def displayPoints():
    clearFrame(displayFrame3)

    curPoints = get_myPoints()
    totPoints = get_TotalPoints()

    score = Label(displayFrame3, pady=5,
                  text="My Current Points: " + str(curPoints) + "\nMy Accumulated Total Points: " + str(totPoints))
    score.pack(side=LEFT)

def update(what, index):
    #index is already accurate to the list
    if what == "activity":
        #update count += 1
        actList = activities_get()
        actList[index].Count+=1
        update_activityFile(actList)

        #update points
        prevPoints = get_myPoints()
        prevTot = get_TotalPoints()
        update_pointsFile(actList, "add", index+1, prevPoints, prevTot)

        #log actName & points
        remark = remarkEntry.get()
        action="Did activity: "+str(actList[index].Activity)+". +"+str(actList[index].Points)+" points! Remarks: "+str(remark)+"."
        log_action(action)

        #display an update on screen
        remarkEntry.delete(0,END)
        updateDisplay = Label(mainFrame, padx=4, pady=4, text="Nice! Keep up the good work :D\n+"+str(actList[index].Points)+" points!")
        updateDisplay.grid(row=4, column=0, columnspan = 2)

        #update score on displayScreen
        displayPoints()

    elif what == "reward":
        rewList = rewards_get()
        curPoints = get_myPoints()

        if curPoints>=rewList[index].Points:
            # update count += 1
            rewList = rewards_get()
            rewList[index].Count += 1
            update_rewardFile(rewList)

            # update points
            prevPoints = get_myPoints()
            prevTot = get_TotalPoints()
            update_pointsFile(rewList, "minus", index + 1, prevPoints, prevTot)

            # update inventory list
            with open("RewardInventory.txt", "a") as file:
                line = rewList[index].Reward + "\n"
                file.write(line)

            # log actName & points
            action = "Received reward: "+str(rewList[index].Reward)+". -"+str(rewList[index].Points)+" points!"
            log_action(action)

            # display an update on screen
            clearFrame(mainFrame)
            updateDisplay = Label(mainFrame, padx=4, pady=4,
                                  text="You have received the reward: " + str(rewList[index].Reward) + "\n -"+str(rewList[index].Points)+"!")
            updateDisplay.grid(row=0, column=0)

            # update score on displayScreen
            displayPoints()
        else:
            #display on screen unsuccessful
            clearFrame(mainFrame)
            errorDisplay = Label(mainFrame, text = "You don't have enough points >_< \nTime to get productive!")
            errorDisplay.pack()

    elif what =="inventory":
        #update inventory text file
        invList = inventory_get()
        used = invList.pop(index)
        with open("RewardInventory.txt", "w") as file:
            for item in invList:
                line = item + "\n"
                file.write(line)

        # display update
        clearFrame(mainFrame)
        displayMsg = Label(mainFrame, text = "You have used: "+used+".")
        displayMsg.grid(row=0)

        clearFrame(bottomFrame)
        backButton = Button(bottomFrame, text="Go Back <<", command=default)
        backButton.grid(row=0, column=0, sticky=E)

        action = "Used reward: " + used + "."
        log_action(action)



def activityRemark(index):
    index-=1
    actList = activities_get()
    activity = actList[index].Activity

    clearFrame(mainFrame)
    mainLabel1 = Label(mainFrame, text = "Activity chosen: " + activity)
    mainLabel2 = Label(mainFrame, text = "Add comments/remarks:", anchor = E)

    #create global variable so can use remarkEntry in another function
    global remarkEntry
    remarkEntry = Entry(mainFrame)


    submit = Button(mainFrame, text = "Submit", command = lambda: update("activity", index))

    mainLabel1.grid(row=0, column=0, columnspan = 2, padx = 5, pady = 5)
    mainLabel2.grid(row=1, column=0, padx = 5, pady = 5)
    remarkEntry.grid(row=1, column=1, sticky = NSEW)
    submit.grid(row=3, column=0, columnspan = 2, padx = 5, pady = 5)




def default():
    clearFrame(bottomFrame)
    clearFrame(mainFrame)

    #mainFrame
    mainLabel = Label(mainFrame, padx=50, pady=50, text="Let's be productive today!\n\(≧▽≦)/")
    mainLabel.pack()

    #bottomFrame
    button1 = Button(bottomFrame, padx=3, pady=3, text="I did something!", command=selectAct)
    button2 = Button(bottomFrame, padx=3, pady=3, text="Choose reward", command=selectRew)
    button3 = Button(bottomFrame, padx=3, pady=3, text="Use reward", command=useRew)
    button4 = Button(bottomFrame, padx=3, pady=3, text="Add activity", command=addAct)
    button5 = Button(bottomFrame, padx=3, pady=3, text="Add reward", command=addRew)
    button6 = Button(bottomFrame, padx=3, pady=3, text="Display log", command=dispLog)
    button7 = Button(bottomFrame, padx=3, pady=3, text="Exit", command=closeWindow)

    button1.grid(row=0, column=0, sticky=NSEW)  # makes button fill up cell
    button2.grid(row=0, column=1, sticky=NSEW)
    button3.grid(row=0, column=2, sticky=NSEW)
    button4.grid(row=1, column=0, sticky=NSEW)
    button5.grid(row=1, column=1, sticky=NSEW)
    button6.grid(row=1, column=2, sticky=NSEW)
    button7.grid(row=1, column=3, sticky=NSEW)

def selectAct():
    clearFrame(bottomFrame)

    actList = activities_get()

    i = 1
    bRow = 0
    bCol = 0
    for item in actList:
        #by using lamda i=i, function looks for what the value i is at the time that the function is called
        b = Button(bottomFrame, text = str(i)+". "+ item.Activity, anchor = W, command = lambda i=i: activityRemark(i))
        b.grid(row = bRow, column = bCol, sticky = NSEW)

        if i%5==0:
            bRow+=1
            bCol=0
        else:
            bCol+=1
        i+=1

    backButton = Button(bottomFrame, text = "Go Back <<", command = default)
    backButton.grid(row = bRow, column = 4, sticky = E)

def confirmRew(index):
    index-=1
    clearFrame(mainFrame)

    rewList = rewards_get()
    reward = rewList[index].Reward

    rewardLabel = Label(mainFrame,  text = "Confirm receiving this reward?\n"+reward)
    pointLabel = Label(mainFrame, text = "-- Requires "+str(rewList[index].Points)+" points --")
    confirm = Button(mainFrame,  text = "Confirm", command = lambda: update("reward", index))

    rewardLabel.grid(row=0, column=0, padx=5, pady=5)
    pointLabel.grid(row=1, column=0, padx=5, pady=5)
    confirm.grid(row=2, column = 0,padx=5, pady=5)

def selectRew():
    clearFrame(bottomFrame)

    rewList = rewards_get()

    i = 1
    bRow = 0
    bCol = 0
    for item in rewList:
        #by using lamda i=i, function looks for what the value i is at the time that the function is called
        b = Button(bottomFrame, text = item.Reward, anchor = W, command = lambda i=i: confirmRew(i))
        b.grid(row = bRow, column = bCol, sticky = NSEW)

        if i%5==0:
            bRow+=1
            bCol=0
        else:
            bCol+=1
        i+=1

    backButton = Button(bottomFrame, text = "Go Back <<", command = default)
    backButton.grid(row = bRow, column = 4, sticky = E)

def confirmUse(index):
    index-=1
    clearFrame(mainFrame)

    invList = inventory_get()
    reward = invList[index]

    useRewardLabel = Label(mainFrame,  text = "-- Use reward: "+reward+" --")
    confirm = Button(mainFrame,  text = "Confirm", command = lambda: update("inventory", index))

    useRewardLabel.grid(row=0, column=0, padx=5, pady=5)
    confirm.grid(row=1, column = 0,padx=5, pady=5)

def useRew():
    clearFrame(bottomFrame)

    invList = inventory_get()
    i = 1
    bRow = 0
    bCol = 0
    for item in invList:
        #by using lamda i=i, function looks for what the value i is at the time that the function is called
        b = Button(bottomFrame, text = item, anchor = W, command = lambda i=i: confirmUse(i))
        b.grid(row = bRow, column = bCol, sticky = NSEW)

        if i%5==0:
            bRow+=1
            bCol=0
        else:
            bCol+=1
        i+=1

    backButton = Button(bottomFrame, text = "Go Back <<", command = default)
    backButton.grid(row = bRow, column = 4, sticky = E)

def confirmAdd(what):
    if what == "activity":

        # get entries before clearing the frame
        activity = entry1.get()
        points = entry2.get()

        default()
        clearFrame(mainFrame)

        label1 = Label(mainFrame, text = "You have added a new activity", pady=5)
        label2 = Label(mainFrame, text ="-- "+activity+" --", pady=5)
        label1.grid(row=1)
        label2.grid(row=2)

        # add activity to file
        with open("Activities.txt", "a") as actFile:
            newAct = activity + "|" + str(points) + "|" + "0" + "\n"
            actFile.write(newAct)

        action = "Add activity: " + newAct + "."

    elif what == "reward":

        # get entries before clearing the frame
        reward = entry3.get()
        points = entry4.get()

        default()
        clearFrame(mainFrame)

        label1 = Label(mainFrame, text = "You have added a new reward", pady=5)
        label2 = Label(mainFrame, text ="-- "+reward+" --", pady=5)
        label1.grid(row=1)
        label2.grid(row=2)

        # add activity to file
        with open("Rewards.txt", "a") as rewFile:
            newRew = reward + "|" + str(points) + "|" + "0" + "\n"
            rewFile.write(newRew)

        action = "Add activity: " + newRew + "."

    log_action(action)

def addAct():
    #allow entries to be accessed in other functions
    global entry1
    global entry2

    clearFrame(mainFrame)
    label1 = Label(mainFrame, text = "New activity name:", padx=4, pady=4)
    entry1 = Entry(mainFrame)
    label2 = Label(mainFrame, text="New activity points:", padx=4, pady=4)
    entry2 = Entry(mainFrame)

    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1, column=1)

    submit = Button(mainFrame, text = "Submit", command = lambda: confirmAdd("activity"))
    submit.grid(row=2, columnspan = 2, padx=5, pady=5)


def addRew():
    # allow entries to be accessed in other functions
    global entry3
    global entry4

    clearFrame(mainFrame)
    label1 = Label(mainFrame, text="New reward name:", padx=4, pady=4)
    entry3 = Entry(mainFrame)
    label2 = Label(mainFrame, text="New reward points:", padx=4, pady=4)
    entry4 = Entry(mainFrame)

    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    entry3.grid(row=0, column=1)
    entry4.grid(row=1, column=1)

    submit = Button(mainFrame, text="Submit", command=lambda: confirmAdd("reward"))
    submit.grid(row=2, columnspan=2, padx=5, pady=5)


def dispLog():
    clearFrame(mainFrame)
    mainLabel = Label(mainFrame, text = "--- TODAY's LOG ---")
    mainLabel.grid(row=0)
    todayDate = datetime.now().date()
    
    therow=1
    # for loop log file and if date == today, print line
    with open("Log.txt") as logFile:
        for line in logFile:
            line=line.strip()
            logdate = line.split()[0][1:]
            
            if str(logdate) == str(todayDate):      #string both variables,bcuz todayDate might not be in string format
                displayLabel = Label(mainFrame, text = line, pady=4)
                displayLabel.grid(row=therow, sticky = W)

            therow+=1

def closeWindow():
    root.destroy()      #closes window
    action = "Exit."
    log_action(action)

    ##Layout## !! Positioning packing before/after MATTERS

topFrame = Frame(root)
topFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)

mainFrame = Frame(topFrame)
mainFrame.pack(side = LEFT)

displayFrameMAIN = Frame(topFrame)
displayFrameMAIN.pack(side = RIGHT,fill=BOTH, expand=True)

displayFrame1 = Frame(displayFrameMAIN)
displayFrame2 = Frame(displayFrameMAIN)
displayFrame3 = Frame(displayFrameMAIN)

displayFrame1.pack(side=TOP, anchor=NW)
displayFrame2.pack(side=TOP)

#Making scroll frame for scrolling list
from ScrollableFrame import ScrollableFrame  # import the class (found online)
scrollFrame = Frame(displayFrameMAIN)  # create the frame to be scrolled within a main frame
scrollFrame.pack(side=TOP, anchor=NE)  # remember to PACK frame

displayFrame3.pack(side=BOTTOM, anchor=NW)


    ##Top frame##

mainLabel = Label(mainFrame, padx=50,pady=50, text ="Let's be productive today!\n\(≧▽≦)/")
mainLabel.pack()


    ##Display frame##

curPoints = get_myPoints()
totPoints = get_TotalPoints()

score = Label(displayFrame3, pady=5, text="My Current Points: "+str(curPoints)+"\nMy Accumulated Total Points: "+str(totPoints))
score.pack(side=LEFT)


#Creating list bar
listBar = Frame(displayFrame1)

    #Create buttons and put into list bar
actDisp = Button(listBar, text = "Activity list", command = DisplayActivities)   #add commands
rewDisp = Button(listBar, text = "Reward list", command = DisplayRewards)
invDisp = Button(listBar, text = "Inventory list", command = DisplayInventory)

    #Pack buttons
actDisp.pack(side=LEFT, padx=2, pady=2)
rewDisp.pack(side=LEFT, padx=2, pady=2)
invDisp.pack(side=LEFT, padx=2, pady=2)

    #Pack the list bar
listBar.pack(side=TOP,anchor=NW)

    ##Bottom frame##

button1 = Button(bottomFrame, padx=3,pady=3,text="I did something!", command = selectAct)
button2 = Button(bottomFrame, padx=3,pady=3,text="Choose reward", command = selectRew)
button3 = Button(bottomFrame, padx=3,pady=3,text="Use reward", command = useRew)
button4 = Button(bottomFrame, padx=3,pady=3,text="Add activity", command = addAct)
button5 = Button(bottomFrame, padx=3,pady=3,text="Add reward", command = addRew)
button6 = Button(bottomFrame, padx=3,pady=3,text="Display log", command = dispLog)
button7 = Button(bottomFrame, padx=3,pady=3,text="Exit", command = closeWindow)

button1.grid(row=0,column=0,sticky=NSEW)    #makes button fill up cell
button2.grid(row=0,column=1,sticky=NSEW)
button3.grid(row=0,column=2,sticky=NSEW)
button4.grid(row=1,column=0,sticky=NSEW)
button5.grid(row=1,column=1,sticky=NSEW)
button6.grid(row=1,column=2,sticky=NSEW)
button7.grid(row=1,column=3,sticky=NSEW)


root.mainloop()






















#!/usr/bin/env python
# coding: utf-8

# # HSG Alarm Clock - Never be late again!

# ## About the Project
# 
# The program consists of a customized alarm clock integrated with the city bus schedule, which helps HSG students to never run late for university again, saving them from the struggles of missing the bus and having to walk up the hill. Most students who live in the city center of St. Gallen need to either walk to university or take the bus number 5 or 9 from the train station. Due to convenience, bus number 9 is favoured by most of the students as it stops right next to the university. Therefore, our alarm clock works with the bus number 9 schedule. Moreover, for simplicity, we have designed the alarm for departure from the St. Gallen train station only, as most students take the bus from there to arrive at the university. 
# 
# The program offers students a special alarm setting system by providing the following features: First, the user is asked to tick a box if he/she wants to go to university. If the user does not tick the box then the time he/she sets is the time of the alarm. Here, the program is used as a regular alarm clock. If the user needs to go to uni, they have to input the time they need to be at university. Furthermore, the user is asked how long he/she needs to get ready by inputting the necessary hours/minutes. This includes breakfast, morning routines, time for the travel to the bus station, etc. The program compares the arrival times of the bus number 9 at the university (departing from the train station) to the indicated preferred arrival time of the user at university and selects the bus, which has the closest timely arrival. According to the bus schedule, the bus needs six minutes to get from the train station to the university. The departure time of the student from the train station is calculated by deducting 6 minutes from the arrival time of Bus 9 at uni. From this bus departure time, the program deducts the time that it takes the user to get ready and be at the bus station. The output is the time when the alarm rings. Additionally, the program allows the user to customize the alarm ringing tone by inputting an URL (e.g. Youtube Link).

# ### Import necessary libraries

# In[1]:


# Import necessary libraries
from datetime import datetime
import time
import webbrowser

# libraries needed for the interface
from tkinter import *  
from tkinter import ttk 
from tkinter.ttk import *  


# ### Greet the User

# In[2]:


# Greet the user depending on the time of the day
currentTime = datetime.now()
currentTime.hour

if currentTime.hour < 12:
    print('Good morning! Bom dia! Guten Morgen! Buenos Dias! Bonjour! 早上好!')
elif 12 <= currentTime.hour < 18:
    print('Good afternoon! Boa tarde! Guten Nachmittag! Buenas tardes! Bonjour! 下午好!')
else:
    print('Good evening! Boa noite! Guten Abend! Buenas noches! Bon soir! 晚上好!')


# ### Define main function

# In[3]:


def setalarm():     
    # Assign variables and get data from the interface
    url = t.get("1.0", END)
    university = var.get()
    arrivingtime = "%s:%s"%(combobox_h.get(),combobox_m.get()) 
    current_time = datetime.strftime(datetime.now(),"%H:%M:%S")
    
    # format used throughout the exercise HH:MM
    format = '%H:%M'    
    
    # Option 1: User goes to university (box checked)
    if university == 1: 
        # Convert arriving time to the right format form string
        arriving_time_format = datetime.strptime(arrivingtime, format) 
        # Bus schedule of Bus 9 from the St. Gallen train station to University (arrival time at university)
        bus_arriving_schedule = ['00:03', '00:48', '05:39', '05:53', '06:03', '06:13', '06:23', '06:39', '06:43', '06:53', '07:03', '07:13', '07:23', '07:39', '07:43', '07:53', '08:03', '08:13', '08:23', '08:39', '08:43', '08:53', '09:03', '09:23', '09:43', '10:03', '10:23', '10:43', '11:03', '11:23', '11:43', '11:53', '12:03', '13:13', '13:23', '13:39', '13:43', '13:53', '14:03', '14:23', '14:43', '15:03', '15:23', '15:43', '16:03', '16:23', '16:43', '16:53', '17:03', '17:13', '17:23', '17:39', '17:43', '17:53', '18:03', '18:13', '18:23', '18:39', '18:43', '18:53', '19:03', '19:13', '19:23', '19:39', '19:43', '19:53', '20:23', '20:43', '21:03', '21:23', '21:43', '22:03', '22:23', '22:43', '23:03', '23:23', '23:43']               
        # Duration the bus takes from the St. Gallen train station to university
        bus_length = '00:06'
        # Create new list that includes all buses that arrive on time at the university
        goodbuslist=[]  
        for i in range(len(bus_arriving_schedule)):
            # Convert bus arrival times to right format for comparison purposes
            bus_arriving_time = datetime.strptime(bus_arriving_schedule[i], format)  
            # Append all buses that arrive prior to the designated time at uni to the list
            if bus_arriving_time <= arriving_time_format:
                goodbuslist.append(bus_arriving_schedule[i])
        # The bus with the maximum time in the list is chosen as the best option (i.e the latest bus that arrives in time before your planned arrival time)
        bestbus = max(goodbuslist) 
        # To calculate the departure time of the bus from the train station, we deduct 6 minutes from the arrival time of the bus at uni, which is the time it takes the bus to get to uni from the train station.
        bus_to_take = datetime.strptime(bestbus, format) - datetime.strptime(bus_length, format)
        bus_to_take_short = str(bus_to_take)[:5]
 
        # Get data from the interface: Time (hours and minutes) the user needs to get ready for departure.
        diff = "%s:%s"%(combobox_ready_h.get(),combobox_ready_m.get()) 
        # Determines the alarm time by deducting the time needed to get ready from the departure of the last timelybus
        alarmtime = datetime.strptime(bus_to_take_short, format) - datetime.strptime(diff, format)  
        alarmtime=str(alarmtime) 
        
        # Close interface
        master.destroy()
        
        # Print times
        print('\033[1;32;40m The latest bus to arrive on time leaves the St. Gallen Bahnhof at', bus_to_take_short)
        print("\033[1;32;40m Alarm has been set to %s to arrive on time to catch the bus!"%(alarmtime)) 
        # Freezes the function for 5 seconds so the user has a chance to read output
        time.sleep(5)   
        
        # Create infinite loop until condition is met
        while True: 
            # Freezes the function for a second so the same thing is not repeated multiple times in one second, only once
            time.sleep(1)   
            #current time in main format used for comparison with alarmtime
            current_time = datetime.strftime(datetime.now(),format)
            #current time including seconds for display in the terminal
            current_time_display = datetime.strftime(datetime.now(),"%H:%M:%S") 
            print("\033[1;32;40m Current time is %s. Do not worry, I will remind you to get ready at %s. The latest bus leaves the St. Gallen Bahnhof at %s."%(current_time_display,alarmtime,bus_to_take_short))
            
            # Condition: check if alarm is equal to the current time
            if current_time == alarmtime:
                print("\033[1;32;40m It is time to get going!") 
                # Plays alarm ring tone by opening the link/url (if you have a Macbook make sure safari is your default browser to immediately trigger the music being played)
                webbrowser.open(url) 
                break
                
                
    # Option 2: User does not go to university
    elif university == 0: 
        # Close interface
        master.destroy()    
        print("\033[1;32;40m Alarm has been set to %s!"%(arrivingtime)) 
        # Converts arriving time to string
        arrivingtime=str(arrivingtime)  
        # Freezes the function for 5 seconds so user has a chance to read output
        time.sleep(5)           
        
        while True:             
            # Freezes the function for a second so the same thing is not repeated multiple times in one second, only once
            time.sleep(1)   
            current_time = datetime.strftime(datetime.now(), format) 
            current_time_display = datetime.strftime(datetime.now(),"%H:%M:%S")
            print("\033[1;32;40m Current time is %s. Do not worry, I will wake you up at %s"%(current_time_display,arrivingtime)) 
            # Condition: check if alarm is equal to the current time
            if current_time == arrivingtime: 
                print("\033[1;32;40m It is time to wake up!")
                webbrowser.open(url)
                break


# ###  Create interface window

# In[4]:


# Create object
master = Tk()  

# Set geometry
master.geometry("450x450") 

# Add current time to the interface
now_string = time.strftime('%H:%M') 

# Add labels, frame, button and option menus
# Labels
label_2 = Label(master, text = now_string)  
label_2.pack(side = TOP, pady = 10) 
label_5 = Label(master, text ="Arrival time to uni / Wake up time if stay at home")
label_5.pack(side = TOP)

# Set hour of the alarm/arrival time at uni
combobox_h = StringVar(master) 
combobox_h.set("HH")
h = ttk.Combobox(master, textvariable=combobox_h, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
h.pack()

# Set minute of the alarm/arrival time at uni
combobox_m = StringVar(master)  
combobox_m.set("MM") 
m = ttk.Combobox(master, textvariable=combobox_m, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])    
m.pack()

# Checkbox feature - University Yes or No
var = IntVar()  
check = Checkbutton(master, text = "Going to University", variable=var) 
check.pack(pady = 10)   

# Label
label_3 = Label(master, text ="IF you go to uni, set time necessary to go get ready and go to bus stop") 
label_3.pack(side = TOP)    

# Set hour the user needs to get ready
combobox_ready_h = StringVar(master)    
combobox_ready_h.set("HH") 
ready_h = ttk.Combobox(master, textvariable=combobox_ready_h, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])   
ready_h.pack()

# Set minutes the user needs to get ready
combobox_ready_m = StringVar(master)    
combobox_ready_m.set("MM") 
ready_m = ttk.Combobox(master, textvariable=combobox_ready_m, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
ready_m.pack()

# Set Alarm button
btn = Button(master, text ="Set alarm", command=setalarm) 
btn.pack(pady = 10) 
options_h = StringVar(master)

# Input of url for the alarm ringtone
label_4 = Label(master, text ="Paste the URL of your favorite song")     
label_4.pack(pady = 10) #position of label_4
t = Text(master, height=1, width=30)
# Default song, to be used in case the user does not provide any preference for the ringtone of the alarm
t.insert(END,"https://www.youtube.com/watch?v=1y6smkh6c-0&list=RDGMEMYH9CUrFO7CfLJpaD7UR85wVMfoE1mO2yM04&index=10") 
t.pack()

mainloop()


# In[ ]:





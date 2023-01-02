#################################################################
# CS - 499 Team 3                                               #
#                                                               #
# Written By: Trebor Bearden and Kali Mcintire                  #
#                                                               #
# Utility File for writting to database based on utility usage. #
#################################################################
import psycopg2 as p


#Temperature Controls
def Update_Temperature(threshold, inside, outside, time):
    '''
    This function write to the database for Front Door Open
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into temperatures (threshold,inside,outside,time) VALUES(%s, %s, %s, %s)",(threshold,inside,outside,time))
    con.commit()
    cur.close()
    con.close()


'''

BEGIN POWER UTILITIES
combinations are initially placed here
then the water sections are in "POWER+WATER UTILITIES"

'''

def Front_Door_Open(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Front Door Open
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()
    

# Front_Door_Open(1,1,'open','2022-01-01 09:29:02')

def Front_Door_Close(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Front Door Close
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Back_Door_Open(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Back Door Open
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Back_Door_Close(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Back Door Close
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_To_House_Open(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Garage to House Door Open
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_To_House_Close(Door_Window_Event_ID, Door_Window_ID, Door_Window_Event, Event_Time):
    '''
    This function write to the database for Garage to House Door Close
    Params:
        Door_Window_Event_ID: (Primary Key) Unique ID for event
        Door_Window_Id: Unique ID for Door or Window
        Door_Window_Event: States what is happening at event (Door or Window either 'Opened' or 'Closed')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into store_window_usage (Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Door_Window_Event_ID,Door_Window_ID,Door_Window_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Microwave_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Microwave On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Microwave_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Microwave Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Stove_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Stove On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Stove_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Stove Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Oven_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Oven On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Oven_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Oven off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Tv_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room TV On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Tv_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room TV Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_Tv_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom TV On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_Tv_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom TV Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Dish_Washer_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Dish Washer On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Dish_Washer_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Dish washer off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Clothes_Washer_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Clothes Washer On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Clothes_Washer_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Clothes Washer Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Clothes_Dryer_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Clothes Dryer On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Clothes_Dryer_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Clothes Dryer Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Lamp_1_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Lamp 1 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Lamp_1_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Lamp 1 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Lamp_2_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Lamp 2 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Master_Bedroom_Lamp_2_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Master Bedroom Lamp 2 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Lamp_1_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Lamp 1 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Lamp_1_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Lamp 1 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Lamp_2_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Lamp 2 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_2_Lamp_2_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 2 Lamp 2 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Lamp_1_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Lamp 1 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Lamp_1_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Lamp 1 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Lamp_2_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Lamp 2 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bedroom_3_Lamp_2_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bedroom 3 Lamp 2 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_Door_1_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Garage Door 1 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_Door_1_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Garage Door 1 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_Door_2_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Garage Door 2 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Garage_Door_2_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Garage Door 2 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Lamp_1_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Lamp 1 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Lamp_1_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Lamp 1 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Lamp_2_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Lamp 2 On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Living_Room_Lamp_2_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Living Room Lamp 2 Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Kitchen_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Kitchen Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Kitchen_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Kitchen Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Refridgerator_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Refridgerator On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Refridgerator_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Refridgerator Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def HVAC_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for HVAC On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def HVAC_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for HVAC Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_1_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 1 Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_1_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 1 Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_2_Overhead_Light_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 2 Overhead Light On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_2_Overhead_Light_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 2 Overhead Light Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_1_Exhaust_Fan_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 1 Exhaust Fan On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_1_Exhaust_Fan_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 1 Exhaust Fan Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_2_Exhaust_Fan_On(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 2 Exhaust Fan On
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

def Bathroom_2_Exhaust_Fan_Off(Power_Event_ID, Utility_ID, Utility_Event, Event_Time):
    '''
    This function write to the database for Bathroom 2 Exhaust Fan Off
    Params:
        Power_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Utlity either 'On' or 'Off')
        Event_Time: Time Stamp for the precise time an event occurs
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into power_usage (Power_Event_ID,Utility_ID,Utility_Event,Event_Time) VALUES(%s, %s, %s, %s)",(Power_Event_ID,Utility_ID,Utility_Event,Event_Time))
    con.commit()
    cur.close()
    con.close()

'''

BEGIN WATER UTILITIES

'''

def Bathroom_1_Shower(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Bathroom 1 Shower water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Bathhroom_2_Shower(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Bathroom 2 Shower water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Bath(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Bath water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Bathroom_1_Sink(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Bathroom 1 Sink water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Bathroom_2_Sink(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Bathroom 2 Sink water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Kitchen_Sink(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Kitchen Sink water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Outside_Faucet(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Outside Faucet water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()
'''

BEGIN POWER+WATER UTILITIES

'''

def Dish_Washer_Water(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Dish washer water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Bath, Shower, Sink)
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

def Clothes_Washer_Water(Water_Event_ID, Utility_ID, Utility_Event, Gallons, Date):
    '''
    This function write to the database for Clothes washer water
    Params:
        Water_Event_ID: (Primary Key) Unique ID for event
        Utility_Id: Unique ID for utility
        Utility Event: State what is happening at the event (Bath, Shower, Sink)
        Gallons: Amount of water used during event
        Date: The day the event occurred
    Returns:
        Nothing writes to database.
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Insert into water_usage (Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date) VALUES(%s, %s, %s, %s, %s)",(Water_Event_ID,Utility_ID,Utility_Event,Gallons,Date))
    con.commit()
    cur.close()
    con.close()

# Garage_To_House_Open(7586, 3, "open", "2022-11-07 011:10:54")
# Garage_To_House_Close(7587, 3, "close", "2022-11-07 011:12:54")
# Microwave_Off(2, 22, 'Off', "2022-10-27 9:51:53")

# Master_Bedroom_Overhead_Light_On(2477,1,'on',"2022-11-07 12:51:23")
# Master_Bedroom_Overhead_Light_Off(2478,1,'off',"2022-11-07 13:51:23")
# Bedroom_2_Overhead_Light_On(2491,2,'on',"2022-11-07 16:45:23")
# Bedroom_2_Overhead_Light_Off(2480,2,'off',"2022-11-07 15:51:23")
# Bedroom_3_Overhead_Light_On(2481,3,'on',"2022-11-07 16:51:23")
# Bedroom_3_Overhead_Light_Off(2482,3,'off',"2022-11-07 17:51:23")
# Living_Room_Overhead_Light_On(2494,15,'on',"2022-11-07 21:58:23")
# Living_Room_Overhead_Light_Off(2493,15,'off',"2022-11-07 19:52:23")
# Kitchen_Overhead_Light_On(2485,19,'on',"2022-11-07 20:51:23")
# Kitchen_Overhead_Light_Off(2486,19,'off',"2022-11-07 21:51:23")
# Bathroom_1_Overhead_Light_On(2487,32,'on',"2022-11-07 22:51:23")
# Bathroom_1_Overhead_Light_Off(2488,32,'off',"2022-11-07 23:51:23")
# Bathroom_2_Overhead_Light_On(2489,33,'on',"2022-11-07 02:51:23")
# Bathroom_2_Overhead_Light_Off(2490,33,'off',"2022-11-07 03:51:23")

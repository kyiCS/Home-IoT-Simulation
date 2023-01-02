#################################################################
# CS - 499 Team 3                                               #
#                                                               #
# Written By: Trebor Bearden and Kali Mcintire                  #
#                                                               #
# Python script to generate historical data                     #
#################################################################
import Event_Utils
from random import *
from datetime import *
from dateutil.relativedelta import *
from randomtimestamp import *
import GetState

def Week_Day(Event,WaterEvent,DoorWindowEvent,Date):
    '''
    This function generates random on and off events for doors, windows, water and power utilitities
    on a regular weekday.
    Params:
        Event: The Unique ID for power events
        WaterEvent: The unique ID for water events
        DoorWindowevent: The unique ID for door window events
        Date: The specific date.
    Returns:
        Event: The Unique ID for power events
        WaterEvent: The unique ID for water events
        DoorWindowevent: The unique ID for door window events
    '''

    for x in range(16):

        randomDoor = randrange(1,4)
        if randomDoor == 1:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Front_Door_Open(DoorWindowEvent,1,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Front_Door_Close(DoorWindowEvent,1,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

        if randomDoor == 2:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Back_Door_Open(DoorWindowEvent,2,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Back_Door_Close(DoorWindowEvent,2,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

        if randomDoor == 3:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Garage_To_House_Open_Door_Open(DoorWindowEvent,3,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Garage_To_House_Close_Door_Close(DoorWindowEvent,3,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Microwave_On(Event,22,'on',Time)
    Event += 1
    time_change = timedelta(minutes=20)
    Time = Time + time_change
    Event_Utils.Microwave_Off(Event,22,'off',Time) # Check
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Stove_On(Event,20,'on',Time)
    Event += 1
    time_change = timedelta(minutes=15)
    Time = Time + time_change
    Event_Utils.Stove_Off(Event,20,'off',Time) # Check
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Oven_On(Event,21,'on',Time)
    Event += 1
    time_change = timedelta(minutes=45)
    Time = Time + time_change
    Event_Utils.Oven_Off(Event,21,'off',Time) # Check
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Living_Room_Tv_On(Event,18,'on',Time)
    Event += 1
    time_change = timedelta(hours=4)
    Time = Time + time_change
    Event_Utils.Living_Room_Tv_Off(Event,18,'off',Time) # Check hours
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Bedroom_Tv_On(Event,10,'on',Time)
    Event += 1
    time_change = timedelta(hours=2)
    Time = Time + time_change
    Event_Utils.Bedroom_Tv_Off(Event,10,'off',Time) # Check hours
    Event += 1

    print(str(Date))
    Event_Utils.Shower(WaterEvent,29,'shower',25,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Shower(WaterEvent,29,'shower',25,Date) # Gallons
    WaterEvent += 1

    Event_Utils.Bath(WaterEvent,29,'shower',30,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Bath(WaterEvent,29,'shower',30,Date) # Gallons
    WaterEvent += 1

    return(DoorWindowEvent,Event,WaterEvent)

def Week_End(Event,WaterEvent,DoorWindowEvent,Date):
    '''
    This function generates random on and off events for doors, windows, water and power utilitities
    on a regular weekend.
    Params:
        Event: The Unique ID for power events
        WaterEvent: The unique ID for water events
        DoorWindowevent: The unique ID for door window events
        Date: The specific date.
    Returns:
        Event: The Unique ID for power events
        WaterEvent: The unique ID for water events
        DoorWindowevent: The unique ID for door window events
    '''

    for x in range(32):

        randomDoor = randrange(1,4)
        if randomDoor == 1:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Front_Door_Open(DoorWindowEvent,1,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Front_Door_Close(DoorWindowEvent,1,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

        if randomDoor == 2:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Back_Door_Open(DoorWindowEvent,2,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Back_Door_Close(DoorWindowEvent,2,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

        if randomDoor == 3:
            Time = datetime.combine(Date,random_time())
            Event_Utils.Garage_To_House_Open_Door_Open(DoorWindowEvent,3,'open',Time)
            DoorWindowEvent += 1
            time_change = timedelta(minutes=30)
            Time = Time + time_change
            Event_Utils.Garage_To_House_Close_Door_Close(DoorWindowEvent,3,'close',Time) # Check on time+ 30 minutes syntax
            DoorWindowEvent += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Microwave_On(Event,22,'on',Time)
    Event += 1
    time_change = timedelta(minutes=30)
    Time = Time + time_change
    Event_Utils.Microwave_Off(Event,22,'off',Time) # Check
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Stove_On(Event,20,'on',Time)
    Event += 1
    time_change = timedelta(minutes=30)
    Time = Time + time_change
    Event_Utils.Stove_Off(Event,20,'off',Time) # Check
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Oven_On(Event,21,'on',Time)
    Event += 1
    time_change = timedelta(hours=1)
    Time = Time + time_change
    Event_Utils.Oven_Off(Event,21,'off',Time) # Check minutes or hour??
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Living_Room_Tv_On(Event,18,'on',Time)
    Event += 1
    time_change = timedelta(hours=8)
    Time = Time + time_change
    Event_Utils.Living_Room_Tv_Off(Event,18,'off',Time) # Check hours
    Event += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Bedroom_Tv_On(Event,10,'on',Time)
    Event += 1
    time_change = timedelta(hours=4)
    Time = Time + time_change
    Event_Utils.Bedroom_Tv_Off(Event,10,'off',Time) # Check hours
    Event += 1

    Event_Utils.Shower(WaterEvent,29,'shower',25,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Shower(WaterEvent,29,'shower',25,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Shower(WaterEvent,29,'shower',25,Date) # Gallons
    WaterEvent += 1

    Event_Utils.Bath(WaterEvent,29,'shower',30,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Bath(WaterEvent,29,'shower',30,Date) # Gallons
    WaterEvent += 1
    Event_Utils.Bath(WaterEvent,29,'shower',30,Date) # Gallons
    WaterEvent += 1

    return(DoorWindowEvent,Event,WaterEvent)

def Weekly_Event(Event,WaterEvent,Date):

    Time = datetime.combine(Date,random_time())
    Event_Utils.Dish_Washer_On(Event,24,'on',Time)
    Event += 1
    time_change = timedelta(minutes=45)
    Time = Time + time_change
    Event_Utils.Dish_Washer_Off(Event,24,'off',Time)
    Event += 1
    Event_Utils.Dish_Washer_Water(WaterEvent,24,'dishwasher',6,Date)
    WaterEvent += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Clothes_Washer_On(Event,13,'on',Time)
    Event += 1
    time_change = timedelta(minutes=30)
    Time = Time + time_change
    Event_Utils.Clothes_Washer_Off(Event,13,'off',Time)
    Event += 1
    Event_Utils.Clothes_Washer_Water(WaterEvent,13,'clotheswasher',20,Date)
    WaterEvent += 1

    Time = datetime.combine(Date,random_time())
    Event_Utils.Clothes_Dryer_On(Event,14,'on',Time)
    Event += 1
    time_change = timedelta(minutes=30)
    Time = Time + time_change
    Event_Utils.Clothes_Dryer_Off(Event,14,'off',Time)
    Event += 1

    return(Event,WaterEvent)

def Weekly():
    '''
    This function generates random on and off events for doors, windows, water and power utilitities
    on a regular week.
    Params:
        None
    Returns:
        None
    '''
    today = date.today();
    Date = today - relativedelta(months=6)

    Event = 1
    WaterEvent = 1
    DoorWindowEvent = 1

    while (Date != today):
        if (Date.weekday() <= 4):
            DoorWindowEvent,Event,WaterEvent = Week_Day(Event,WaterEvent,DoorWindowEvent,Date)
            if (Date.weekday() == 0 or Date.weekday() == 2 or Date.weekday() == 4):
                Event,WaterEvent = Weekly_Event(Event,WaterEvent,Date)
        elif (Date.weekday() > 4 and Date.weekday() <=6):
            DoorWindowEvent,Event,WaterEvent = Week_End(Event,WaterEvent,DoorWindowEvent,Date)
            if (Date.weekday() == 6):
                Event,WaterEvent = Weekly_Event(Event,WaterEvent,Date)

        Date += timedelta(days=1)
        print(Date)

# Weekly()

# Just to have states -- add doors / overheads for floor plan
# def now():
#     id = GetState.Get_Recent_ID() + 1
    # Event_Utils.Master_Bedroom_Lamp_1_On(id,4,'on','2022-11-22 19:58:54')
    # id += 1
    # Event_Utils.Master_Bedroom_Lamp_1_Off(id,4,'off','2022-11-22 19:59:54')
    # id += 1
    # Event_Utils.Master_Bedroom_Lamp_2_On(id,5,'on','2022-11-22 20:00:54')
    # id += 1
    # Event_Utils.Master_Bedroom_Lamp_2_Off(id,5,'off','2022-11-22 20:01:54')
    # id += 1
    # Event_Utils.Bedroom_2_Lamp_1_On(id,6,'on','2022-11-22 20:02:54')
    # id += 1
    # Event_Utils.Bedroom_2_Lamp_1_Off(id,6,'off','2022-11-22 20:03:54')
    # id += 1
    # Event_Utils.Bedroom_2_Lamp_2_On(id,7,'on','2022-11-22 20:04:54')
    # id += 1
    # Event_Utils.Bedroom_2_Lamp_2_Off(id,7,'off','2022-11-22 20:05:54')
    # id += 1
    # Event_Utils.Bedroom_3_Lamp_1_On(id,8,'on','2022-11-22 20:06:54')
    # id += 1
    # Event_Utils.Bedroom_3_Lamp_1_Off(id,8,'off','2022-11-22 20:07:54')
    # id += 1
    # Event_Utils.Bedroom_3_Lamp_2_On(id,9,'on','2022-11-22 20:08:54')
    # id += 1
    # Event_Utils.Bedroom_3_Lamp_2_Off(id,9,'off','2022-11-22 20:09:54')
    # id += 1
    # Event_Utils.Bathroom_1_Exhaust_Fan_On(id,34,'on','2022-11-22 20:10:54')
    # id += 1
    # Event_Utils.Bathroom_1_Exhaust_Fan_Off(id,34,'off','2022-11-22 20:11:54')
    # id += 1
    # Event_Utils.Bathroom_2_Exhaust_Fan_On(id,35,'on','2022-11-22 20:12:54')
    # id += 1
    # Event_Utils.Bathroom_2_Exhaust_Fan_Off(id,35,'off','2022-11-22 20:13:54')
    # id += 1
    # Event_Utils.Garage_Door_1_On(id,11,'on','2022-11-22 20:14:54')
    # id += 1
    # Event_Utils.Garage_Door_1_Off(id,11,'off','2022-11-22 20:15:54')
    # id += 1
    # Event_Utils.Garage_Door_2_On(id,12,'on','2022-11-22 20:16:54')
    # id += 1
    # Event_Utils.Garage_Door_2_Off(id,12,'off','2022-11-22 20:17:54')
    # id += 1
    # Event_Utils.Living_Room_Lamp_1_On(id,16,'on','2022-11-22 20:18:54')
    # id += 1
    # Event_Utils.Living_Room_Lamp_1_Off(id,16,'off','2022-11-22 20:19:54')
    # id += 1
    # Event_Utils.Living_Room_Lamp_2_On(id,17,'on','2022-11-22 20:20:54')
    # id += 1
    # Event_Utils.Living_Room_Lamp_2_Off(id,17,'off','2022-11-22 20:21:54')
    # id += 1
    # Event_Utils.HVAC_On(id,25,'on','2022-11-22 20:22:54')
    # id += 1
    # Event_Utils.HVAC_Off(id,25,'off','2022-11-22 20:23:54')
    # id += 1
    # Event_Utils.Stove_On(id,20,'on','2022-11-22 20:24:54')
    # id += 1
    # Event_Utils.Stove_Off(id,20,'off','2022-11-22 20:25:54')
    # id += 1
    # Event_Utils.Oven_On(id,21,'on','2022-11-22 20:26:54')
    # id += 1
    # Event_Utils.Oven_Off(id,21,'off','2022-11-22 20:27:54')
    # id += 1
    # Event_Utils.Microwave_On(id,22,'on','2022-11-22 20:28:54')
    # id += 1
    # Event_Utils.Microwave_Off(id,22,'off','2022-11-22 20:29:54')

# now()

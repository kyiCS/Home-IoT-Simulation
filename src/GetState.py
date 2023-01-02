#################################################################
# CS - 499 Team 3                                               #
#                                                               #
# Written By: Trebor Bearden and Kali Mcintire and Ian Yuen     #
#                                                               #
# Utility File for getting the most recent state of each device #
# in the database                                               #
#################################################################

import psycopg2 as p
from random import *

#temperatures

def Threshold_State():
    '''
    This function queries the database for the most recent state of the Threshold temp.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("SELECT * FROM public.temperatures ORDER BY time DESC ;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Inside_State():
    '''
    This function queries the database for the most recent state of the Inside temp.
    Params:
        None
    Returns:
        data[0][1]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][1] is the state of the most event that the query returns
        }
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("SELECT * FROM public.temperatures ORDER BY time DESC ;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][1])

def Outside_State():
    '''
    This function queries the database for the most recent state of the Front Door.
    Params:
        None
    Returns:
        data[0][2]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][2] is the state of the most event that the query returns
        }
    '''
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("SELECT * FROM public.temperatures ORDER BY time DESC ;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][2])

# doors windows states

def Front_Door_State():
    '''
    This function queries the database for the most recent state of the Front Door.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select door_window_event, door_window_event_id, max(event_time) from store_window_usage where door_window_id = 1 group by door_window_event, door_window_event_id, event_time order by door_window_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Back_Door_State():
    '''
    This function queries the database for the most recent state of the Back Door.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select door_window_event, door_window_event_id, max(event_time) from store_window_usage where door_window_id = 2 group by door_window_event, door_window_event_id, event_time order by door_window_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Garage_Door_State():
    '''
    This function queries the database for the most recent state of the Garage Door.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select door_window_event, door_window_event_id, max(event_time) from store_window_usage where door_window_id = 3 group by door_window_event, door_window_event_id, event_time order by door_window_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


# Power Utility states

def Master_Bedroom_Overhead_State():
    '''
    This function queries the database for the most recent state of the Master Bedroom Overhead Light.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 1 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Bedroom2_Overhead_State():
    '''
    This function queries the database for the most recent state of the Second Bedroom Overhead Light.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 2 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Bedroom3_Overhead_State():
    '''
    This function queries the database for the most recent state of the Third Bedroom Overhead Light.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 3 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    # print(data[0][0])
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Master_Bedroom_Lamp_1_State():
    '''
    This function queries the database for the most recent state of the First lamp in the Master Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 4 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Master_Bedroom_Lamp_2_State():
    '''
    This function queries the database for the most recent state of the Second lamp in the Master Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 5 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bedroom2_Lamp_1_State():
    '''
    This function queries the database for the most recent state of the First lamp in the Second Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 6 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bedroom2_Lamp_2_State():
    '''
    This function queries the database for the most recent state of the Second lamp in the Second Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 7 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bedroom3_Lamp_1_State():
    '''
    This function queries the database for the most recent state of the First lamp in the Third Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 8 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bedroom3_Lamp_2_State():
    '''
    This function queries the database for the most recent state of the Second lamp in the Third Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 9 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Master_Bedroom_TV_State():
    '''
    This function queries the database for the most recent state of the TV in the Master Bedroom.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 10 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Garage_Door_Power_1_State():
    '''
    This function queries the database for the most recent state of the First Garage Door.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 11 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Garage_Door_Power_2_State():
    '''
    This function queries the database for the most recent state of the Second Garage Door.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 12 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Dryer_State():
    '''
    This function queries the database for the most recent state of the Clothes Dryer.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 14 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def Living_Room_Overhead_State():
    '''
    This function queries the database for the most recent state of the Living Room Overhead Light.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 15 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Living_Room_Lamp_1_State():
    '''
    This function queries the database for the most recent state of the first lamp in the Living Room.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 16 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Living_Room_Lamp_2_State():
    '''
    This function queries the database for the most recent state of the Second Lamp in the Living Room.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 17 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Living_Room_TV_State():
    '''
    This function queries the database for the most recent state of the TV in the Living Room.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 18 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Kitchen_Overhead_State():
    '''
    This function queries the database for the most recent state of the Kitchen Overhead.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 19 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Stove_State():
    '''
    This function queries the database for the most recent state of the Stove.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 20 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Oven_State():
    '''
    This function queries the database for the most recent state of the Oven.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 21 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Microwave_State():
    '''
    This function queries the database for the most recent state of the Microwave.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 22 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Refridgerator_State():
    '''
    This function queries the database for the most recent state of the Refridgerator.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 23 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


def HVAC_State():
    '''
    This function queries the database for the most recent state of the HVAC.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 25 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])



def Bathroom1_Overhead_State():
    '''
    This function queries the database for the most recent state of the first bathroom Overhead.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 32 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom2_Overhead_State():
    '''
    This function queries the database for the most recent state of the second bathroom overhead.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 33 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom1_Exhaust_Fan_State():
    '''
    This function queries the database for the most recent state of the first bathroom exhaust fan.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 34 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom2_Exhaust_Fan_State():
    '''
    This function queries the database for the most recent state of the second bathroom exhuast fan.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, power_event_id, max(event_time) from power_usage where utility_id = 35 group by utility_event, power_event_id, event_time order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


# Water utility States

def Washer_State():
    '''
    This function queries the database for the most recent state of the Clothes washer.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 13 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Dishwasher_State():
    '''
    This function queries the database for the most recent state of the Dishwasher.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 24 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom1_Sink_State():
    '''
    This function queries the database for the most recent state of the first bathroom sink.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 26 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom2_Sink_State():
    '''
    This function queries the database for the most recent state of the second bathroom sink.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 27 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Kitchen_Sink_State():
    '''
    This function queries the database for the most recent state of the Kitchen sink.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 28 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom1_Shower_State():
    '''
    This function queries the database for the most recent state of the first bathroom shower.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 29 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Bathroom2_Shower_State():
    '''
    This function queries the database for the most recent state of the second bathroom shower.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 30 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Outside_Faucet_State():
    '''
    This function queries the database for the most recent state of the Outside Faucet.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the state of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select utility_event, max(date) from water_usage where utility_id = 31 group by utility_event, date order by date desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Get_Recent_ID():
    '''
    This function queries the database for the most recent Power event ID.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the id of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select power_event_id from power_usage order by power_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Get_Recent_Water_ID():
    '''
    This function queries the database for the most recent water event ID.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the id of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select water_event_ID from water_usage order by water_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])

def Get_Recent_Door_ID():
    '''
    This function queries the database for the most recent Door/Window event ID.
    Params:
        None
    Returns:
        data[0][0]
        {
            data is the results of the query to get the most recent id for this device [(event,utility_id,time])
            data[0] is the first tuple that the query returns (The most recent logged event)
            data[0][0] is the id of the most event that the query returns
        }
    '''

    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select door_window_event_id from store_window_usage order by door_window_event_id desc;")
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return(data[0][0])


# print(randrange(1,4))
# print(Master_Bedroom_Overhead_State())
# print(Bedroom2_Overhead_State())
# print(Bedroom3_Overhead_State())
# print(Living_Room_Overhead_State())
# print(Kitchen_Overhead_State())
# print(Bathroom1_Overhead_State())
# print(Bathroom2_Overhead_State())

# select utility_event, max(event_time) from power_usage where utility_id = 14 group by utility_event;
#
# select door_window_event, max(event_time) from store_window_usage where door_window_id = 1 group by door_window_event;

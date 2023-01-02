#################################################################
# CS - 499 Team 3                                               #
#                                                               #
# Written By: Trebor Bearden                                    #
#                                                               #
# Utility File for getting the yearly and monthly power and     #
# water usage data for the reports page                         #
#################################################################

import psycopg2 as p
from datetime import *

# _________________________________________________________________________________________________________________________________________________________________________
#                                                  Get Yearly Data points
# _________________________________________________________________________________________________________________________________________________________________________

# These are global variables used so that local functions can return all neccessary data to other functions
yearly_power_list = []
yearly_water_list = []
monthly_power_list = []
monthly_water_list = []
month_and_usage_power = ()
month_and_usage_water = ()
day_and_usage_power = ()
day_and_usage_water = ()


def Get_Data_Yearly(Year,Month,Day):
    '''
    This function queries the databases to recieve yearly power and water usage.
    This function calculates the current usage amounts as well as converts usage to their end states.
    This function predicts the next months power and water usage as well.
    Params:
        Year - the year in which the front end user specifies (always 2022)
        Month - the month in which the front end user specifies (user input from chart.html or chart2.html)
        Day - the specific day which is hardcoded from the function Get_Monthly_Data_For_Yearly_Chart()
    Returns:
        month_and_usage_power -  a tuple containing the month and the power usage for that month
    '''

    # DB connection
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Select * from power_usage where event_time BETWEEN '"+ Year +"-"+ Month +"-01 00:00:00'::timestamp AND '"+ Year +"-"+ Month +"-"+ Day +" 23:59:59'::timestamp;")
    powerData = cur.fetchall()

    # 'Global-local' variables for this function
    # needed to keep track of total watts used for the different wattages across different devices
    total_kwh = 0
    total_hvac = 0
    total_dishwasher = 0
    total_fridge = 0
    total_microwave = 0
    total_oven = 0
    total_stove = 0
    total_BR_Tv = 0
    total_dryer = 0
    total_washer = 0
    total_LR_Tv = 0
    total_light_bulb = 0
    total_seconds = 0
    total_minutes = 0
    total_hours = 0
    total_exhaust = 0
    usage = timedelta(0)

    # looping through queried data and finding the time between each events
    for i in range(0,len(powerData)):
        if powerData[i][2] == 'on':
            if (powerData[i][1] == 1 or  powerData[i][1] == 2 or powerData[i][1] == 3 or powerData[i][1] == 4 or powerData[i][1] == 5 or powerData[i][1] == 6 or powerData[i][1] == 7 or powerData[i][1] == 8 or powerData[i][1] == 9 or powerData[i][1] == 15 or powerData[i][1] == 16 or powerData[i][1] == 17 or powerData[i][1] == 19 or powerData[i][1] == 32 or powerData[i][1] == 33):
                start = powerData[i]
                end = powerData[i+1]
                total_light_bulb = find_time(total_light_bulb,usage,start,end)
            elif powerData[i][1] == 10:
                start = powerData[i]
                end = powerData[i+1]
                total_LR_Tv = find_time(total_LR_Tv,usage,start,end)
            elif powerData[i][1] == 13:
                start = powerData[i]
                end = powerData[i+1]
                total_washer = find_time(total_washer,usage,start,end)
            elif powerData[i][1] == 14:
                start = powerData[i]
                end = powerData[i+1]
                total_dryer = find_time(total_dryer,usage,start,end)
            elif powerData[i][1] == 18:
                start = powerData[i]
                end = powerData[i+1]
                total_BR_Tv = find_time(total_BR_Tv,usage,start,end)
            elif powerData[i][1] == 20:
                start = powerData[i]
                end = powerData[i+1]
                total_stove = find_time(total_stove,usage,start,end)
            elif powerData[i][1] == 21:
                start = powerData[i]
                end = powerData[i+1]
                total_oven = find_time(total_oven,usage,start,end)
            elif powerData[i][1] == 22:
                start = powerData[i]
                end = powerData[i+1]
                total_microwave = find_time(total_microwave,usage,start,end)
            elif powerData[i][1] == 23:
                start = powerData[i]
                end = powerData[i+1]
                total_fridge = find_time(total_fridge,usage,start,end)
            elif powerData[i][1] == 24:
                start = powerData[i]
                end = powerData[i+1]
                total_dishwasher = find_time(total_dishwasher,usage,start,end)
            elif powerData[i][1] == 25:
                start = powerData[i]
                end = powerData[i+1]
                total_hvac = find_time(total_hvac,usage,start,end)
            elif powerData[i][1] == 34 or powerData[i][1] == 35:
                start = powerData[i]
                end = powerData[i+1]
                total_exhaust = find_time(total_exhaust,usage,start,end)
        else:
            continue

    # Calculating Kwh for light bulbs
    day = total_light_bulb // (24 * 3600)
    total_light_bulb = total_light_bulb % (24 * 3600)
    hour = total_light_bulb // 3600
    total_light_bulb %= 3600
    minutes = total_light_bulb // 60
    total_light_bulb %= 60
    seconds = total_light_bulb
    bulb_hours = day * 24
    bulb_hours = bulb_hours + hour + (minutes / 100)
    bulb_kwh = (60 * bulb_hours) / 1000
    total_kwh += bulb_kwh

    # Calculating Kwh for Living room TV
    day = total_LR_Tv // (24 * 3600)
    total_LR_Tv = total_LR_Tv % (24 * 3600)
    hour = total_LR_Tv // 3600
    total_LR_Tv %= 3600
    minutes = total_LR_Tv // 60
    total_LR_Tv %= 60
    seconds = total_LR_Tv
    Ltv_hours = day * 24
    Ltv_hours = Ltv_hours + hour + (minutes / 100)
    Ltv_kwh = (636 * Ltv_hours) / 1000
    total_kwh += Ltv_kwh

    # Calculating Kwh for clothes washer
    day = total_washer // (24 * 3600)
    total_washer = total_washer % (24 * 3600)
    hour = total_washer // 3600
    total_washer %= 3600
    minutes = total_washer // 60
    total_washer %= 60
    seconds = total_washer
    washer_hours = day * 24
    washer_hours = washer_hours + hour + (minutes / 100)
    washer_kwh = (500 * washer_hours) / 1000
    total_kwh += washer_kwh

    # Calculating Kwh for dryer
    day = total_dryer // (24 * 3600)
    total_dryer = total_dryer % (24 * 3600)
    hour = total_dryer // 3600
    total_dryer %= 3600
    minutes = total_dryer // 60
    total_dryer %= 60
    seconds = total_dryer
    dryer_hours = day * 24
    dryer_hours = dryer_hours + hour + (minutes / 100)
    dryer_kwh = (3000 * dryer_hours) / 1000
    total_kwh += dryer_kwh

    # Calculating Kwh for bed room tv
    day = total_BR_Tv // (24 * 3600)
    total_BR_Tv = total_BR_Tv % (24 * 3600)
    hour = total_BR_Tv // 3600
    total_BR_Tv %= 3600
    minutes = total_BR_Tv // 60
    total_BR_Tv %= 60
    seconds = total_BR_Tv
    Btv_hours = day * 24
    Btv_hours = Btv_hours + hour + (minutes / 100)
    Btv_kwh = (100 * Btv_hours) / 1000
    total_kwh += Btv_kwh

    # Calculating Kwh for stove
    day = total_stove // (24 * 3600)
    total_stove = total_stove % (24 * 3600)
    hour = total_stove // 3600
    total_stove %= 3600
    minutes = total_stove // 60
    total_stove %= 60
    seconds = total_stove
    stove_hours = day * 24
    stove_hours = stove_hours + hour + (minutes / 100)
    stove_kwh = (3500 * stove_hours) / 1000
    total_kwh += stove_kwh

    # Calculating Kwh for oven
    day = total_oven // (24 * 3600)
    total_oven = total_oven % (24 * 3600)
    hour = total_oven // 3600
    total_oven %= 3600
    minutes = total_oven // 60
    total_oven %= 60
    seconds = total_oven
    oven_hours = day * 24
    oven_hours = oven_hours + hour + (minutes / 100)
    oven_kwh = (4000 * oven_hours) / 1000
    total_kwh += oven_kwh

    # Calculating Kwh for microwave
    day = total_microwave // (24 * 3600)
    total_microwave = total_microwave % (24 * 3600)
    hour = total_microwave // 3600
    total_microwave %= 3600
    minutes = total_microwave // 60
    total_microwave %= 60
    seconds = total_microwave
    micro_hours = day * 24
    micro_hours = micro_hours + hour + (minutes / 100)
    micro_kwh = (1100 * micro_hours) / 1000
    total_kwh += micro_kwh

    # Calculating Kwh for fridge
    day = total_fridge // (24 * 3600)
    total_fridge = total_fridge % (24 * 3600)
    hour = total_fridge // 3600
    total_fridge %= 3600
    minutes = total_fridge // 60
    total_fridge %= 60
    seconds = total_fridge
    fridge_hours = day * 24
    fridge_hours = fridge_hours + hour + (minutes / 100)
    fridge_kwh = (150 * fridge_hours) / 1000
    total_kwh += fridge_kwh

    # Calculating Kwh for dishwasher
    day = total_dishwasher // (24 * 3600)
    total_dishwasher = total_dishwasher % (24 * 3600)
    hour = total_dishwasher // 3600
    total_dishwasher %= 3600
    minutes = total_dishwasher // 60
    total_dishwasher %= 60
    seconds = total_dishwasher
    dish_hours = day * 24
    dish_hours = dish_hours + hour + (minutes / 100)
    dish_kwh = (1800 * dish_hours) / 1000
    total_kwh += dish_kwh

    # Calculating Kwh for hvac
    day = total_hvac // (24 * 3600)
    total_hvac = total_hvac % (24 * 3600)
    hour = total_hvac // 3600
    total_hvac %= 3600
    minutes = total_hvac // 60
    total_hvac %= 60
    seconds = total_hvac
    hvac_hours = day * 24
    hvac_hours = hvac_hours + hour + (minutes / 100)
    hvac_kwh = (3500 * hvac_hours) / 1000
    total_kwh += hvac_kwh

    # Calculating Kwh for exhaust fans
    day = total_exhaust // (24 * 3600)
    total_exhaust = total_exhaust % (24 * 3600)
    hour = total_exhaust // 3600
    total_exhaust %= 3600
    minutes = total_exhaust // 60
    total_exhaust %= 60
    seconds = total_exhaust
    exhaust_hours = day * 24
    exhaust_hours = exhaust_hours + hour + (minutes / 100)
    exhaust_kwh = (30 * exhaust_hours) / 1000
    total_kwh += exhaust_kwh

    # print("Power usage = ", total_kwh)
    # yearly_power_list.append(total_kwh)

    # Getting the month for return
    if Month == '01':
        month = 'January'
    elif Month == '02':
        month = 'Febuary'
    elif Month == '03':
        month = 'March'
    elif Month == '04':
        month = 'April'
    elif Month == '05':
        month = 'May'
    elif Month == '06':
        month = 'June'
    elif Month == '07':
        month = 'July'
    elif Month == '08':
        month = 'August'
    elif Month == '09':
        month = 'September'
    elif Month == '10':
        month = 'October'
    elif Month == '11':
        month = 'November'
    elif Month == '12':
        month = 'December'

    # making a tuple to return
    month_and_usage_power = (month,round(total_kwh,2))

    return(month_and_usage_power)


def Get_Yearly_Water(Year,Month,Day):
    '''
    This function queries the databases to recieve yearly power and water usage.
    This function calculates the current usage amounts as well as converts usage to their end states.
    This function predicts the next months power and water usage as well.
    Params:
        Year - the year in which the front end user specifies (always 2022)
        Month - the month in which the front end user specifies (user input from chart.html or chart2.html)
        Day - the specific day which is hardcoded from the function Get_Monthly_Data_For_Yearly_Chart()
    Returns:
        month_and_water_power -  a tuple containing the month and the power usage for that month
    '''

    # DB connection
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select sum(gallons) from water_usage where date BETWEEN '"+ Year +"-"+ Month +"-01'::timestamp AND '"+ Year +"-"+ Month +"-"+ Day +"'::timestamp;")
    waterData = cur.fetchall()

    # getting each month data
    for row in waterData:
        # print("Water usage = ", row[0], "\n")
        # yearly_water_list.append(row[0])
        if row[0] == None:
            water = 0
        else:
            water = row[0] / 7.48

        if Month == '01':
            month = 'January'
        elif Month == '02':
            month = 'Febuary'
        elif Month == '03':
            month = 'March'
        elif Month == '04':
            month = 'April'
        elif Month == '05':
            month = 'May'
        elif Month == '06':
            month = 'June'
        elif Month == '07':
            month = 'July'
        elif Month == '08':
            month = 'August'
        elif Month == '09':
            month = 'September'
        elif Month == '10':
            month = 'October'
        elif Month == '11':
            month = 'November'
        elif Month == '12':
            month = 'December'

        # making a tuple
        month_and_usage_water = (month, round(water,2))

        return(month_and_usage_water)


def Get_Data_Monthly(Year,Month,Day):
    '''
    This function queries the databases to recieve monthly power usage.
    This function calculates the current usage amounts as well as converts usage to their end states.
    This function predicts the next months power usage as well.
    Params:
        Year - the year in which the front end user specifies (always 2022)
        Month - the month in which the front end user specifies (user input from chart.html or chart2.html)
        Day - the specific day which is hardcoded from the function Get_Monthly_Data_For_Yearly_Chart()
    Returns:
        day_and_usage_power -  a tuple containing the month and the power usage for that month
    '''

    # DB connection
    next_Day = int(Day) + 1
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("Select * from power_usage where event_time BETWEEN '"+ Year +"-"+ Month +"-"+ Day +" 00:00:00'::timestamp AND '"+ Year +"-"+ Month +"-"+ Day +" 23:59:59'::timestamp;")
    powerData = cur.fetchall()

    powerData.append((1,10,'off', datetime(int(Year), int(Month), int(Day), 23, 59, 59)))

    # ---------------------------------- See Yearly usage for documentation ------------------------------------
                                            # (it's pretty much the same)

    total_kwh = 0
    total_hvac = 0
    total_dishwasher = 0
    total_fridge = 0
    total_microwave = 0
    total_oven = 0
    total_stove = 0
    total_BR_Tv = 0
    total_dryer = 0
    total_washer = 0
    total_LR_Tv = 0
    total_light_bulb = 0
    total_seconds = 0
    total_minutes = 0
    total_hours = 0
    total_exhaust = 0
    usage = timedelta(0)

    for i in range(0,len(powerData)):
        if powerData[i][2] == 'on':
            if (powerData[i][1] == 1 or  powerData[i][1] == 2 or powerData[i][1] == 3 or powerData[i][1] == 4 or powerData[i][1] == 5 or powerData[i][1] == 6 or powerData[i][1] == 7 or powerData[i][1] == 8 or powerData[i][1] == 9 or powerData[i][1] == 15 or powerData[i][1] == 16 or powerData[i][1] == 17 or powerData[i][1] == 19 or powerData[i][1] == 32 or powerData[i][1] == 33):
                start = powerData[i]
                end = powerData[i+1]
                total_light_bulb = find_time(total_light_bulb,usage,start,end)
            elif powerData[i][1] == 10:
                start = powerData[i]
                end = powerData[i+1]
                total_LR_Tv = find_time(total_LR_Tv,usage,start,end)
            elif powerData[i][1] == 13:
                start = powerData[i]
                end = powerData[i+1]
                total_washer = find_time(total_washer,usage,start,end)
            elif powerData[i][1] == 14:
                start = powerData[i]
                end = powerData[i+1]
                total_dryer = find_time(total_dryer,usage,start,end)
            elif powerData[i][1] == 18:
                start = powerData[i]
                end = powerData[i+1]
                total_BR_Tv = find_time(total_BR_Tv,usage,start,end)
            elif powerData[i][1] == 20:
                start = powerData[i]
                end = powerData[i+1]
                total_stove = find_time(total_stove,usage,start,end)
            elif powerData[i][1] == 21:
                start = powerData[i]
                end = powerData[i+1]
                total_oven = find_time(total_oven,usage,start,end)
            elif powerData[i][1] == 22:
                start = powerData[i]
                end = powerData[i+1]
                total_microwave = find_time(total_microwave,usage,start,end)
            elif powerData[i][1] == 23:
                start = powerData[i]
                end = powerData[i+1]
                total_fridge = find_time(total_fridge,usage,start,end)
            elif powerData[i][1] == 24:
                start = powerData[i]
                end = powerData[i+1]
                total_dishwasher = find_time(total_dishwasher,usage,start,end)
            elif powerData[i][1] == 25:
                start = powerData[i]
                end = powerData[i+1]
                total_hvac = find_time(total_hvac,usage,start,end)
            elif powerData[i][1] == 34 or powerData[i][1] == 35:
                start = powerData[i]
                end = powerData[i+1]
                total_exhaust = find_time(total_exhaust,usage,start,end)
        else:
            continue

    day = total_light_bulb // (24 * 3600)
    total_light_bulb = total_light_bulb % (24 * 3600)
    hour = total_light_bulb // 3600
    total_light_bulb %= 3600
    minutes = total_light_bulb // 60
    total_light_bulb %= 60
    seconds = total_light_bulb
    # bulb_hours = day * 24
    bulb_hours = hour + (minutes / 100)
    bulb_kwh = (60 * bulb_hours) / 1000
    total_kwh += bulb_kwh
    #print(total_kwh)

    day = total_LR_Tv // (24 * 3600)
    total_LR_Tv = total_LR_Tv % (24 * 3600)
    hour = total_LR_Tv // 3600
    total_LR_Tv %= 3600
    minutes = total_LR_Tv // 60
    total_LR_Tv %= 60
    seconds = total_LR_Tv
    # Ltv_hours = day * 24
    Ltv_hours = hour + (minutes / 100)
    Ltv_kwh = (636 * Ltv_hours) / 1000
    total_kwh += Ltv_kwh
    #print(total_kwh)

    day = total_washer // (24 * 3600)
    total_washer = total_washer % (24 * 3600)
    hour = total_washer // 3600
    total_washer %= 3600
    minutes = total_washer // 60
    total_washer %= 60
    seconds = total_washer
    # washer_hours = day * 24
    washer_hours = hour + (minutes / 100)
    washer_kwh = (500 * washer_hours) / 1000
    total_kwh += washer_kwh
    #print(total_kwh)

    day = total_dryer // (24 * 3600)
    total_dryer = total_dryer % (24 * 3600)
    hour = total_dryer // 3600
    total_dryer %= 3600
    minutes = total_dryer // 60
    total_dryer %= 60
    seconds = total_dryer
    # dryer_hours = day * 24
    dryer_hours = hour + (minutes / 100)
    dryer_kwh = (3000 * dryer_hours) / 1000
    total_kwh += dryer_kwh
    #print(total_kwh)

    day = total_BR_Tv // (24 * 3600)
    total_BR_Tv = total_BR_Tv % (24 * 3600)
    hour = total_BR_Tv // 3600
    total_BR_Tv %= 3600
    minutes = total_BR_Tv // 60
    total_BR_Tv %= 60
    seconds = total_BR_Tv
    # Btv_hours = day * 24
    Btv_hours = hour + (minutes / 100)
    Btv_kwh = (100 * Btv_hours) / 1000
    total_kwh += Btv_kwh
    #print(total_kwh)

    day = total_stove // (24 * 3600)
    total_stove = total_stove % (24 * 3600)
    hour = total_stove // 3600
    total_stove %= 3600
    minutes = total_stove // 60
    total_stove %= 60
    seconds = total_stove
    # stove_hours = day * 24
    stove_hours = hour + (minutes / 100)
    stove_kwh = (3500 * stove_hours) / 1000
    total_kwh += stove_kwh
    #print(total_kwh)

    day = total_oven // (24 * 3600)
    total_oven = total_oven % (24 * 3600)
    hour = total_oven // 3600
    total_oven %= 3600
    minutes = total_oven // 60
    total_oven %= 60
    seconds = total_oven
    # oven_hours = day * 24
    oven_hours = hour + (minutes / 100)
    oven_kwh = (4000 * oven_hours) / 1000
    total_kwh += oven_kwh
    #print(total_kwh)

    day = total_microwave // (24 * 3600)
    total_microwave = total_microwave % (24 * 3600)
    hour = total_microwave // 3600
    total_microwave %= 3600
    minutes = total_microwave // 60
    total_microwave %= 60
    seconds = total_microwave
    # micro_hours = day * 24
    micro_hours = hour + (minutes / 100)
    micro_kwh = (1100 * micro_hours) / 1000
    total_kwh += micro_kwh
    #print(total_kwh)

    day = total_fridge // (24 * 3600)
    total_fridge = total_fridge % (24 * 3600)
    hour = total_fridge // 3600
    total_fridge %= 3600
    minutes = total_fridge // 60
    total_fridge %= 60
    seconds = total_fridge
    # fridge_hours = day * 24
    fridge_hours = hour + (minutes / 100)
    fridge_kwh = (150 * fridge_hours) / 1000
    total_kwh += fridge_kwh
    #print(total_kwh)

    day = total_dishwasher // (24 * 3600)
    total_dishwasher = total_dishwasher % (24 * 3600)
    hour = total_dishwasher // 3600
    total_dishwasher %= 3600
    minutes = total_dishwasher // 60
    total_dishwasher %= 60
    seconds = total_dishwasher
    # dish_hours = day * 24
    dish_hours = hour + (minutes / 100)
    dish_kwh = (1800 * dish_hours) / 1000
    total_kwh += dish_kwh
    #print(total_kwh)

    day = total_hvac // (24 * 3600)
    total_hvac = total_hvac % (24 * 3600)
    hour = total_hvac // 3600
    total_hvac %= 3600
    minutes = total_hvac // 60
    total_hvac %= 60
    seconds = total_hvac
    # hvac_hours = day * 24
    hvac_hours = hour + (minutes / 100)
    hvac_kwh = (3500 * hvac_hours) / 1000
    total_kwh += hvac_kwh
    #print(total_kwh)

    day = total_exhaust // (24 * 3600)
    total_exhaust = total_exhaust % (24 * 3600)
    hour = total_exhaust // 3600
    total_exhaust %= 3600
    minutes = total_exhaust // 60
    total_exhaust %= 60
    seconds = total_exhaust
    # exhaust_hours = day * 24
    exhaust_hours = hour + (minutes / 100)
    exhaust_kwh = (30 * exhaust_hours) / 1000
    total_kwh += exhaust_kwh
    #print(total_kwh)

    # print("Power usage = ", total_kwh)

    month_and_usage_power = (Day,round(total_kwh,2))

    return(month_and_usage_power)
    #
    # cur.execute("select sum(gallons) from water_usage where date BETWEEN '"+ Year +"-"+ Month +"-"+ Day +" 00:00:00'::timestamp AND '"+ Year +"-"+ Month +"-"+ Day +" 23:59:59'::timestamp;")
    # waterData = cur.fetchall()
    # for row in waterData:
    #     print("Water usage = ", row[0], "\n")

def Get_Monthly_Water(Year,Month,Day):
    '''
    This function queries the databases to recieve monthly water usage.
    This function calculates the current usage amounts as well as converts usage to their end states.
    This function predicts the next months power and water usage as well.
    Params:
        Year - the year in which the front end user specifies (always 2022)
        Month - the month in which the front end user specifies (user input from chart.html or chart2.html)
        Day - the specific day which is hardcoded from the function Get_Monthly_Data_For_Yearly_Chart()
    Returns:
        day_and_usage_water -  a tuple containing the month and the water usage for that day
    '''

    # DB connection
    con = p.connect(user='Team3', password='team3', host='138.26.48.83', port='5432', database='Team3DB')
    cur = con.cursor()
    cur.execute("select sum(gallons) from water_usage where date BETWEEN '"+ Year +"-"+ Month +"-"+ Day +" 00:00:00'::timestamp AND '"+ Year +"-"+ Month +"-"+ Day +" 23:59:59'::timestamp;")
    waterData = cur.fetchall()
    for row in waterData:
        # print("Water usage = ", row[0], "\n")
        # yearly_water_list.append(row[0])
        if row[0] == None:
            water = 0
        else:
            water = row[0] / 7.48

        day_and_usage_water = (Day,round(water,2))

        return(day_and_usage_water)

def find_time(total_usage,usage,start,end):
    '''
    Helper function to find the time between two events
    Params:
        total_usage: the total usage of the two events
        usage: the difference between the two events
        start: the on event
        end: the off event
    returns:
        total_usage: the total usage
    '''

    usage = end[3]-start[3]
    seconds = usage.total_seconds()
    total_usage += seconds
    return(total_usage)

    cur.close()
    con.close()

def Get_Monthly_Data_For_Yearly_Chart():
    '''
    Main Yearly Function
    Params:
        None
    returns:
        yearly_power_list: power usage per month - list
        yearly_water_list: water usage per month - list
    '''
    today = date.today()
    year = today.year

    months = [["01","31"],["02","28"],["03","31"],["04","30"],["05","31"],["06","30"],["07","31"],["08","31"],["09","30"],["10","31"],["11","30"],["12","31"]]
    for i in range(0,len(months)):
        yearly_power_list.append(Get_Data_Yearly(str(year),months[i][0],months[i][1]))
        yearly_water_list.append(Get_Yearly_Water(str(year),months[i][0],months[i][1]))

    return(yearly_power_list,yearly_water_list)

# Get_Monthly_Data_For_Yearly_Chart()

# _________________________________________________________________________________________________________________________________________________________________________
#                                                  Get Monthly Data points
# _________________________________________________________________________________________________________________________________________________________________________

def Get_Weekly_Data_For_Monthly_Chart(Month):
    '''
    Main Yearly Function
    Params:
        None
    returns:
        monthly_power_list: power usage per day - list
        monthly_water_list: water usage per day - list
    '''

    today = date.today()
    year = today.year
    day = 0
    months = [["01",31],["02",28],["03",31],["04",30],["05",31],["06",30],["07",31],["08",31],["09",30],["10",31],["11",30],["12",31]]

    if Month == "01":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[0][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[0][0],str(day)))

    elif Month == "02":
        for i in range(28):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[1][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[1][0],str(day)))

    elif Month == "03":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[2][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[2][0],str(day)))

    elif Month == "04":
        for i in range(30):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[3][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[3][0],str(day)))

    elif Month == "05":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[4][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[4][0],str(day)))

    elif Month == "06":
        for i in range(30):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[5][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[5][0],str(day)))

    elif Month == "07":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[6][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[6][0],str(day)))

    elif Month == "08":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[7][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[7][0],str(day)))

    elif Month == "09":
        for i in range(30):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[8][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[8][0],str(day)))

    elif Month == "10":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[9][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[9][0],str(day)))

    elif Month == "11":
        for i in range(30):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[10][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[10][0],str(day)))

    elif Month == "12":
        for i in range(31):
            day += 1
            monthly_power_list.append(Get_Data_Monthly(str(year),months[11][0],str(day)))
            monthly_water_list.append(Get_Monthly_Water(str(year),months[11][0],str(day)))

    return(monthly_power_list,monthly_water_list)



# print(Get_Weekly_Data_For_Monthly_Chart("07"))
# print(Get_Monthly_Data_For_Yearly_Chart())

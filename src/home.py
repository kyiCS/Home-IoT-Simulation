#################################################################
# CS - 499 Team 3                                               #
#                                                               #
# Written By: Trebor Bearden, Adrian Hilton, Kali Mcintire,     #
# Trevin Rodda, and Kelvin Yi                                   #
#                                                               #
# The Back End                                                  #
#################################################################

import os
from flask import Flask, render_template, Response, request, redirect, url_for, flash, session, jsonify
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from datetime import *
from dateutil.relativedelta import *
import DBRead
import Event_Utils
import GetState
import threading
import time as time
import requests, json

# app config stuff
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ourfinalprojectisawesome'
basedir = os.path.abspath(os.path.dirname(__file__))

# Global Variables for thermostat
threshold = GetState.Threshold_State()
inside = GetState.Inside_State()
outside = GetState.Outside_State()

# weather API stuff
api_key="b2916bd1be6ef042718a5e53121fb584"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + "Birmingham"


def tempUpdate():
    '''
    Function to monitor and update the HVAC when threshold temp is modified.
    Params:
        None
    Returns:
        None

    Writes to the DB as needed (HVAC on and off)
    '''
    threading.Timer(10.0, tempUpdate).start()
    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()

    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    HVAC = GetState.HVAC_State()

    id = GetState.Get_Recent_ID() + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    countOpen = 0
    for n in [FD,BD,GD]:
        if n == "open":
            countOpen += 1

    diff = abs(inside-outside)%10

    #inside is within 2 degrees of set temp
    if abs(threshold-inside)<=2:
        if HVAC == 'on':
            Event_Utils.HVAC_Off(id, 25, "off", timestamp)

    #inside is less than set temp
    elif (threshold-inside)>2:
        if HVAC == 'off':
            Event_Utils.HVAC_On(id, 25, "on", timestamp)

        if countOpen == 0:
            inside += (1/6)*diff
        else:
            inside += 2
            if inside>outside:
                inside -= 2*countOpen
                if inside<outside:
                    inside = outside

            if inside<outside:
                inside += 2* countOpen
                if inside>outside:
                    inside = outside

        if inside > threshold:
            inside = threshold

    #inside is greater than set temp
    elif (threshold-inside)<-2:
        if HVAC == 'off':
            Event_Utils.HVAC_On(id, 25, "on", timestamp)

        if countOpen == 0:
            inside -= (1/6)*diff
        else:
            inside -= 2
            if inside>outside:
                inside -= 2*countOpen
                if inside<outside:
                    inside = outside

            if inside<outside:
                inside += 2* countOpen
                if inside>outside:
                    inside = outside

        if inside < threshold:
            inside = threshold

    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"] * 1.8 - 459.67
    print(current_temperature)


    Event_Utils.Update_Temperature(threshold,inside,current_temperature,int((str(time.time())).split('.')[0]))

tempUpdate()

"""
function to check user inputted PIN against correct PIN
"""

def checkPIN(code):
    passCode = '1234'
    if code == passCode:
        return True
    return False

"""
If a PIN is entered on the home page and it is correct then app will redirect to the layout page
If not then it will stay on the enter the PIN page
PIN is taken form the input of the textbox and used as a parameter to the checkPIN function (returns a boolean)
"""

@app.route("/", methods=["POST", "GET"])
def securityCheck():
    if request.method == "POST":
        PIN = request.form["PIN"]

        if checkPIN(PIN) == True:
            return redirect(url_for("layout"))

        else:
            flash("Incorrect PIN, try again..")
            return render_template("index.html")

    return render_template("index.html", threshold=threshold, outside=outside, inside=inside)


@app.route('/layout')
def layout():
    '''
    This function is what occurs when the 'layout page' is loaded
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''
    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    MBOH = GetState.Master_Bedroom_Overhead_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    LROH = GetState.Living_Room_Overhead_State()
    KOH = GetState.Kitchen_Overhead_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()

    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()


    return render_template('layout.html', FD=FD, BD=BD, GD=GD, MBOH=MBOH, B2OH=B2OH, B3OH=B3OH, LROH=LROH, KOH=KOH, Bath1OH=Bath1OH, Bath2OH=Bath2OH, threshold=int(threshold), inside=int(inside), outside=int(outside))

@app.route('/thermostat/', methods=['POST'])
def getThreshold():
    '''
    This function monitors the Thermostat threshold value for when it is increased or decreased
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''
    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    MBOH = GetState.Master_Bedroom_Overhead_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    LROH = GetState.Living_Room_Overhead_State()
    KOH = GetState.Kitchen_Overhead_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()

    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()

    if request.method == "POST":
        setTemp = request.form.get('threshold')
        if setTemp!=None:
            Event_Utils.Update_Temperature(int(setTemp),inside,outside,int((str(time.time())).split('.')[0]))
    return render_template('layout.html', FD=FD, BD=BD, GD=GD, MBOH=MBOH, B2OH=B2OH, B3OH=B3OH, LROH=LROH, KOH=KOH, Bath1OH=Bath1OH, Bath2OH=Bath2OH, threshold=int(threshold), inside=int(inside), outside=int(outside))



@app.route('/runDishwasher/', methods=['GET', 'POST'])
def RunDishwasher():
    '''
    This function is a simulated event that runs the dishwasher for 45 minutes.
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    MBOH = GetState.Master_Bedroom_Overhead_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    LROH = GetState.Living_Room_Overhead_State()
    KOH = GetState.Kitchen_Overhead_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()

    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()

    id1 = GetState.Get_Recent_ID() + 1
    water_id = GetState.Get_Recent_Water_ID() + 1
    onTime = datetime.now().time()
    dateWater = date.today()
    datetimeOn = datetime.combine(dateWater, onTime)
    time_change = timedelta(minutes=45)
    offTime = datetimeOn + time_change

    Event_Utils.Dish_Washer_On(id1, 24, 'on', datetimeOn)
    id2 = GetState.Get_Recent_ID() + 1
    Event_Utils.Dish_Washer_Off(id2, 24, 'off', offTime)
    Event_Utils.Dish_Washer_Water(water_id, 24, 'dishwasher', 6, dateWater)

    return render_template('layout.html', FD=FD, BD=BD, GD=GD, MBOH=MBOH, B2OH=B2OH, B3OH=B3OH, LROH=LROH, KOH=KOH, Bath1OH=Bath1OH, Bath2OH=Bath2OH, threshold=int(threshold), inside=int(inside), outside=int(outside))


@app.route('/runClothesWasherAndDryer/', methods=['GET', 'POST'])
def RunClothesWasherAndDryer():
    '''
    This function is a simulated event that washes and drys a load of clothes
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    MBOH = GetState.Master_Bedroom_Overhead_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    LROH = GetState.Living_Room_Overhead_State()
    KOH = GetState.Kitchen_Overhead_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()

    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()

    id1 = GetState.Get_Recent_ID() + 1
    water_id = GetState.Get_Recent_Water_ID() + 1
    onTime = datetime.now().time()
    dateWater = date.today()
    datetimeOn = datetime.combine(dateWater, onTime)
    time_change = timedelta(minutes=45)
    offTime = datetimeOn + time_change

    Event_Utils.Clothes_Washer_On(id1, 13, 'on', datetimeOn)
    id2 = GetState.Get_Recent_ID() + 1
    Event_Utils.Clothes_Washer_Off(id2, 13, 'off', offTime)
    Event_Utils.Clothes_Washer_Water(water_id, 13, 'clotheswasher', 20, dateWater)

    # time_change = timedelta(minutes=45)
    # onTime2 = offTime + time_change
    id3 = GetState.Get_Recent_ID() + 1
    Event_Utils.Clothes_Dryer_On(id3, 14, 'on', offTime)
    time_change = timedelta(minutes=30)
    offTime2 = offTime + time_change
    id4 = GetState.Get_Recent_ID() + 1
    Event_Utils.Clothes_Dryer_On(id4, 14, 'off', offTime2)

    return render_template('layout.html', FD=FD, BD=BD, GD=GD, MBOH=MBOH, B2OH=B2OH, B3OH=B3OH, LROH=LROH, KOH=KOH, Bath1OH=Bath1OH, Bath2OH=Bath2OH, threshold=int(threshold), inside=int(inside), outside=int(outside))


@app.route('/layoutFD/', methods=['GET', 'POST'])
def FDControls():
    '''
    This function is a simulated event to show what changes on the UI when a door or window open or closed
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    FD = GetState.Front_Door_State()
    BD = GetState.Back_Door_State()
    GD = GetState.Garage_Door_State()

    MBOH = GetState.Master_Bedroom_Overhead_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    LROH = GetState.Living_Room_Overhead_State()
    KOH = GetState.Kitchen_Overhead_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()

    threshold = GetState.Threshold_State()
    inside = GetState.Inside_State()
    outside = GetState.Outside_State()

    id1 = GetState.Get_Recent_ID() + 1
    # water_id = GetState.Get_Recent_Water_ID() + 1
    onTime = datetime.now().time()
    dateWater = date.today()
    datetimeOn = datetime.combine(dateWater, onTime)
    time_change = timedelta(minutes=45)
    offTime = datetimeOn + time_change

    # Event_Utils.Clothes_Washer_On(id1,13,'on',datetimeOn)
    id2 = GetState.Get_Recent_ID() + 1
    # Event_Utils.Clothes_Washer_Off(id2,13,'off',offTime)
    # Event_Utils.Clothes_Washer_Water(water_id,13,'clotheswasher',20,dateWater)

    FDtest = request.form["device-one"]
    if FDtest == "Close":
        FD = "open"
        id = GetState.Get_Recent_Door_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Front_Door_Open(id, 1, "open", time)
    elif FDtest == "Open":
        FD = "close"
        id = GetState.Get_Recent_Door_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Front_Door_Close(id, 1, "close", time)

    return render_template('layout.html', FD=FD, BD=BD, GD=GD, MBOH=MBOH, B2OH=B2OH, B3OH=B3OH, LROH=LROH, KOH=KOH, Bath1OH=Bath1OH, Bath2OH=Bath2OH, threshold=int(threshold), inside=int(inside), outside=int(outside))


@app.route('/chart')
def chart():
    '''
    This function is what occurs when the 'chart page' is loaded
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''
    try:
        power = DBRead.Get_Monthly_Data_For_Yearly_Chart()[0]
        labels1 = [row[0] for row in power]
        values1 = [row[1] for row in power]
        water = DBRead.Get_Monthly_Data_For_Yearly_Chart()[1]
        values2 = [row[1] for row in water]

        powerlist = []
        waterlist = []
        totallist = []

        all = []

        for i in values1:
            power_cost = i * .12
            powerlist.append(power_cost)
        for j in values2:
            water_cost = j / 100 * 2.52
            waterlist.append(water_cost)
        for k in range(0, len(powerlist)):
            total = powerlist[k] + waterlist[k]
            totallist.append(total)

        for l in range(0, len(totallist)):
            temp = [labels1[l], values2[l], "$" + str(round(waterlist[l], 2)), values1[l], "$"+str(
                round(powerlist[l], 2)), "$"+str(round(totallist[l], 2))]
            all.append(temp)

        return render_template('chart.html', labels1=labels1, values1=values1, values2=values2, all=all)
    except:
        print("Oops")
    finally:
        # have to clear these values otherwise the data will be appended on each button click
        power.clear()
        labels1.clear()
        values1.clear()
        water.clear()
        values2.clear()
        powerlist.clear()
        waterlist.clear()
        totallist.clear()
        all.clear()
        power_cost = 0
        water_cost = 0
        total = 0
        temp.clear()


@app.route("/yearlychart/", methods=['POST'])
def yearlyData():
    '''
    This function is what occurs when the yearly chart button is selected
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''
    try:
        power = DBRead.Get_Monthly_Data_For_Yearly_Chart()[0]
        labels1 = [row[0] for row in power]
        values1 = [row[1] for row in power]
        water = DBRead.Get_Monthly_Data_For_Yearly_Chart()[1]
        values2 = [row[1] for row in water]

        powerlist = []
        waterlist = []
        totallist = []

        all = []

        for i in values1:
            power_cost = i * .12
            powerlist.append(power_cost)
        for j in values2:
            water_cost = j / 100 * 2.52
            waterlist.append(water_cost)
        for k in range(0, len(powerlist)):
            total = powerlist[k] + waterlist[k]
            totallist.append(total)

        for l in range(0, len(totallist)):
            temp = [labels1[l], values2[l], "$" + str(round(waterlist[l], 2)), values1[l], "$"+str(
                round(powerlist[l], 2)), "$"+str(round(totallist[l], 2))]
            all.append(temp)

        return render_template('chart.html', labels1=labels1, values1=values1, values2=values2, all=all)
    except:
        print("Oops")
    finally:
        power.clear()
        labels1.clear()
        values1.clear()
        water.clear()
        values2.clear()
        powerlist.clear()
        waterlist.clear()
        totallist.clear()
        all.clear()
        power_cost = 0
        water_cost = 0
        total = 0
        temp.clear()


@app.route("/monthlychart/", methods=['GET', 'POST'])
def monthlyData():
    '''
    This function is what occurs when a month is selected and the monthly chart button is clicked
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''
    try:
        month = request.form
        selection = month['Month']
        if selection == 'January':
            param = '01'
        elif selection == 'Febuary':
            param = '02'
        elif selection == 'March':
            param = '03'
        elif selection == 'April':
            param = '04'
        elif selection == 'May':
            param = '05'
        elif selection == 'June':
            param = '06'
        elif selection == 'July':
            param = '07'
        elif selection == 'August':
            param = '08'
        elif selection == 'September':
            param = '09'
        elif selection == 'October':
            param = '10'
        elif selection == 'November':
            param = '11'
        elif selection == 'December':
            param = '07'

        power = DBRead.Get_Weekly_Data_For_Monthly_Chart(param)[0]
        labels1 = [row[0] for row in power]
        values1 = [row[1] for row in power]
        water = DBRead.Get_Weekly_Data_For_Monthly_Chart(param)[1]
        values2 = [row[1] for row in water]

        powerlist = []
        waterlist = []
        totallist = []

        all = []

        for i in values1:
            power_cost = i * .12
            powerlist.append(power_cost)
        for j in values2:
            water_cost = j / 100 * 2.52
            waterlist.append(water_cost)
        for k in range(0, len(powerlist)):
            total = powerlist[k] + waterlist[k]
            totallist.append(total)

        for l in range(0, len(totallist)):
            temp = [labels1[l], values2[l], "$" + str(round(waterlist[l], 2)), values1[l], "$"+str(
                round(powerlist[l], 2)), "$"+str(round(totallist[l], 2))]
            all.append(temp)

        return render_template('chart2.html', labels1=labels1, values1=values1, values2=values2, all=all, selection=selection)
    except:
        print("Oops")
    finally:
        month = ''
        selection = ''
        param = ''
        power.clear()
        labels1.clear()
        values1.clear()
        water.clear()
        values2.clear()
        powerlist.clear()
        waterlist.clear()
        totallist.clear()
        all.clear()
        power_cost = 0
        water_cost = 0
        total = 0
        # temp.clear()


@app.route('/devices', methods=["POST", "GET"])
def devices():
    '''
    This function is what occurs when the 'devices page' is loaded
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    return render_template('devices.html', MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesMBOH/', methods=["POST", "GET"])
def MasterBedroomOverhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR MASTER BEDROOM OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    MBOHtest = request.form["device-one"]
    if MBOHtest == "Off":
        MBOH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Overhead_Light_On(id, 1, "on", time)
    elif MBOHtest == "On":
        MBOH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Overhead_Light_Off(id, 1, "off", time)

    return render_template('devices.html', MBOH=MBOH, MBOHtest=MBOHtest, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesMBL1/', methods=["POST", "GET"])
def MasterBedroomLamp1():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR MASTER BEDROOM LAMP 1 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    MBL1test = request.form["device-two"]
    if MBL1test == "Off":
        MBL1 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Lamp_1_On(id, 4, "on", time)
    elif MBL1test == "On":
        MBL1 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Lamp_1_Off(id, 4, "off", time)

    return render_template('devices.html', MBL1=MBL1, MBL1test=MBL1test, MBOH=MBOH, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesMBL2/', methods=["POST", "GET"])
def MasterBedroomLamp2():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR MASTER BEDROOM LAMP 2 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    MBL2test = request.form["device-three"]
    if MBL2test == "Off":
        MBL2 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Lamp_2_On(id, 5, "on", time)
    elif MBL2test == "On":
        MBL2 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Master_Bedroom_Lamp_2_Off(id, 5, "off", time)

    return render_template('devices.html', MBL2=MBL2, MBL2test=MBL2test, MBOH=MBOH, MBL1=MBL1, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesMBTV/', methods=["POST", "GET"])
def MasterBedroomTv():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR MASTER BEDROOM TV BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    MBTVtest = request.form["device-four"]
    if MBTVtest == "Off":
        MBTV = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_Tv_On(id, 10, "on", time)
    elif MBTVtest == "On":
        MBTV = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_Tv_Off(id, 10, "off", time)

    return render_template('devices.html', MBTV=MBTV, MBTVtest=MBTVtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB2OH/', methods=["POST", "GET"])
def Bedroom2Overhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 2 OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B2OHtest = request.form["device-five"]
    if B2OHtest == "Off":
        B2OH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_Tv_On(id, 2, "on", time)
    elif B2OHtest == "On":
        B2OH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_Tv_Off(id, 2, "off", time)

    return render_template('devices.html', B2OH=B2OH, B2OHtest=B2OHtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB2L1/', methods=["POST", "GET"])
def Bedroom2Lamp1():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 2 LAMP 1 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B2L1test = request.form["device-six"]
    if B2L1test == "Off":
        B2L1 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Lamp_1_On(id, 6, "on", time)
    elif B2L1test == "On":
        B2L1 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Lamp_1_Off(id, 6, "off", time)

    return render_template('devices.html', B2L1=B2L1, B2L1test=B2L1test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB2L2/', methods=["POST", "GET"])
def Bedroom2Lamp2():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 2 LAMP 2 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B2L2test = request.form["device-seven"]
    if B2L2test == "Off":
        B2L2 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Lamp_2_On(id, 7, "on", time)
    elif B2L2test == "On":
        B2L2 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Lamp_2_Off(id, 7, "off", time)

    return render_template('devices.html', B2L2=B2L2, B2L2test=B2L2test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB3OH/', methods=["POST", "GET"])
def Bedroom3Overhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 3 OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B3OHtest = request.form["device-eight"]
    if B3OHtest == "Off":
        B3OH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Overhead_Light_On(id, 3, "on", time)
    elif B3OHtest == "On":
        B3OH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_2_Overhead_Light_Off(id, 3, "off", time)

    return render_template('devices.html', B3OH=B3OH, B3OHtest=B3OHtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB3L1/', methods=["POST", "GET"])
def Bedroom3Lamp1():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 3 LAMP 1 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B3L1test = request.form["device-nine"]
    if B3L1test == "Off":
        B3L1 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_3_Lamp_1_On(id, 8, "on", time)
    elif B3L1test == "On":
        B3L1 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_3_Lamp_1_Off(id, 8, "off", time)

    return render_template('devices.html', B3L1=B3L1, B3L1test=B3L1test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesB3L2/', methods=["POST", "GET"])
def Bedroom3Lamp2():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BEDROOM 3 LAMP 2 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    B3L2test = request.form["device-ten"]
    if B3L2test == "Off":
        B3L2 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_3_Lamp_2_On(id, 9, "on", time)
    elif B3L2test == "On":
        B3L2 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bedroom_3_Lamp_2_Off(id, 9, "off", time)

    return render_template('devices.html', B3L2=B3L2, B3L2test=B3L2test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesBath1OH/', methods=["POST", "GET"])
def Bathroom1Overhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BATHROOM 1 OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    Bath1OHtest = request.form["device-eleven"]
    if Bath1OHtest == "Off":
        Bath1OH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_1_Overhead_Light_On(id, 32, "on", time)
    elif Bath1OHtest == "On":
        Bath1OH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_1_Overhead_Light_Off(id, 32, "off", time)

    return render_template('devices.html', Bath1OH=Bath1OH, Bath1OHtest=Bath1OHtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesBath1EF/', methods=["POST", "GET"])
def Bathroom1ExhaustFan():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BATHROOM 1 EXHAUST FAN BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    Bath1EFtest = request.form["device-twelve"]
    if Bath1EFtest == "Off":
        Bath1EF = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_1_Exhaust_Fan_On(id, 34, "on", time)
    elif Bath1EFtest == "On":
        Bath1EF = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_1_Exhaust_Fan_Off(id, 34, "off", time)

    return render_template('devices.html', Bath1EF=Bath1EF, Bath1EFtest=Bath1EFtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesBath2OH/', methods=["POST", "GET"])
def Bathroom2Overhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BATHROOM 2 OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    Bath2OHtest = request.form["device-thirteen"]
    if Bath2OHtest == "Off":
        Bath2OH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_2_Overhead_Light_On(id, 33, "on", time)
    elif Bath2OHtest == "On":
        Bath2OH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_2_Overhead_Light_Off(id, 33, "off", time)

    return render_template('devices.html', Bath2OH=Bath2OH, Bath2OHtest=Bath2OHtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesBath2EF/', methods=["POST", "GET"])
def Bathroom2ExhaustFan():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR BATHROOM 2 EXHAUST FAN BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    Bath2EFtest = request.form["device-fourteen"]
    if Bath2EFtest == "Off":
        Bath2EF = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_2_Exhaust_Fan_On(id, 35, "on", time)
    elif Bath2EFtest == "On":
        Bath2EF = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Bathroom_2_Exhaust_Fan_Off(id, 35, "off", time)

    return render_template('devices.html', Bath2EF=Bath2EF, Bath2EFtest=Bath2EFtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesGD1/', methods=["POST", "GET"])
def GarageDoor1():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR GARAGE DOOR 1 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    GD1test = request.form["device-fifteen"]
    if GD1test == "Off":
        GD1 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Garage_Door_1_On(id, 11, "on", time)
    elif GD1test == "On":
        GD1 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Garage_Door_1_Off(id, 11, "off", time)

    return render_template('devices.html', GD1=GD1, GD1test=GD1test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesGD2/', methods=["POST", "GET"])
def GarageDoor2():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR GARAGE DOOR 2 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    GD2test = request.form["device-sixteen"]
    if GD2test == "Off":
        GD2 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Garage_Door_2_On(id, 12, "on", time)
    elif GD2test == "On":
        GD2 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Garage_Door_2_Off(id, 12, "off", time)

    return render_template('devices.html', GD2=GD2, GD2test=GD2test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesLROH/', methods=["POST", "GET"])
def LivingRoomOverhead():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR LIVING ROOM OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    LROHtest = request.form["device-seventeen"]
    if LROHtest == "Off":
        LROH = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Overhead_Light_On(id, 15, "on", time)
    elif LROHtest == "On":
        LROH = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Overhead_Light_Off(id, 15, "off", time)

    return render_template('devices.html', LROH=LROH, LROHtest=LROHtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesLRL1/', methods=["POST", "GET"])
def LivingRoomLamp1():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR LIVING ROOM LAMP 1 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    LRL1test = request.form["device-eighteen"]
    if LRL1test == "Off":
        LRL1 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Lamp_1_On(id, 16, "on", time)
    elif LRL1test == "On":
        LRL1 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Lamp_1_Off(id, 16, "off", time)

    return render_template('devices.html', LRL1=LRL1, LRL1test=LRL1test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesLRL2/', methods=["POST", "GET"])
def LivingRoomLamp2():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR LIVING ROOM LAMP 2 BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    LRL2test = request.form["device-nineteen"]
    if LRL2test == "Off":
        LRL2 = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Lamp_2_On(id, 17, "on", time)
    elif LRL2test == "On":
        LRL2 = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Lamp_2_Off(id, 17, "off", time)

    return render_template('devices.html', LRL2=LRL2, LRL2test=LRL2test, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesLRTV/', methods=["POST", "GET"])
def LivingRoomTv():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR LIVING ROOM TV BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    LRTVtest = request.form["device-twenty"]
    if LRTVtest == "Off":
        LRTV = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Tv_On(id, 18, "on", time)
    elif LRTVtest == "On":
        LRTV = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Living_Room_Tv_Off(id, 18, "off", time)

    return render_template('devices.html', LRTV=LRTV, LRTVtest=LRTVtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesHVAC/', methods=["POST", "GET"])
def HVAC():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR HVAC BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    HVACtest = request.form["device-twentyone"]
    if HVACtest == "Off":
        HVAC = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.HVAC_On(id, 25, "on", time)
    elif HVACtest == "On":
        HVAC = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.HVAC_Off(id, 25, "off", time)

    return render_template('devices.html', HVAC=HVAC, HVACtest=HVACtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, KOL=KOL, stove=stove, oven=oven, micro=micro)


@app.route('/devicesKOL/', methods=["POST", "GET"])
def KOL():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR KITCHEN OVERHEAD BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    KOLtest = request.form["device-twentytwo"]
    if KOLtest == "Off":
        KOL = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Kitchen_Overhead_Light_On(id, 19, "on", time)
    elif KOLtest == "On":
        KOL = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Kitchen_Overhead_Light_Off(id, 19, "off", time)

    return render_template('devices.html', KOL=KOL, KOLtest=KOLtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, stove=stove, oven=oven, micro=micro)


@app.route('/devicesStove/', methods=["POST", "GET"])
def Stove():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR STOVE BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    oven = GetState.Oven_State()
    micro = GetState.Microwave_State()

    stovetest = request.form["device-twentyfive"]
    print(stovetest)
    if stovetest == "Off":
        stove = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Stove_On(id, 20, "on", time)
    elif stovetest == "On":
        stove = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Stove_Off(id, 20, "off", time)

    return render_template('devices.html', stove=stove, stovetest=stovetest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, oven=oven, micro=micro)


@app.route('/devicesOven/', methods=["POST", "GET"])
def oven():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR OVEN BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    micro = GetState.Microwave_State()

    oventest = request.form["device-twentysix"]
    if oventest == "Off":
        oven = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Oven_On(id, 21, "on", time)
    elif oventest == "On":
        oven = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Oven_Off(id, 21, "off", time)

    return render_template('devices.html', oven=oven, oventest=oventest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, micro=micro)


@app.route('/devicesMicrowave/', methods=["POST", "GET"])
def microwave():
    '''
    This function is what occurs when the 'devices page' is loaded
    FOR MICROWAVE BUTTON CLICK
    Params:
        None
    Returns:
        the rendered template with each on screen value passed to the front end.
    '''

    MBOH = GetState.Master_Bedroom_Overhead_State()
    MBL1 = GetState.Master_Bedroom_Lamp_1_State()
    MBL2 = GetState.Master_Bedroom_Lamp_2_State()
    MBTV = GetState.Master_Bedroom_TV_State()
    B2OH = GetState.Bedroom2_Overhead_State()
    B2L1 = GetState.Bedroom2_Lamp_1_State()
    B2L2 = GetState.Bedroom2_Lamp_2_State()
    B3OH = GetState.Bedroom3_Overhead_State()
    B3L1 = GetState.Bedroom3_Lamp_1_State()
    B3L2 = GetState.Bedroom3_Lamp_2_State()
    Bath1OH = GetState.Bathroom1_Overhead_State()
    Bath1EF = GetState.Bathroom1_Exhaust_Fan_State()
    Bath2OH = GetState.Bathroom2_Overhead_State()
    Bath2EF = GetState.Bathroom2_Exhaust_Fan_State()
    GD1 = GetState.Garage_Door_Power_1_State()
    GD2 = GetState.Garage_Door_Power_2_State()
    LROH = GetState.Living_Room_Overhead_State()
    LRL1 = GetState.Living_Room_Lamp_1_State()
    LRL2 = GetState.Living_Room_Lamp_2_State()
    LRTV = GetState.Living_Room_TV_State()
    HVAC = GetState.HVAC_State()
    KOL = GetState.Kitchen_Overhead_State()
    stove = GetState.Stove_State()
    oven = GetState.Oven_State()

    microtest = request.form["device-twentyseven"]
    if microtest == "Off":
        micro = "on"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Microwave_On(id, 22, "on", time)
    elif microtest == "On":
        micro = "off"
        id = GetState.Get_Recent_ID() + 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Event_Utils.Microwave_Off(id, 22, "off", time)

    return render_template('devices.html', micro=micro, microtest=microtest, MBOH=MBOH, MBL1=MBL1, MBL2=MBL2, MBTV=MBTV, B2OH=B2OH, B2L1=B2L1, B2L2=B2L2, B3OH=B3OH, B3L1=B3L1, B3L2=B3L2, Bath1OH=Bath1OH, Bath1EF=Bath1EF, Bath2OH=Bath2OH, Bath2EF=Bath2EF, GD1=GD1, GD2=GD2, LROH=LROH, LRL1=LRL1, LRL2=LRL2, LRTV=LRTV, HVAC=HVAC, KOL=KOL, stove=stove, oven=oven)

# More flask stuff
if __name__ == '__main__':
    app.run()

# finally done :)

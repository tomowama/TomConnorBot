import utils 
import activity
import birthdays
import asyncio
import json

async def everyMinute():
    while True:
        print("looping")
        compareDates()
        await asyncio.sleep(60)

# open data.json and get the current date
# compare the current date to datetime now
# if the dates are different, update the currentDate in data.json
# check birthdays
# if the dates are the same, do nothing
def compareDates():
    print("comparing dates")
    data = utils.openDataJSON()
    currentDate = data["currentDate"]
    now = utils.getCurrentDateTime()
    nowDate = utils.convertDateTimeToDateString(now)
    if (currentDate != nowDate):
        print("updating stored date")
        updateCurrentDate(nowDate)
        todaysBirthdays = birthdays.getAllBirthdaysWithDate(now)
        print("sending birthday messages")
        sendBirthdayMessages(todaysBirthdays)
    
def updateCurrentDate(nowDate: str):
    data = utils.openDataJSON()
    data["currentDate"] = nowDate
    utils.writeDataJSON(data)

def sendBirthdayMessages(todaysBirthdays):
    for birthday in todaysBirthdays:
        birthdayMessage = f"Happy Birthday {birthday}!"
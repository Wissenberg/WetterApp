from pyowm import OWM
from tkinter import *
from datetime import datetime
import re
import mysql.connector

class Settings:
    #Settings for the api request
    apiKey = "98c9e6829a2efe0ee5a3d10d4d294d59"
    lat = 51.450832
    lon = 7.013056
    city = "Essen"

    #Settings for the ui
    bg = "Grey25"
    bgLightGrey = "#848484"
    fg = "white"
    fontDefault = ('arial', 20)
    fontData = ('arial', 15)
    defaultLabelLenght = 300
    defaultLabelHeight = 30

    #Settings for the db mapper
    user = "root"
    passwd = "test123"
    port = 3306
    ipAddress = "127.0.0.1"
    dbName = "weather_db"

    @staticmethod
    def getUrl():
        return Settings.url
    

class UiMain:
    def __init__(self):
        self.tkWindow = Tk()
        self.tkWindow.title("Wetter App") # Title of the app
        self.tkWindow.geometry("950x800")# Size of the window
        self.tkWindow.configure(bg=Settings.bg)# Background of the window
        self.tkWindow.resizable(0, 0)# False
        self.uiObjects()
    
    def uiObjects(self):
#----------------------------------------------------------Current-------------------------------------------------------------------------------------------------------------------
        self.currentFrame = Frame(master = self.tkWindow, bg = Settings.bgLightGrey)
        self.currentFrame.place(x = 5, y = 5, height = 170, width = 940)

        self.labelCurrent = Label(master = self.currentFrame, bg = Settings.bgLightGrey, fg = Settings.fg, text = "Aktuell", anchor = "w",
            font = Settings.fontDefault)
        self.labelCurrent.place(x = 400, y = 10, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelCurrentTemp = Label(master = self.currentFrame, bg = Settings.bgLightGrey, fg = Settings.fg, text = "Temp", anchor = "w",
            font = Settings.fontData)
        self.labelCurrentTemp.place(x = 400, y = 50, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelCurrentWind = Label(master = self.currentFrame, bg = Settings.bgLightGrey, fg = Settings.fg, text = "Wind", anchor = "w",
            font = Settings.fontData)
        self.labelCurrentWind.place(x = 400, y = 90, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelCurrentHumidity = Label(master = self.currentFrame, bg = Settings.bgLightGrey, fg = Settings.fg, text = "Feuchte", anchor = "w",
            font = Settings.fontData)
        self.labelCurrentHumidity.place(x = 400, y = 130, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelCurrentRain = Label(master = self.currentFrame, bg = Settings.bgLightGrey, fg = Settings.fg, text = "Rain", anchor = "w",
            font = Settings.fontData)
        self.labelCurrentRain.place(x = 10, y = 170, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 2-------------------------------------------------------------------------------------------------------------------

        self.labelDay2 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Morgen:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay2.place(x = 10, y = 300, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay2Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp TW", anchor = "w",
            font = Settings.fontData)
        self.labelDay2Temp.place(x = 10, y = 340, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay2Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind TW", anchor = "w",
            font = Settings.fontData)
        self.labelDay2Wind.place(x = 10, y = 380, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay2Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte TW", anchor = "w",
            font = Settings.fontData)
        self.labelDay2Humidity.place(x = 10, y = 420, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay2Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain TW", anchor = "w",
            font = Settings.fontData)
        self.labelDay2Rain.place(x = 10, y = 460, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 3-------------------------------------------------------------------------------------------------------------------
        self.labelDay3 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Übermorgen:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay3.place(x = 330, y = 300, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay3Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp 3", anchor = "w",
            font = Settings.fontData)
        self.labelDay3Temp.place(x = 330, y = 340, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay3Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind 3", anchor = "w",
            font = Settings.fontData)
        self.labelDay3Wind.place(x = 330, y = 380, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay3Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte 3", anchor = "w",
            font = Settings.fontData)
        self.labelDay3Humidity.place(x = 330, y = 420, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay3Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain 3", anchor = "w",
            font = Settings.fontData)
        self.labelDay3Rain.place(x = 330, y = 460, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 4-------------------------------------------------------------------------------------------------------------------

        self.labelDay4 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Forecast 4:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay4.place(x = 650, y = 300, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay4Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp 4", anchor = "w",
            font = Settings.fontData)
        self.labelDay4Temp.place(x = 650, y = 340, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay4Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind 4", anchor = "w",
            font = Settings.fontData)
        self.labelDay4Wind.place(x = 650, y = 380, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay4Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte 4", anchor = "w",
            font = Settings.fontData)
        self.labelDay4Humidity.place(x = 650, y = 420, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay4Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain 4", anchor = "w",
            font = Settings.fontData)
        self.labelDay4Rain.place(x = 650, y = 460, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 5-------------------------------------------------------------------------------------------------------------------
        self.labelDay5 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Forecast 5:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay5.place(x = 10, y = 520, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay5Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp 5", anchor = "w",
            font = Settings.fontData)
        self.labelDay5Temp.place(x = 10, y = 560, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay5Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind 5", anchor = "w",
            font = Settings.fontData)
        self.labelDay5Wind.place(x = 10, y = 600, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay5Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte 5", anchor = "w",
            font = Settings.fontData)
        self.labelDay5Humidity.place(x = 10, y = 640, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay5Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain 5", anchor = "w",
            font = Settings.fontData)
        self.labelDay5Rain.place(x = 10, y = 680, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 6-------------------------------------------------------------------------------------------------------------------

        self.labelDay6 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Forecast 6:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay6.place(x = 330, y = 520, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay6Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp 6", anchor = "w",
            font = Settings.fontData)
        self.labelDay6Temp.place(x = 330, y = 560, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay6Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind 6", anchor = "w",
            font = Settings.fontData)
        self.labelDay6Wind.place(x = 330, y = 600, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay6Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte 6", anchor = "w",
            font = Settings.fontData)
        self.labelDay6Humidity.place(x = 330, y = 640, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay6Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain 6", anchor = "w",
            font = Settings.fontData)
        self.labelDay6Rain.place(x = 330, y = 680, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

#----------------------------------------------------------Day 7-------------------------------------------------------------------------------------------------------------------

        self.labelDay7 = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Forecast 7:", anchor = "w",
            font = Settings.fontDefault)
        self.labelDay7.place(x = 650, y = 520, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay7Temp = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Temp 7", anchor = "w",
            font = Settings.fontData)
        self.labelDay7Temp.place(x = 650, y = 560, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)
        
        self.labelDay7Wind = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Wind 7", anchor = "w",
            font = Settings.fontData)
        self.labelDay7Wind.place(x = 650, y = 600, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay7Humidity = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Feuchte 7", anchor = "w",
            font = Settings.fontData)
        self.labelDay7Humidity.place(x = 650, y = 640, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

        self.labelDay7Rain = Label(master = self.tkWindow, bg = Settings.bg, fg = Settings.fg, text = "Rain 7", anchor = "w",
            font = Settings.fontData)
        self.labelDay7Rain.place(x = 650, y = 680, width = Settings.defaultLabelLenght, height = Settings.defaultLabelHeight)

class WeatherDataMapping:
    def __init__(self):
        self.dbConnect = mysql.connector.connect(host = Settings.ipAddress, port = Settings.port, user = Settings.user, passwd = Settings.passwd, database = Settings.dbName) 
        self.pointerDB = self.dbConnect.cursor()
    
    def getWeatherValues(self,cityName, time, forecastTime):
        data = []
        self.pointerDB.execute(f"SELECT temperature, wind, humidity, rain FROM weathervalues INNER JOIN city ON (city_id = city.id) WHERE city.name = '{cityName}' and captured = '{time}' and forecastTime = '{forecastTime}';")
        for x in self.pointerDB.fetchone():
            data.append(x)
        return data

    def getCityName(self, cityName):
        city = []
        self.pointerDB.execute(f"SELECT name, lat, lon FROM city WHERE name = '{cityName}';")
        for x in self.pointerDB.fetchone():
            city.append(x)
        return city

    def getCitys(self, cityName):
        city = []
        self.pointerDB.execute(f"SELECT * FROM city WHERE name = '{cityName}';")
        for x in self.pointerDB.fetchone():
            city.append(x)
        return city

    def setWeatherData(self, time, forecastTime, cityName, temperature, wind, humidity, rain):
        self.pointerDB.execute(f"INSERT INTO weathervalues (captured, forecastTime, city_id, temperature, wind, humidity, rain) VALUES ('{time}', '{forecastTime}', (SELECT id FROM city WHERE name = '{cityName}'), '{temperature}', '{wind}', '{humidity}', {rain});")
        self.dbConnect.commit()
    
    def setCountry(self,countryNameEng, countryNameGer,shortedName):
        self.pointerDB.execute(f"INSERT INTO country(shorted, name_eng, name_ger) VALUES ({shortedName}, {countryNameEng}, {countryNameGer});")
        self.pointerDB.commit()

    def setStateName(self, stateName, countryName):
        self.pointerDB.execute(f"INSERT INTO state_name (name, country_id) VALUES ({stateName}, SELECT id FROM country WHERE name = {countryName});")
        self.pointerDB.commit()
    
    def setCityName(self, cityName, stateName, lat, lon):
        self.pointerDB.execute(f"INSERT INTO city (name, state_id, lat, lon) VALUES ({cityName}, SELECT id FROM state_name WHERE name = {stateName}, lat, lon);")
        self.pointerDB.commit()        
        

class WeatherData:
    def __init__(self):
        self.owm = OWM(Settings.apiKey)
        self.owmManager = self.owm.weather_manager()
        self.weatherForecast = []
        self.weatherCurrent = []
        self.processedWeatherDataCurrent = []
        self.processedWeatherDataForecast = []

    def getDataFromOwm(self, dbMapper, city):
        data = dbMapper.getCityName(city)
        lat = data[1]
        lon = data[2]
        self.observation = self.owmManager.one_call(lat, lon)
    
    def processWeatherDataCurrent(self):
            self.weatherCurrent.append(str(self.observation.current.temperature('celsius').get('temp',None)))
            self.weatherCurrent.append(str(self.observation.current.wind().get('speed', 0)))
            self.weatherCurrent.append(str(self.observation.current.humidity))
            self.weatherCurrent.append(str(self.observation.current.rain))

    def processWeatherDataForecast(self):
        for x in range (0,7):
            self.weatherForecast.append(str(self.observation.forecast_daily[x].temperature('celsius').get('day',None)))
            self.weatherForecast.append(str(self.observation.forecast_daily[x].wind().get('speed', 0)))
            self.weatherForecast.append(str(self.observation.forecast_daily[x].humidity))
            self.weatherForecast.append(str(self.observation.forecast_daily[x].rain.get('all',None)))
            self.weatherForecast.append("|")
    
    def getCurrentData(self, dbMapper, daysUnprocessed):
        mainController.setCurrentDataToDB()
        currentData = dbMapper.getWeatherValues(Settings.city, daysUnprocessed[0], daysUnprocessed[0])
        self.processedWeatherDataCurrent.append(f"Temperatur: {currentData[0]}°C")
        self.processedWeatherDataCurrent.append(f"Wind: {currentData[1]}m/s")
        self.processedWeatherDataCurrent.append(f"Feuchtigkeit: {currentData[2]}%")
        if currentData[3] == '{}' or currentData[3] == "None" or currentData[3] == 0 or currentData[3] == "0":
            self.processedWeatherDataCurrent.append(f"Regen: Nein")
        else:
            self.processedWeatherDataCurrent.append(f"Regen: Ja")
    
    def getForecastData(self, day, dbMapper, daysUnprocessed, daysProcessed):
        forecastData = dbMapper.getWeatherValues(Settings.city, daysUnprocessed[0], daysProcessed[day])
        self.processedWeatherDataForecast.append(f"Tag: {day}")
        self.processedWeatherDataForecast.append(f"Temperatur: {forecastData[0]}°C")
        self.processedWeatherDataForecast.append(f"Wind: {forecastData[1]}m/s")
        self.processedWeatherDataForecast.append(f"Feuchtigkeit: {forecastData[2]}%")
        if forecastData[3] == '{}' or forecastData[3] == 'None':
            self.processedWeatherDataForecast.append("Regen: Nein")
        else:
            self.processedWeatherDataForecast.append("Regen: Ja")
        self.processedWeatherDataForecast.append("|")

    def main(self, dbMapper, daysUnprocessed, daysProcessed):
        self.getDataFromOwm(dbMapper, Settings.city)
        self.processWeatherDataCurrent()
        self.processWeatherDataForecast()
        self.getCurrentData(dbMapper, daysUnprocessed)
        mainController.setForecastDataToDB()
        for x in range (1, 7):
            self.getForecastData(x, dbMapper, daysUnprocessed, daysProcessed)

class Controller:
    def __init__(self):
        self.weatherManager = WeatherData()
        self.uiManager = UiMain()
        self.dbMapper = WeatherDataMapping()
        self.daysUnprocessed = []
        self.daysProcessed = []

        self.now = datetime.now()
        self.daysUnprocessed.append (str(self.now))
        self.today = self.now.timestamp()
        self.secondsOneDay = 86400
        self.suche_1 = "20..."
        self.suche_2 = " ..............."

    def run(self):
        self.constructDate()
        self.weatherManager.main(self.dbMapper, self.daysUnprocessed, self.daysProcessed)
        self.insertDateInUi()
        self.insertDataInUi()
    
    def setCurrentDataToDB(self):
        temp = self.weatherManager.weatherCurrent[0]
        wind = self.weatherManager.weatherCurrent[1]
        humidity = self.weatherManager.weatherCurrent[2]
        if self.weatherManager.weatherCurrent[3] == "{}" or self.weatherManager.weatherCurrent[3] == "None":
            rain = 0
        else:
            rain = 1
        self.dbMapper.setWeatherData(self.daysUnprocessed[0],self.daysUnprocessed[0], Settings.city, temp, wind, humidity, rain)
    
    def setForecastDataToDB(self):
        y = 0
        for x in range(0,35,5):
            temp = self.weatherManager.weatherForecast[x]
            wind = self.weatherManager.weatherForecast[x + 1]
            humidity = self.weatherManager.weatherForecast[x + 2]
            if self.weatherManager.weatherForecast[x + 3] == "{}" or self.weatherManager.weatherForecast[x + 3] == "None":
                rain = 0
            else:
                rain = 1
            self.dbMapper.setWeatherData(self.daysUnprocessed[0],self.daysProcessed[y], Settings.city, temp, wind, humidity, rain)
            y += 1    


    def insertDataInUi(self):
        self.uiManager.labelCurrentTemp.config(text = self.weatherManager.processedWeatherDataCurrent[0])
        self.uiManager.labelCurrentWind.config(text = self.weatherManager.processedWeatherDataCurrent[1])
        self.uiManager.labelCurrentHumidity.config(text = self.weatherManager.processedWeatherDataCurrent[2])
        self.uiManager.labelCurrentRain.config(text = self.weatherManager.processedWeatherDataCurrent[3])

        self.uiManager.labelDay2Temp.config(text = self.weatherManager.processedWeatherDataForecast[1])
        self.uiManager.labelDay2Wind.config(text = self.weatherManager.processedWeatherDataForecast[2])
        self.uiManager.labelDay2Humidity.config(text = self.weatherManager.processedWeatherDataForecast[3])
        self.uiManager.labelDay2Rain.config(text = self.weatherManager.processedWeatherDataForecast[4])

        self.uiManager.labelDay3Temp.config(text = self.weatherManager.processedWeatherDataForecast[7])
        self.uiManager.labelDay3Wind.config(text = self.weatherManager.processedWeatherDataForecast[8])
        self.uiManager.labelDay3Humidity.config(text = self.weatherManager.processedWeatherDataForecast[9])
        self.uiManager.labelDay3Rain.config(text = self.weatherManager.processedWeatherDataForecast[10])

        self.uiManager.labelDay4Temp.config(text = self.weatherManager.processedWeatherDataForecast[13])
        self.uiManager.labelDay4Wind.config(text = self.weatherManager.processedWeatherDataForecast[14])
        self.uiManager.labelDay4Humidity.config(text = self.weatherManager.processedWeatherDataForecast[15])
        self.uiManager.labelDay4Rain.config(text = self.weatherManager.processedWeatherDataForecast[16])

        self.uiManager.labelDay5Temp.config(text = self.weatherManager.processedWeatherDataForecast[19])
        self.uiManager.labelDay5Wind.config(text = self.weatherManager.processedWeatherDataForecast[20])
        self.uiManager.labelDay5Humidity.config(text = self.weatherManager.processedWeatherDataForecast[21])
        self.uiManager.labelDay5Rain.config(text = self.weatherManager.processedWeatherDataForecast[22])

        self.uiManager.labelDay6Temp.config(text = self.weatherManager.processedWeatherDataForecast[25])
        self.uiManager.labelDay6Wind.config(text = self.weatherManager.processedWeatherDataForecast[26])
        self.uiManager.labelDay6Humidity.config(text = self.weatherManager.processedWeatherDataForecast[27])
        self.uiManager.labelDay6Rain.config(text = self.weatherManager.processedWeatherDataForecast[28])

        self.uiManager.labelDay7Temp.config(text = self.weatherManager.processedWeatherDataForecast[31])
        self.uiManager.labelDay7Wind.config(text = self.weatherManager.processedWeatherDataForecast[32])
        self.uiManager.labelDay7Humidity.config(text = self.weatherManager.processedWeatherDataForecast[33])
        self.uiManager.labelDay7Rain.config(text = self.weatherManager.processedWeatherDataForecast[34])
    
    def constructDate(self):
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + self.secondsOneDay)))
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + (self.secondsOneDay * 2))))
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + (self.secondsOneDay * 3))))
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + (self.secondsOneDay * 4))))
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + (self.secondsOneDay * 5))))
        self.daysUnprocessed.append (str(datetime.fromtimestamp(self.today + (self.secondsOneDay * 6))))

        for x in range (0, 7):
            y = re.sub(self.suche_1, "",self.daysUnprocessed[x])
            z = re.sub(self.suche_2,"", y)
            a = z.split("-")
            self.daysProcessed.append(f"{a[1]}.{a[0]}")
        
    def insertDateInUi(self):
        self.uiManager.labelCurrent.config(text = self.daysProcessed[0])
        self.uiManager.labelDay2.config(text = self.daysProcessed[1])
        self.uiManager.labelDay3.config(text = self.daysProcessed[2])
        self.uiManager.labelDay4.config(text = self.daysProcessed[3])
        self.uiManager.labelDay5.config(text = self.daysProcessed[4])
        self.uiManager.labelDay6.config(text = self.daysProcessed[5])
        self.uiManager.labelDay7.config(text = self.daysProcessed[6])

if __name__ == '__main__':
    mainController = Controller()
    mainController.run()
    mainController.uiManager.tkWindow.mainloop()



    
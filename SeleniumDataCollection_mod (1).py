from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains
import csv
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import numpy as np

pm25LocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='PM']/child::sub[text()='2.5']"
pm10LocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='PM']/child::sub[text()='10']"
oLocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='O']"
noLocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='NO']"
soLocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='SO']"
coLocatorXpath = "//div[text()='Daily Data']/following-sibling::ul/child::li[text()='CO']"
yearHeadingsXpath ="//div[@class='historical-yearly-data']/child::table/descendant::tr[@class='year-divider']/child::td[@colspan]"


yearMonthDayGenericXpath = "//tr[@key='$KEY$']/child::td[@class='squares']/descendant::*[@x][@y]"
yearMonthDayAllXpath = "//tr[@key='$KEY$']/child::td[@class='squares']/descendant::*[@x][@y][##]"
monthAvailableCheckXpath = "//tr[@key='$KEY$']/child::td[@class='squares']"

# city = 'delhi'
# station= 'mandir-marg'

city = 'india'
station= 'thiruvananthapuram/plammoodu'



URL = "https://aqicn.org/historical#!city:$CITY$/$STATION$"
URL = URL.replace('$CITY$',city).replace('$STATION$',station)


print(URL)







 
options = Options()  
#options.add_argument("--headless") 
options.add_argument('start-maximized')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')


driver.get(URL)




time.sleep(2)
actions = ActionChains(driver)

actions.move_to_element(driver.find_element_by_xpath(pm10LocatorXpath)).click().perform()

time.sleep(2)

driver.find_element_by_xpath(pm25LocatorXpath).click()

print("Data available for the below years:")
yearList = driver.find_elements_by_xpath(yearHeadingsXpath)

availableYears = []
for webElement in yearList:
    availableYears.append(webElement.text)
        
    
availableYears.sort()

print("Data available for the below years:")
for x in availableYears:    
    print(x)
 
    
monthIndex = dict(
       [
        (0,'00'),
        (1,'01'),
        (2,'02'),
        (3,'03'),
        (4,'04'),
        (5,'05'),
        (6,'06'),
        (7,'07'),
        (8,'08'),
        (9,'09'),
        (10,'10'),
        (11,'11')
       ]
    )
 

monthName = dict(
    [
        (0, "Jan"),
        (1, "Feb"),
        (2, "Mar"),
        (3, "Apr"),
        (4, "May"),
        (5, "Jun"),
        (6, "Jul"),
        (7, "Aug"),
        (8, "Sep"),
        (9, "Oct"),
        (10, "Nov"),
        (11, "Dec")
    ]
)

DATE_LIST=[]
PM_25_LIST=[]
PM_10_LIST=[]
O3_LIST=[]
NO2_LIST=[]
SO2_LIST=[]
CO_LIST=[]







#PM2.5
print("PM2.5")
for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        
      
      
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
        
                  
        for j in range (1,numberOfDays+1):
            
                   
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
            if(valueFromPage == '-'):
                valueFromPage = ''
            
            
            print(valueFromPage)
       
            date = (str(j)+"-"+monthName[i]+"-"+year)
           
            DATE_LIST.append(date)
        
            PM_25_LIST.append(valueFromPage)


            

print(DATE_LIST)


#PM10
print("PM10")
time.sleep(2);
driver.find_element_by_xpath(pm10LocatorXpath).click()


for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
                  
        for j in range (1,numberOfDays+1):
            
                       
           
            
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
            if(valueFromPage == '-'):
                valueFromPage = ''
            
            print(valueFromPage)
               
            PM_10_LIST.append(valueFromPage)

    



#O3
print("O3")
time.sleep(2);
driver.find_element_by_xpath(oLocatorXpath).click()


for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
                  
        for j in range (1,numberOfDays+1):
            
                       
            
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
            
            if(valueFromPage == '-'):
                valueFromPage = ''
            print(valueFromPage)
       
        
            O3_LIST.append(valueFromPage)
            
            
            
#N02
print("NO2")
time.sleep(2);
driver.find_element_by_xpath(noLocatorXpath).click()


for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
                  
        for j in range (1,numberOfDays+1):
            
             
            
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
                
            if(valueFromPage == '-'):
                valueFromPage = ''
                
            print(valueFromPage)
                  
        
            NO2_LIST.append(valueFromPage)            



#S02
print("SO2")
time.sleep(2);
driver.find_element_by_xpath(soLocatorXpath).click()


for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
                  
        for j in range (1,numberOfDays+1):
            
                       
            
            
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
                    
            if(valueFromPage == '-'):
                valueFromPage = ''
                
                
            print(valueFromPage)
                  
        
            SO2_LIST.append(valueFromPage)
            
            
            
    

#C0
print("CO")
time.sleep(2);
driver.find_element_by_xpath(coLocatorXpath).click()


for year in availableYears:
    for i in range (12):
        

        print("Grabbing data for ", monthName[i], year)
        monthYearKey = year + monthIndex[i]
        numberOfDays = len(driver.find_elements_by_xpath(yearMonthDayGenericXpath.replace("$KEY$",monthYearKey)))
                  
        for j in range (1,numberOfDays+1):
            
                       
             
            
            valueFromPage = driver.find_element_by_xpath(yearMonthDayAllXpath.replace("$KEY$",monthYearKey).replace("##",str(j))).text
                  
            if(valueFromPage == '-'):
                valueFromPage = ''
                
                
            print(valueFromPage)
                  
        
            CO_LIST.append(valueFromPage)
            





length = len(DATE_LIST)





                                 
                                 
with open('temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date","PM2.5","PM10","O3","NO2","SO2","CO"])
    for i in range(length):
        writer.writerow([DATE_LIST[i], PM_25_LIST[i],PM_10_LIST[i],O3_LIST[i],NO2_LIST[i],SO2_LIST[i],CO_LIST[i] ])
        

#####Removing Unwanted Rows##########


df = pd.read_csv('temp.csv')



length =len(df.index)

rows_to_be_removed_until=0

for i in range(1,length):
    if (np.isnan(df["PM2.5"][i]) and np.isnan(df["PM10"][i]) and np.isnan(df["O3"][i]) and np.isnan(df["NO2"][i]) and np.isnan(df["SO2"][i]) and np.isnan(df["CO"][i])):
        rows_to_be_removed_until=rows_to_be_removed_until + 1
    else:
        break



df = df.iloc[rows_to_be_removed_until+1: , :]

df.to_csv('temp2.csv')

df = pd.read_csv('temp2.csv')

df.drop(df.columns[[0]], axis = 1, inplace = True)



rows_to_be_removed_until_from_last=0
length =len(df.index)
count=0
for i in range(length-1,1,-1):
    print(i,df["PM2.5"][i],df["PM10"][i],df["O3"][i],df["NO2"][i],df["SO2"][i],df["CO"][i])
    if (np.isnan(df["PM2.5"][i]) and np.isnan(df["PM10"][i]) and np.isnan(df["O3"][i]) and np.isnan(df["NO2"][i]) and np.isnan(df["SO2"][i]) and np.isnan(df["CO"][i])):
        rows_to_be_removed_until_from_last = rows_to_be_removed_until_from_last +1 
    else:
        break
    
    
    
df.drop(df.tail(rows_to_be_removed_until_from_last).index,inplace = True)

outputFileName = city + '_'+ station.replace('/','_') + '_LiveData' +'.csv'

df.to_csv(outputFileName,index=False)





        
        



     
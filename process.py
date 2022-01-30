import datetime

f = open("strings.txt", "r")
allWords = f.read()
list = allWords.replace("\"","").replace("\\n","").replace("\\","").split(",")
day = datetime.datetime(2022,1,31)

x = 0
for i in list:
    print(i + "  " + str(day.year) +"-"+ str(day.month) +"-"+ str(day.day))
    print()
    x+=1
    day += datetime.timedelta(days=1)

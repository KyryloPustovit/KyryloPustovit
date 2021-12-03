import matplotlib.pyplot as plt


#Текст
Text='Текст. Текст... Текст? Текст... Текст! Текст. Текст! Текст? Текст? Текст...'


#Крапка, три крапка, питальні, окличні.
a=0
b=0
c=0
d=0


#Пошук символів
for symbol in Text:
    if symbol==".":
        a=a+1
    elif symbol=="...":
        b=b+1
    elif symbol=="?":
        c=c+1
    elif symbol=="!":
        d=d+1


#Перетворення даних в кординати 
e=[a,b,c,d]
ydata=e
xdata=("крапка", "три крапка", "питальні", "окличні")


#Гістограма
fig=plt.figure(figsize=(6,6))
plt.bar(xdata, ydata, width=0.8, color=['DarkBlue'])
plt.xlabel('Тип речення')
plt.ylabel('Частота')
plt.xticks(xdata)
plt.title('Частота появи реченнь')
plt.savefig('Histogram_Lab#7_task3.png')


plt.show()
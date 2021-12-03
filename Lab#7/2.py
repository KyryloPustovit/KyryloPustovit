import pandas as pd
import pylab
import matplotlib.pyplot as plt



Text='''5G — одна из самых обсуждаемых технологий конца десятилетия. В августе 2019 она достигла пика
 завышенных ожиданий согласно Gartner Hype Cycle for Emerging Technologies. Как и во многих аналогичных 
 случаях, информационное пространство насыщено субъективными оценками и фрагментарными сведениями.
 Постараемся структурировать понимание 5G с точки зрения целей, технологических параметров и пользовательского опыта.'''

symbol_list = list(Text)

a = pd.DataFrame({'symbols': symbol_list})

a = a[a.symbols != ' ']

a['num']=1

a = a.groupby('symbols').sum().sort_values('num', ascending=False) / len(a)

fig = plt.figure(figsize=(20,10))
plt.bar(a.index, a.num, width=0.8, color='DarkBlue')
plt.xlabel('Символ')
plt.ylabel('частота')
plt.xticks(a.index)
plt.title('Частота символів')
plt.savefig('Histogram_Lab#7_task2.png')


plt.show()

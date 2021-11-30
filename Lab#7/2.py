import pylab

filePath = "https://github.com/KyryloPustovit/KyryloPustovit/blob/ffc2329afe1ed50d7cd08ac4dcb474121f5331c9/Lab%237/2.txt"
file1 = open(filePath, "r", encoding='UTF-8').read().lower().split()
print(file1)
symbols = []

for word in file1:
    for symbol in word:
        symbols.append(symbol)  

symbols.sort()
frequency = {}

for item in symbols:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

keys, values = zip(*frequency.items())

pylab.bar(keys, values)
pylab.show()
from random import randint
from Func import *

LENGTH = 10
list = []

for i in range(LENGTH):
    list.append(randint(0, 16))

print("Список:", list)
print("Відсортовавний список:", sort(list))
print("Індекс першого елемента зі значенням 8:", indexOf(8, list))
print("5 найменьших елементів:", getMinFive(list))
print("5 найбільших елементів:", getMaxFive(list))
print("Середне арифметичне:", getAvg(list))
print("Неповторні елементи списку:", getUnique(list))
print("Кількість неунікальних елементів списку:", getNotUniqueCount(list))
print("Зсунутий масив:", shiftList(list))
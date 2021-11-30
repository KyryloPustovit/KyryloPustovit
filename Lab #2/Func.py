"""Швидке сортування"""
def sort(list):
    """Сортування алгоритмом Insertion"""
    for i in range(len(list)):
        j = i
        while (list[j] < list[j-1] and j > 0):
            """Замінити елементи з індексом j и j-1 місцями"""
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
    return sorted(list)

"""Пошук елементу за значенням"""
def indexOf(element, list):
    """Перебір елементів списку"""
    for i in range(len(list)):
        el = list[i]
        if (el == element):
            """Повернення індекса елементу"""
            return i
    """Якщо не знайшли, повернути -1"""
    return -1

"""5 мінімальних елементів"""
def getMinFive(list):
    """Сортування"""
    sorted = sort(list)
    fiveMin = []
    """Записуєм та повертаємо 5 мінімальних елементів"""
    for i in range(0, 5):
        fiveMin.append(sorted[i])
    return fiveMin

"""5 максимальних елементів"""
def getMaxFive(list):
    """Сортування"""
    sorted = sort(list)
    fiveMax = []
    """Записуєм та повертаємо 5 максимальних елементів"""
    for i in range(len(sorted) - 5, len(sorted)):
        fiveMax.append(sorted[i])
    return fiveMax

"""Середне арифметичне"""
def getAvg(list):
    avg = 0
    for i in range(len(list)):
        """Додаємо всі елементи"""
        avg += list[i]
    """Ділимо суму на кількість елементів та повертаємо"""
    avg /= len(list)
    return avg

"""Знаходження унікальних елементів"""
def getUnique(list):
    unique = []
    """Перебір елементів списку"""
    for i in range(len(list)):
        el = list[i]
        """Якщо поточний елемент не записували, то записуємо"""
        if not el in unique:
            unique.append(el)
    return unique

"""Знаходження кількості повторень"""
def getNotUniqueCount(list):
    unique = getUnique(list)
    uniqueLen = len(unique)
    listLen = len(list)
    """Віднімаємо кілкість унікальних елементів від усіх"""
    return listLen - uniqueLen

"""Функція для зсуву списку"""
def shiftList(list):
    length = len(list)
    shifted = [list[length - 1]]
    for i in range(length - 1):
        shifted.append(list[i])
    return shifted

"""Функція знаходження найменшого спільного дільника двох чисел"""
def getLeastComMult(a, b):
    i = min(a, b)
    while True:
        if i%a == 0 and i%b == 0:
            return i
        i += 1
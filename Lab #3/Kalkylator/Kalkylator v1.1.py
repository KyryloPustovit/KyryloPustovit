print("Ноль завершает работу")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        print("Завершение работы")
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("На ноль нельзя делить!")
    else:
        print("Ошибка операции"
              "\nВведите верный знак")

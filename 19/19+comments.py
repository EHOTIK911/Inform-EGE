def f(x,y,p): #Рекурсивная функция, получающая на входе количество камешков в кучке, номер и номер позиции
    if x + y <=20 and p == 3: # Условия при которых после неудачного хода Пети, Ваня выигрывает своим первым ходом
        return True
    else:
        if x + y > 20 and p == 3:
            return False
    return f(x - 1, y,p + 1) or f(x//2, y,p + 1) or f(x,y - 1, p + 1) or f(x,y//2,p + 1) #Возможные варианты попадания в нужный нам ход.

a = []

for i in range(10,50+1): # Цикл поиска наибольшего значения S
    if f(10,i,1): # Рекурсивная функиция получает на вход i - это наше  и 1 - это первая позиция(исходяща позиция)
        a += [i]

print(a)

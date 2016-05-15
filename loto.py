#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import copy
r = list(range(1,91))
#print (r)
class Ticket():
    #wrap = paper() 
    #num = self.g_ticket()
    #ticket = copy.copy(num)
    #wrap = 'jgjglk'
    #num = []
    #ticket = []	
    def __init__(self):
        self.wrap = self._paper()
        #num = self.g_ticket()
        #ticket = copy.copy(num)
        #wrap = 'jgjglk'
        #self.num = sorted(random.sample(range (1,91),15))
        self.num = self._gen()
        #self.num = [8, 10, 14, 18, 29, 33, 35, 41, 46, 53, 58, 67, 73, 74, 85]
        self.ticket = copy.deepcopy(self.num)
        #print (self.wrap)
        return 

    def _paper(self):
        k = random.sample(range(1,10),5)
        k0 = sorted(k)
        k1 = sorted(random.sample(range(10,19),5))
        k2 = sorted(random.sample(range(19,28),5))
        for i in range(5):
            k.append(k1[i])
            k.append(k2[i])
        #print(k0,k1,k2)
        k_c = sorted(k)
        #print (k_c)
        s=''
        index = 0
        for i in range(1,28):
            #n.append(i)
            if i in k_c:
                s = s +('{0['+str(index)+']:3} ')
                index +=1
            else:
                s = s + ('    ')
        return (s)
    def _gen(self):
        num = sorted(random.sample(range (1,91),15))
        return (num)
    def prnt (self):
        print ("-"*35) 
        print(self.wrap[:61].format(self.num))
        print(self.wrap[61:122].format(self.num))
        print(self.wrap[122:].format(self.num))
        print ("-"*35)
        return
    def stress(self,barrel):
        if barrel in self.num:
            #print('y')
            mi = self.num.index(barrel)
            self.ticket.remove(barrel)
            self.num[mi]='  -'
        #else:
            #print ('n')
        #print ("NUM : {}   \nTICKET : {}".format(self.num, self.ticket))
        return 
class Bag():
    def __init__(self):
    	self.barrels = r
    	return
    def getnew(self):
        self.barrel = random.sample(self.barrels,1)[0]
        self.barrels.remove(self.barrel)
        return (self.barrel)

#num = sorted(random.sample(range (1,91),15))
num = [8, 10, 14, 18, 29, 33, 35, 41, 46, 53, 58, 67, 73, 74, 85]
mt = Ticket()
ct = Ticket()
#mt.num = [8, 10, 14, 18, 29, 33, 35, 41, 46, 53, 58, 67, 73, 74, 85]
#ct.num = [8, 10, 14, 18, 29, 37, 95, 42, 46, 53, 58, 67, 73, 74, 85]

l = random.randint(1,91)
#l = 33
mt.prnt()
ct.prnt()
mas = Bag()
#l = mas.getnew()
#print (l)

while mt.ticket != [] and ct.ticket != [] :
    l = mas.getnew()
    mt.stress(l)
    ct.stress(l)
    #mt.prnt()
    #ct.prnt()
    print (mt.ticket)
    print (ct.ticket)
    if mt.ticket ==[] or ct.ticket == [] :
    	print ('ok')


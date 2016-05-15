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
class Ticket():

    def __init__(self):
        self.wrap = self._paper()
        self.num = self._gen()
        self.ticket = copy.deepcopy(self.num)
        return 

    def _paper(self):
        k = random.sample(range(1,10),5)
        k0 = sorted(k)
        k1 = sorted(random.sample(range(10,19),5))
        k2 = sorted(random.sample(range(19,28),5))
        for i in range(5):
            k.append(k1[i])
            k.append(k2[i])
        k_c = sorted(k)
        s=''
        index = 0
        for i in range(1,28):
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
        return 
class Bag():
    def __init__(self):
    	self.barrels = r
    	return
    def getnew(self):
        self.barrel = random.sample(self.barrels,1)[0]
        self.barrels.remove(self.barrel)
        return (self.barrel)
yn = 'y'
while yn == 'y':
    mt = Ticket()
    ct = Ticket()
    mas = Bag()
    print ('\n Начинаем новаю игру \n Сдаем карточки')
    #print ('{:-^35}'.format('Ваша карточка'))
    #mt.prnt()
    #print ('{:-^35}'.format('Карточка компьютера'))
    #ct.prnt()

    while mt.ticket != [] and ct.ticket != [] :
        l = mas.getnew()
        print('Новый бочонок: {} (осталось {})'.format(l,len(mas.barrels)))
        print ('{:-^35}'.format('Ваша карточка'))
        mt.prnt()
        print ('{:-^35}'.format('Карточка компьютера'))
        ct.prnt()
        strike = ''
        strike = input ('Зачеркнуть цифру? (y/n)')
        while strike != 'y' and strike !='n':
            print ('Символ должны быть y/n. Введите еще')
            strike = input ('Зачеркнуть цифру? (y/n)')
        if strike == 'y' and l in mt.ticket:
            mt.stress(l)
        elif strike == 'y' and (l not in mt.ticket) :
            print ('А такого числа у вас не было. увы, Вы проиграли')
            break
        elif strike == 'n' and (l in mt.ticket) :
            print ('Число было, а Вы не отметили. Вы проиграли')
            break
        elif strike !='y' and strike !='n':
            print ('символы должны быть y/n')
            break
        else:
            print ('Поехали дальше')
        ct.stress(l)
    if mt.ticket ==[] :
        print ('Поздравляю! Вы выиграли!')
    elif ct.ticket == [] :
        print ('Увы! Вы проиграли')
    else:
        print ('GAME OVER')
        yn = input ('Играем еще? y/n')

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# line = 'фывабвйцу кенабвджэ, ячсабвнгш. йцукенгвба'
# while ',' in line or '.' in line or ';' in line or ':' in line:
    # line = line.replace(',', '')
    # line = line.replace('.', '')
    # line = line.replace(';', '')
    # line = line.replace(':', '')

# print(line)

# arr = line.split()
# print(arr)

# arr2 = []
# for word in arr:
    # if 'абв' not in word:
        # arr2.append(word)
# print(arr2)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# from random import randint
# 
# def input_dat(name):
    # x = int(input(f"{name}, сколько же конфетвы возьмёте, но помните их число должно быть в пределе от 1 до 28: "))
    # while x < 1 or x > 28:
        # x = int(input(f"{name}, напоминаем что количество конфет, которое вы можете взять должно быть в пределе от 1 до 28: "))
    # return x
# 
# def p_print(name, k, counter, value):
    # print(f"Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. На столе осталось {value} конфет.")
# 
# print('Приветствуем на игре поприветствуем наших игроков')
# player1 = input("Игрок номер один представьтесь: ")
# player2 = input("Игрок номер два представьтесь: ")
# value = int(input("Какое же количество конфет будет в нашей игре: "))
# flag = randint(0, 2)  # флаг очередности
# if flag == 0:
    # print(f"Жребий показал, что первым ходит игрок под первым номером - {player1}")
# else:
    # print(f"Жребий показал, что первым ходит игрок под вторым номером - {player2}")
# 
# counter1 = 0
# counter2 = 0
# 
# while value > 28:
    # if flag == 0:
        # k = input_dat(player1)
        # counter1 += k
        # value -= k
        # flag = False
        # p_print(player1, k, counter1, value)
    # else:
        # k = input_dat(player2)
        # counter2 += k
        # value -= k
        # flag = True
        # p_print(player2, k, counter2, value)
# 
# if flag == 0:
    # print(f"Выиграл первый игрок - {player1}. Поздравляем!")
# else:
    # print(f"Выиграл второй игрок - {player2}. Поздравляем!")

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def coding(text):
    # count = 1
    # res = ''
    # for i in range(len(text)-1):
        # if text[i] == text[i+1]:
            # count += 1
        # else:
            # res = res + str(count) + text[i]
            # count = 1
    # if count > 1 or (text[len(text)-2] != text[-1]):
        # res = res + str(count) + text[-1]
    # return res

# def decoding(text):
    # number = ''
    # res = ''
    # for i in range(len(text)):
        # if i%2 == 0:
            # number = text[i]
        # else:
            # res = res + text[i] * int(number)
            # number = ''
    # return res

# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")
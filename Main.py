# Задача 1	Найдите сумму цифр трехзначного числа.
# Пример:  123 -> 6 (1 + 2 + 3)   100 -> 1 (1 + 0 + 0)
# number = int(input('Введите число: '))
# sum = (number//100) + ((number//10)%10) + (number%10) 
# print(f'Сумма цифр трехзначного числа равна: {sum}')
# Задача 2	Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:  6 -> 1  4  1   24 -> 4  16  4   60 -> 10  40  10
# number1 = int(input('Введите число: '))
# madeKat = 0
# if number1% 3 == 0:
#     print(f'Катя сделала {number1//3*2} журавликов, Петя сделал {number1//3//2} журавликов, Сережа сделал {number1//3//2} журавликов')
# else:
#     print('Введенное число не удовлетворяет условим задачи')
# Задача 3 Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где 
# сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример: 385916 -> yes   123456 -> no
# number2 = int(input('Введите номер билета: '))
# sum1 = (number2//100000) + ((number2//10000)%10) + ((number2//1000)%10) 
# sum2 = ((number2//100)%10) + ((number2//10)%10) + (number2%10)  
# if sum1 == sum2:
#     print(f'"Yes" билет с номером {number2} счастливый!')
# else:
#      print(f'"No" билет с номером {number2} не являеться счастливым')
# Задача 4 Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если 
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два 
# прямоугольника). Пример: 3 2 4 -> yes  3 2 1 -> no
# sizeN = int(input('Введите n долек: '))
# sizeM = int(input('Введите m долек: '))
# amount = int(input('Введите k долек: '))
# if amount % sizeN == 0 or amount % sizeM == 0 and amount < sizeN * sizeM:
#     print(f'"Yes" от шоколадки размером {sizeN} x {sizeM} 3можно отломить {amount} долек')
# else:
#     print(f'"No" от шоколадки размером {sizeN} x {sizeM} нельзя отломить {amount} долек')
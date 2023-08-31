"""Нам нужен рандомный список, у пользователя спрашиваем число, пробегаем по списку , 
смотрим есть ли это число в нем, если нет, то выводим ближайшее, если есть то в каком количестве."""

import random
list_length = int(input("задайте длину списка,введите число:"))
list = [random.randint(1, 100) for _ in range(list_length)]
print(list)
number= int(input("введите число:"))
close_diff = abs(list[0]-number)
closest_element = list[0]
count=0
for i in list:
    diff  = abs(i - number)
    if diff < close_diff:
        close_diff = diff
        closest_element = i
        print(closest_element)
    if i == number:
      count+=1
      print(count)


 



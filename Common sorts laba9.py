"""Мельник Дмитро Володимирович 1 курс 122А
Одразу скажу,що в цій програмі є режим тесту часу виконнання для всіх 3 типів сортування одночасно(причому на однакових масивах,
для об'єктивності тесту).Це 4 режим сортування(all sorts).При тестах я зрозумів що найкраще брати масиви на 10000 елементів.
Хоча в завданні для тесту просять на 100000 елементів(чекати доводиться більше 20 хвилин(я так і ніразу не дочекався
результату програми).Це найоптимальніший варіант тому що не доводиться занадто довго чекати результат виконання програми(десь 30 секунд
на баблсорті і ще менше на інших методах) і на такому масиві чудово видно як кожен метод себе показує по складності
та часу сортування"""


import timeit    #Імпортуємо тайміт, щоб порахувати час виконання сортувань

while True:    #Зациклюємо нашу програму
    my_setup = """
import random
from datetime import datetime    #Імпортуємо дейттайм для розрахунку часу виконання 4(тестового) режиму
import numpy as np


def bubble_sort_ascending():   #Функція сортування бульбашкою по зростанню
    comparisons = 0            #Вводимо змінні для підрахунку порівнянь і перестановок
    changes = 0
    for i in range(1, quantity_of_elements):
        for j in range(quantity_of_elements - 1, i - 1, -1):   
            if massive[j - 1] > massive[j]:   #Порівнюємо чи більший попередній елемент за наш поточний
                comparisons += 1
                massive[j], massive[j - 1] = massive[j - 1], massive[j]  #Якщо умова правдива,то міняємо місцями елементи
                changes += 2
    print(f'bubble sorted {massive}')
    print(f'Comparisons: {comparisons} Changes: {changes}')



def selection_sort_ascending():
    comparisons = 0
    changes = 0
    for i in range(quantity_of_elements - 1):
        min = i                              #Припускаємо,що мінімум займає 'і' позицію
        for j in range(i + 1, quantity_of_elements):
            if massive_sel[j] < massive_sel[min]: #Порівнюємо чи елемент на 'j' позиціїї > елемент на 'min' позиції
                comparisons += 1
                min = j   #Якщо умова правдива,то ми знайшли мінімальний елемент
        massive_sel[i], massive_sel[min] = massive_sel[min], massive_sel[i]
        changes += 2
    print(f'selection sorted {massive_sel}')
    print(f'Comparisons: {comparisons} Changes: {changes}')



def insertion_sort_ascending():   #Місце вставки ми визначаємо лінійним пошуком
    comparisons = 0
    changes = 0
    for i in range(1, quantity_of_elements):
        j = i - 1
        key = massive_ins[i]      #Елемент масиву з яким ми все порівнюємо
        while j >= 0 and massive_ins[j] > key:  #Щоб не зробити від'ємну позицію
            comparisons += 2
            massive_ins[j + 1] = massive_ins[j]  #Робимо перезапис
            changes += 1
            j -= 1
        massive_ins[j + 1] = key   #Вставляємо наш записаний елемнт на потрібне місце
    print(f'insertion sorted {massive_ins}')
    print(f'Comparisons: {comparisons} Changes: {changes}')



def bubble_sort_descending():  #Все те, саме як в зростанні
    comparisons = 0
    changes = 0
    for i in range(1, quantity_of_elements):
        for j in range(quantity_of_elements - 1, i - 1, -1):
            if massive[j - 1] < massive[j]:                    #Тільки ось тут міняємо знак
                comparisons += 1
                massive[j], massive[j - 1] = massive[j - 1], massive[j]
                changes += 2
    print(f'bubble sorted {massive}')
    print(f'Comparisons: {comparisons} Changes: {changes}')



def selection_sort_descending():  # Все те саме як в зростанні
    comparisons = 0
    changes = 0
    for i in range(quantity_of_elements - 1):
        min = i
        for j in range(i + 1, quantity_of_elements):
            if massive_sel[j] > massive_sel[min]:    #Тільки міняємо знак тут
                comparisons += 1
                min = j
        massive_sel[i], massive_sel[min] = massive_sel[min], massive_sel[i]
        changes += 2
    print(f'selection sorted {massive_sel}')
    print(f'Comparisons: {comparisons} Changes: {changes}')



def insertion_sort_descending():    #Все те саме як в зростанні
    comparisons = 0
    changes = 0
    for i in range(1, quantity_of_elements):
        j = i - 1
        key = massive_ins[i]
        while j >= 0 and massive_ins[j] < key:  #Тільки міняємо знак тут
            comparisons += 2
            massive_ins[j + 1] = massive_ins[j]
            changes += 1
            j -= 1
        massive_ins[j + 1] = key
    print(f'insertion sorted {massive_ins}')
    print(f'Comparisons: {comparisons} Changes: {changes}')


print('It`s sort program')
quantity_of_elements = int(input('Quantity of elements: '))   #Кількість елементів масиву
yourself_random = input('Input elements by yourself-1,Input random-2: ')  #Вибір як вводимо елементи
choice = input('Choose your sort type:1-bubble sort,2-selection sort,3-insertion sort,4-all sorts(тест часу із однаковими данними): ')
sort_direction = input('Which direction: 1-ascending,2-descending: ')   #Вибір у який бік сортувати
massive = np.zeros(quantity_of_elements, dtype=int)  #Створюємо масив
if yourself_random == '1':  #Реалізація вводу елементів вручну
    while True:             #Перевірка,щоб користувач вводив числа
            try:
                for i in range(quantity_of_elements):
                    massive[i] = int(input(f'Input element {i + 1} :'))
                break
            except ValueError:
                print('Input number')
    print(massive)
elif yourself_random == '2':      #Реалізація рандомного вводу елементів масиву
    for i in range(quantity_of_elements):
        massive[i] = random.randint(0, 30)
    print(massive)
massive_sel = massive.copy()  #Дві копії масивів для об'єктивних тестів
massive_ins = massive.copy()
"""
    code_to_test = """
if choice == '1' and sort_direction == '1':
    bubble_sort_ascending()
elif choice == '1' and sort_direction == '2':
    bubble_sort_descending()
elif choice == '2' and sort_direction == '1':
    selection_sort_ascending()
elif choice == '2' and sort_direction == '2':
    selection_sort_descending()
elif choice == '3' and sort_direction == '1':
    insertion_sort_ascending()
elif choice == '3' and sort_direction == '2':
    insertion_sort_descending()
elif choice == '4' and sort_direction == '1':   #Реалізація підрахунку виконання часу виконання сортувань
    start_time_bub = datetime.now()             #для кожного таймер обнуляється.Потім в кінці ще пише скільки взагальному
    bubble_sort_ascending()                     #виконувалась вся програма
    print(f'Time of bubble sort: {datetime.now() - start_time_bub}')
    start_time_sel = datetime.now()
    selection_sort_ascending()
    print(f'Time of selection sort: {datetime.now() - start_time_sel}')
    start_time_ins = datetime.now()
    insertion_sort_ascending()
    print(f'Time of insertion sort: {datetime.now() - start_time_ins}')
elif choice == '4' and sort_direction == '2':
    start_time_bub = datetime.now()
    bubble_sort_descending()
    print(f'Time of bubble sort: {datetime.now() - start_time_bub}')
    start_time_sel = datetime.now()
    selection_sort_descending()
    print(f'Time of selection sort: {datetime.now() - start_time_sel}')
    start_time_ins = datetime.now()
    insertion_sort_descending()
    print(f'Time of insertion sort: {datetime.now() - start_time_ins}')
else:
    print('Invalid choice')
    
"""
    elapsed_time = timeit.timeit(setup=my_setup, stmt=code_to_test, number=1)
    print(f'Full time of execution: {elapsed_time} seconds')

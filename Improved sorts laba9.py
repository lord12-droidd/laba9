import timeit

while True:
    my_setup = """

import numpy as np

import random

from datetime import datetime  

def cocktailSort_ascending():
    comparisons = 0
    changes = 0
    swapped = True
    start = 0
    end = quantity_of_elements - 1
    while (swapped == True):
        swapped = False   #Оновлюємо прапор з попередньої ітерації
        for i in range(start, end):
            if (massive[i] > massive[i + 1]):  #Порівнюємо чи більший поточний елемент за наступний
                comparisons += 1
                massive[i], massive[i + 1] = massive[i + 1], massive[i]  #Якщо умова правдива то міняємо місцями
                changes += 2
                swapped = True   #якщо нічого не змінилось, то масив відсортований
        if (swapped == False):
            break
        swapped = False   #Якщо не відсортований то міняємо прапор
        end = end - 1    #Переміщуємо кінцеву точку на одиничку тому що елемент знаходиться на првильному місці
        for i in range(end - 1, start - 1, -1):
             if (massive[i] > massive[i + 1]):   #Знову порівнюємо елементи
                 comparisons += 1
                 massive[i], massive[i + 1] = massive[i + 1], massive[i]
                 changes += 2
                 swapped = True
        start = start + 1   #Перемістити початкову точку на 1 щоб повернути все на місце
    print(massive)
    print(f'Comparisons: {comparisons} Changes: {changes}')

def cocktailSort_descending():   #Все те саме тільки міняємо знаки
    comparisons = 0
    changes = 0
    swapped = True
    start = 0
    end = quantity_of_elements - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (massive[i] < massive[i + 1]):   #Тут
                comparisons += 1
                massive[i], massive[i + 1] = massive[i + 1], massive[i]
                changes += 2
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (massive[i] < massive[i + 1]):   #І тут
                comparisons += 1
                massive[i], massive[i + 1] = massive[i + 1], massive[i]
                changes += 2
                swapped = True
        start = start + 1
    print(massive)
    print(f'Comparisons: {comparisons} Changes: {changes}')


def shellSort_ascending():
    comparisons = 0
    changes = 0
    gap = quantity_of_elements // 2   #Ділимо наш масив на 2 частини,які потім будемо зменшувати
    while gap > 0:   #Для цієї частини масиву виконуємо сортування вставками
        for i in range(gap, quantity_of_elements):
            temp = massive_shell[i]  #Додаємо елемент до відсортованих елементів в частині масиву та зберігаємойого в змінній
            j = i
            while j >= gap and massive_shell[j - gap] > temp:
                comparisons += 2
                massive_shell[j] =massive_shell[j - gap]
                changes += 1
                j -= gap
            massive_shell[j] = temp
        gap //= 2
    print(massive_shell)
    print(f'Comparisons: {comparisons} Changes: {changes}')

def shellSort_descending():  #Все те саме,тільки міняємо 1 знак
    comparisons = 0
    changes = 0
    gap = quantity_of_elements // 2
    while gap > 0:
        for i in range(gap, quantity_of_elements):
            temp = massive_shell[i]
            j = i
            while j >= gap and massive_shell[j - gap] < temp:  #Тут
                comparisons += 2
                massive_shell[j] =massive_shell[j - gap]
                changes += 1
                j -= gap
            massive_shell[j] = temp
        gap //= 2
    print(massive_shell)
    print(f'Comparisons: {comparisons} Changes: {changes}')

def heapify_descending(massive_heap, quantity_of_elements, i):  #Складаємо піддерево нашого масиву
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < quantity_of_elements and massive_heap[i] > massive_heap[l]:
        largest = l
    if r < quantity_of_elements and massive_heap[largest] > massive_heap[r]:
        largest = r
    if largest != i:
        massive_heap[i], massive_heap[largest] = massive_heap[largest], massive_heap[i]
        heapify_descending(massive_heap, quantity_of_elements, largest)
        
def heapSort_descending(massive_heap):
    for i in range(quantity_of_elements, -1, -1):
        heapify_descending(massive_heap, quantity_of_elements, i)
    for i in range(quantity_of_elements - 1, 0, -1):
        massive_heap[i], massive_heap[0] = massive_heap[0], massive_heap[i]
        heapify_descending(massive_heap, i, 0)
    print(massive_heap)

def heapify_ascending(massive_heap, quantity_of_elements, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < quantity_of_elements and massive_heap[i] < massive_heap[l]:
        largest = l
    if r < quantity_of_elements and massive_heap[largest] < massive_heap[r]:
        largest = r
    if largest != i:
        massive_heap[i], massive_heap[largest] = massive_heap[largest], massive_heap[i]
        heapify_ascending(massive_heap, quantity_of_elements, largest)


def heapSort_ascending(massive_heap):
    for i in range(quantity_of_elements, -1, -1):
        heapify_ascending(massive_heap, quantity_of_elements, i)
    for i in range(quantity_of_elements - 1, 0, -1):
        massive_heap[i], massive_heap[0] = massive_heap[0], massive_heap[i]
        heapify_ascending(massive_heap, i, 0)
    print(massive_heap)

print('It`s sort program')  #Абсолютно такий самий код як і в простих сортуваннях
quantity_of_elements = int(input('Quantity of elements: '))
yourself_random = input('Input elements by yourself-1,Input random-2: ')
choice = input('Choose your sort type:1-cocktail sort,2-shell sort,3-heap sort,4-all sorts(тест часу із однаковими данними): ')
sort_direction = input('Which direction: 1-ascending,2-descending: ')
massive = np.zeros(quantity_of_elements, dtype=int)
if yourself_random == '1':
    while True:
            try:
                for i in range(quantity_of_elements):
                    massive[i] = int(input(f'Input element {i + 1} :'))
                break
            except ValueError:
                print('Input number')
    print(massive)
elif yourself_random == '2':
    for i in range(quantity_of_elements):
        massive[i] = random.randint(0, 30)
    print(massive)
massive_shell = massive.copy()
massive_heap = massive.copy()
"""
    code_to_test = """
if choice == '1' and sort_direction == '1':
    cocktailSort_ascending()
elif choice == '1' and sort_direction == '2':
    cocktailSort_descending()
elif choice == '2' and sort_direction == '1':
    shellSort_ascending()
elif choice == '2' and sort_direction == '2':
    shellSort_descending()
elif choice == '3' and sort_direction == '1':
    heapSort_ascending(massive_heap)
elif choice == '3' and sort_direction == '2':
    heapSort_descending(massive_heap)
elif choice == '4' and sort_direction == '1':
    start_time_cocktail = datetime.now()
    cocktailSort_ascending()
    print(f'Time of cocktail sort: {datetime.now() - start_time_cocktail}')
    start_time_shell = datetime.now()
    shellSort_ascending()
    print(f'Time of shell sort: {datetime.now() - start_time_shell}')
    start_time_heap = datetime.now()
    heapSort_ascending(massive_heap)
    print(f'Time of heap sort: {datetime.now() - start_time_heap}')
elif choice == '4' and sort_direction == '2':
    start_time_cocktail = datetime.now()
    cocktailSort_descending()
    print(f'Time of cocktail sort: {datetime.now() - start_time_cocktail}')
    start_time_shell = datetime.now()
    shellSort_descending()
    print(f'Time of shell sort: {datetime.now() - start_time_shell}')
    start_time_heap = datetime.now()
    heapSort_descending(massive_heap)
    print(f'Time of heap sort: {datetime.now() - start_time_heap}')
else:
    print('Invalid choice')

"""
    elapsed_time = timeit.timeit(setup=my_setup, stmt=code_to_test, number=1)
    print(f'Full time of execution: {elapsed_time} seconds')
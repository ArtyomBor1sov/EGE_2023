# ЕГЭ 2023

Здесь будет много полезной информации, я в процессе создания!

## №1 - Анализ информационных моделей (работа с графами)

**_Граф_** - математическая модель, состоящая из точек (вершин) и линий (ребер)

**_Ориентированный граф_** - ребрами являются стрелкки, двигаться можно только в указанном направлении

**_Неориентированный граф_** - ребрами являются линии, двигаться можно в любом направлении

**_Взвешенный граф_** - каждому ребру соответсвует значение (вес ребра)

**_Степень вершины_** - число ребер графа, которым принадлежит вершина. В ориентированных графах выделяют входящую
и исходящую степени

### Алгоритм решения

1. Определить степени вершин
2. Определить соседние вершины

### Пример

[**_РешуЕГЭ - №10377_**](https://inf-ege.sdamgia.ru/problem?id=10377)

1. **Степени вершин**  
   А = 3  
   Б = 2 (П5)  
   В = 4  
   Г = 5 (П2)  
   Д = 4  
   Е = 3  
   К = 3
2. **Соседние вершины**  
   Б (П5) связана с Г (П2) и А (П3). Искомое расстояние - путь между П2 и П3.  

**Ответ:** 22

## №2 - Построение таблиц истинности логических выражений

![**_Таблица истинности_**](img/02_01.jpg)

### Порядок выполнения логических операций

1. Инверсия (логическое отрицание)
2. Конъюнкция (логическое умножение)
3. Дизъюнкция (логическое сложение) / XOR (исключающее ИЛИ)
4. Импликация (логическое следование)
5. Эквивалентность (логическое равенство)

**_На порядок выполнения логических операций можно влиять с помощью скобок!_**

### Основные тождества

![**_Основные тождества_**](img/02_02.jpg)

### Алгоритм решения

1. Построить таблицу истинности 
   - Вручную
     - Определить порядок действий
     - Упростить выражение (если это возможно)
     - Построить таблицу истинности
   - С помощью программы
2. Отобрать подходящие строки таблицы истинности
3. Сопоставить выбранные строки со строками из условия

### Пример

[**_РешуЕГЭ - №15787_**](https://inf-ege.sdamgia.ru/problem?id=15787)

```python
'''
Инверсия - not
Конъюнкция - and
Дизъюнкция - or
XOR - !=
Импликация - <=
Эквивалентность - ==
'''

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int(((x <= y) and (y <= w)) or (z == (x or y)))
                if F == 0:
                    print(x, y, z, w, F)

'''
РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ

x y z w F
0 1 0 0 0
1 0 0 0 0
1 0 0 1 0
1 1 0 0 0
'''
```

Обратим внимание, что в условии всего 2 строки, содержащих 2 единицы - в получившейся таблице тоже. Более того, есть
лишь 1 столбец, который в обеих строках содержит единицу.Таким образом мы можем определить, что четвертому столбцу
соответствует переменная **_x_**. Единтсвенная переменная, которая не равна единице ни в одной из строк, где **_x_**
равен единице - **_z_**, следовательно она соответствует третьему столбцу. Обратим внимание, что в строках содержащих 1
единицу, она соответствует либо **_x_**, либо **_y_**, но **_x_** - четвертый столбец, а единица стоит в первом,
следовательно **_y_** соответствует первому столбцу. По остаточному принципу второму столбцу соответствует **_w_**.

**Ответ:** ywzx

## №4 - Кодирование и декодирование информации

**_Условие Фано_** - никакое кодовое слово не может быть началом другого кодового слова

### Пример

[**_РешуЕГЭ - №16881_**](https://inf-ege.sdamgia.ru/problem?id=16881)

![**_РешуЕГЭ - №16881 - Решение_**](img/04_01.jpg)

**Ответ:** 23

## №5 - Анализ и построение алгоритмов для исполнителей

[**_Перевод в десятичную систему_**](http://informatics-lesson.ru/notations/translation-decimal-system.php)

[**_Перевод из десятичной системы_**](http://informatics-lesson.ru/notations/translation-decimal-p-ichnou.php)

[**_Перевод между степенями по одному основанию_**](http://informatics-lesson.ru/notations/translation-power-two.php)

**_Шпаргалка по переводу чисел на Python_**

```python
#ИЗ ДЕСЯТИЧНОЙ СИСТЕМЫ СЧИСЛЕНИЯ

#В ДВОИЧНУЮ

print(bin(123))
#0b1111011
print(bin(123)[2:])
#1111011

#В ВОСЬМЕРИЧНУЮ

print(oct(123))
#0o173
print(oct(123)[2:])
#173

#В ШЕСТНАДЦАТЕРИЧНУЮ

print(hex(123))
#0x7b
print(hex(123)[2:])
#7b

#В ЛЮБУЮ

def perevod(num, osn):
    values = '0123456789ABCDEF'
    result = ''
    while num > 0:
        result = values[num % osn] + result
        num = num // osn
    return result

print(perevod(123, 9))
#146

#В ДЕСЯТИЧНУЮ

print(int('1111011', 2))
#123
print(int('173', 8))
#123
print(int('7b', 16))
#123
print('146', 9)
#123
```

### Пример

[**_РешуЕГЭ - №26978_**](https://inf-ege.sdamgia.ru/problem?id=26978)

Обратим внимание на то, что результат работы алгоритма должен быть меньше 109, следовательно в его двоичной записи не
более 7 цифр. По ходу выполнения алгоритма количество разрядов увеличивается на 2, а это значит, что в изначальном
числе их должно быть не больше 5, следовательно изначальное число меньше чем 32.

```python
maximum = 0
for N in range(1, 32):
    bin_N = bin(N)[2:]
    if N % 2 == 0:
        bin_N += '10'
    else:
        bin_N += '01'
    R = int(bin_N, 2)
    if R < 109:
        maximum = max(R, maximum)
print(maximum)
```

**Ответ:** 106

## №6 - Определение результатов работы простейших алгоритмов (черепашка)

[**_Библиотека Turtle_**](https://docs.python.org/3/library/turtle.html)

### Примеры

[**_РешуЕГЭ - №47303_**](https://inf-ege.sdamgia.ru/problem?id=47303)

При выполнении алгоритма исполнитель чертит фигуру с прямыми углами. В заданиях подобного типа необязательно писать
программу - достаточно нарисовать фигуру на бумаге. Ошибок из-за точности рисунка не случится. Результат работы
исполнителя - прямоугольник со сторонами 10 и 5. Умножаем 11 на 6 и получаем итоговый ответ.

**Ответ:** 66

[**_РешуЕГЭ - №47210_**](https://inf-ege.sdamgia.ru/problem?id=47210)

В заданиях с наклонными линиями одним рисунком не обойтись - нужно писать программу, а затем внимательно считать точки.

```python
from turtle import *

speed(0)
k = 30
left(90)
for i in range(7):
    forward(10 * k)
    right(120)
penup()
for x in range(0, 10):
    for y in range(0, 11):
        goto(x * k, y * k)
        dot(4)
done()
```

**Ответ:** 38

[**_РешуЕГЭ - №47391_**](https://inf-ege.sdamgia.ru/problem?id=47391)

В заданиях с большим ответом будет проблематично считать точки самостоятельно - необходимо видоизменить программу.

[**_Метод find_overlapping_**](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html)

```python
from turtle import *

speed(0)
k = 1000
left(90)
color('black', 'red')
begin_fill()
for i in range(12):
    right(60)
    forward(2 * k)
    right(60)
    forward(2 * k)
    right(270)
end_fill()
canvas = getcanvas()
counter = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if len(s) == 1 and s[0] == 5:
            counter += 1
print(counter)
done()
```

**Ответ:** 149

**_При автоматическом подсчете необходимо указывать большой масштаб и количество итераций цикла, необходимое для
завершения фигуры - лишние итерации не нужны_**

**_Обратите внимание на то, что библиотека Turtle использует привычную нам систему координат (ось X направлена вправо, 
ось Y - вверх), но find_overlapping является методом canvas (холста), а в canvas система координат устроена по-другому
(ось X - вправо, ось Y - вниз). Учитывайте это при выборе диапазона значений для X и Y!_**

## №7 - Кодирование и декодирование информации. Передача информации

![**_Единицы измерения информации_**](img/07_01.jpg)

### Кодирование текста

I - информационный вес файла  
K - количество символов в тексте  
N - количество допустимых символов (мощность алфавита)  
i - информационный вес символа

**I = K * i**  
**N = 2<sup>i</sup>**

### Кодирование изображений

I - информационный вес файла  
K - количество пикселей в изображении  
N - количество допустимых цветов (мощность алфавита)  
i - информационный вес пикселя

**I = K * i**  
**N = 2<sup>i</sup>**

### Кодирование звука

I - информационный вес файла  
k - количество каналов  
f - частота дискретизации  
i - глубина кодирования  
t - время звучания

**I = k * f * i * t**  

### Вероятностный подход к измерению информации

I - информационный вес сообщения о событии  
p - вероятность события

**I = log<sub>2</sub>(1/p)**

### Пример

[**_РешуЕГЭ - №8097_**](https://inf-ege.sdamgia.ru/problem?id=8097)

![**_РешуЕГЭ - №8097 - Решение_**](img/07_02.jpg)

**Ответ:** 10

## №8 - Перебор слов и системы счисления

### Примеры

[**_РешуЕГЭ - №8098_**](https://inf-ege.sdamgia.ru/problem?id=8098)

**_Аналитическое решение_**

Букву "С" можно поставить на одно из пяти мест. Для каждого из пяти способов есть 3<sup>4</sup> способов расставить
оставшиеся буквы (по 3 варианта на каждую из 4 позиций). 5 * 3<sup>4</sup> = 405

**_Решение на Python_**

[**_Библиотека Itertools_**](https://habr.com/ru/company/otus/blog/529356)

```python
from itertools import *
alphabet = "СЛОН"
words = product(alphabet, repeat = 5)
counter = 0
for element in words:
    if element.count('С') == 1:
        counter += 1
print(counter)
```

**Ответ:** 405

[**_РешуЕГЭ - №9162_**](https://inf-ege.sdamgia.ru/problem?id=9162)

Алфавит из 4 букв можно представить в виде системы счисления с основанием 4. Список слов дает нам понять, что: М = 0,
С = 1, Т = 2, Ф = 3. Обратиим внимание, что на 1 месте стоит число 0, следовательно на 138 месте стоит число
137<sub>10</sub> = 2021<sub>4</sub>

**Ответ:** ТМТС

[**_Число сочетаний_**](https://www.yaklass.ru/p/algebra/11-klass/nachalnye-svedeniia-kombinatoriki-9340/sochetaniia-i-ikh-svoistva-9344/re-9772d3f7-98a3-4363-a771-70d1e2306dc8)

[**_Сайт Константина Полякова - №1961_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=1961)

Воспользуемся формулой для вычисления числа сочетаний. Есть 35 способов расставить буквы А и для каждого из них есть
4 способа расставить буквы Т. 35 * 4 = 140

**Ответ:** 140

## №9 - Работа с таблицами

## №11 - Вычисление количества информации

### Примеры

[**_РешуЕГЭ - №10289_**](https://inf-ege.sdamgia.ru/problem?id=10289)

![**_РешуЕГЭ - №10289 - Решение_**](img/11_01.jpg)

**Ответ:** 10

[**_Сайт Константина Полякова - №5702_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5702)

![**_Сайт Константина Полякова - №5702 - Решение_**](img/11_02.jpg)

**Ответ:** 28

## №12 - Выполнение алгоритмов для исполнителей

### Примеры

[**_РешуЕГЭ - №10388_**](https://inf-ege.sdamgia.ru/problem?id=10388)

В заданиях, где дана изначальная строка, достаточно написать программу, выполняющую алгоритм из условия

```python
s = '5' * 54 + '7'
while '722' in s or '557' in s:
    s = s.replace('722', '57', 1)
    s = s.replace('557', '72', 1)
print(s)
```

**Ответ:** 572

[**_РешуЕГЭ - №26957_**](https://inf-ege.sdamgia.ru/problem?id=26957)

В заданиях, где не дана изначальная строка, необходимо обратить внимание на алгоритм из условия. Есть вероятность, что
порядок, в котором стоят символы, не повлияет на результат работы алгоритма (как в этом случае)

```python
s = '>' + '1' * 26 + '2' * 10 + '3' * 14
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
summa = 0
for i in range(len(s) - 1):
    summa += int(s[i])
print(summa)
```

**Ответ:** 138

[**_СтатГрад (октябрь 2022) - №12_**](СтатГрад/2022-10/Вариант%20№1.pdf)

Однако бывают случаи, когда строка не дана, но порядок символов влияет на итоговый ответ. Пусть k1 раз выполняется
команда 1, k2 раз - команда 2 и тд. Получаем систему уравнений, которую можно решить с помощью Python

![**_СтатГрад (октябрь 2022) - №12 - Решение_**](img/12_01.jpg)

```python
minimum = 10 ** 12
for k1 in range(81):
    for k2 in range(81):
        for k3 in range(81):
            for k4 in range(81):
                if 2 * k1 + k3 == 2 * k2 + k4 and k2 + 2 * k4 == 40 and k1 + 2 * k3 > 50:
                    minimum = min(k1 + 2 * k3, minimum)
print(minimum)
```

**Ответ:** 52

[**_СтатГрад (декабрь 2022) - №12_**](СтатГрад/2022-12/Вариант%20№1.pdf)

В тех случаях, когда исходная строка неизвестна и порядок цифр влияет на итоговый результат, можно перебрать все
подходящие строки (в адекватных пределах)

```python
from itertools import *

minimum = 10 ** 12
for element in product('12', repeat = 20):
    if element.count('1') == 10:
        stroka = ''
        for symbol in element:
            stroka += symbol
        stroka = '0' + stroka + '0'
        while '00' not in stroka:
            stroka = stroka.replace('012', '30', 1)
            if '011' in stroka:
                stroka = stroka.replace('011', '20', 1)
                stroka = stroka.replace('022', '40', 1)
            else:
                stroka = stroka.replace('01', '10', 1)
                stroka = stroka.replace('02', '101', 1)
        if stroka.count('1') == 7 and stroka.count('2') == 5 and stroka.count('3') < minimum:
            minimum = stroka.count('3')
print(minimum)
```

**Ответ:** 52

## №13 - Поиск путей в графе

### Пример

[**_РешуЕГЭ - №10478_**](https://inf-ege.sdamgia.ru/problem?id=10478)

Для решения задач подобного типа необходимо присвоить значение стартовой вершине (0, если ищем расстояние, и 1, если
ищем количество путей)

А = **1**  
Б = А = **1**  
В = А + Б + Г = **4**  
Г = А + Д = **2**  
Д = А = **1**  
Е = Б + В = **5**  
Ж = В + Е + З = **16**  
З = В + Г + Д = **7**  
И = ~~Е~~ + Ж + ~~З~~ = **16**  
К = 0  
Л = Ж = **16**  
М = К + Л = **16**

**Ответ:** 16

[**_Сайт Константина Полякова - №5699_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5699)

Решить данную задачу таким же способом не выйдет - необходимо разбить на случаи. Также стоит обратить внимание на то,
что маршруты с ребром М -> З всегда нарушают условие "не проходящих дважды через один пункт", следовательно можно
игнорировать данное ребро

**_В маршруте есть З -> Д_**

Ж = **1**  
З = Ж = **1**  
Д = З = **1**  
К = Д = **1**  
Л = К = **1**  
М = Л = **1**  
Н = М = **1**  
А = М + Н = **2**  
Б = А + Н = **3**  
В = Б + Н = **4**  
Г = В = **4**  
Е = В + Г + Д = **9**  
Ж = В + Д + Е = **14**

**_В маршруте нет З -> Д_**

Ж = **1**  
З = Ж = **1**   
К = З = **1**  
Л = 3 + К = **2**  
М = Л = **2**  
Н = Ж + М = **3**  
А = М + Н = **5**  
Б = А + Н = **8**  
В = Б + Н = **11**  
Г = В = **11**  
Д = Г = **11**  
Е = В + Г + Д = **33**  
Ж = В + Д + Е = **55**

Складываем найденные значения и получаем итоговый ответ

**Ответ:** 69

## №14 - Кодирование чисел. Системы счисления

### Примеры

[**_РешуЕГЭ - №48384_**](https://inf-ege.sdamgia.ru/problem?id=48384)

```python
minimum = 10 ** 12
for x in range(9):
    for y in range(9):
        result = (8 * 9 ** 4) + (8 * 9 ** 3) + (x * 9 ** 2) + (4 * 9) + y + (7 * 11 ** 4) + (x * 11 ** 3) + (4 * 11 ** 2) + (4 * 11) + y
        if result % 61 == 0:
            minimum = min(result, minimum)
print(minimum // 61)
```

**Ответ:** 2715

[**_РешуЕГЭ - №8664_**](https://inf-ege.sdamgia.ru/problem?id=8664)

```python
num = 8 ** 2020 + 4 ** 2017 + 26 - 1
stroka = bin(num)[2:]
print(stroka.count('1'))
```

**Ответ:** 5

## №15 - Преобразование логических выражений

4 ВАРИАНТА ЗАДАЧ

## №16 - Рекурсивные алгоритмы

### Пример

[**_РешуЕГЭ - №4645_**](https://inf-ege.sdamgia.ru/problem?id=4645)

```python
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return F(n - 1) * n + F(n - 2) * (n - 1)

print(F(5))
```

**Ответ:** 309

**ВАЖНО!** Для решения задачи с маленьким значением параметра функции достаточно написать программу подобного типа. В
противном случае программа может выполняться долго, и тогда необходимо найти закономерность в результатах работы функции.
Также может помочь декоратор [**_lru_cache_**](https://www.geeksforgeeks.org/python-functools-lru_cache)

## №17 - Обработка числовых последовательностей

[**_Работа с файлами_**](https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html)

### Пример

[**_РешуЕГЭ - №37373_**](https://inf-ege.sdamgia.ru/problem?id=37373)

```python
'''
ПАРЫ ПОДРЯД ИДУЩИХ ЭЛЕМЕНТОВ

for i in range(len(nums) - 1):
    print(nums[i], nums[i + 1])

ТРОЙКИ ПОДРЯД ИДУЩИХ ЭЛЕМЕНТОВ

for i in range(len(nums) - 2):
    print(nums[i], nums[i + 1], nums[i + 2])

ПАРЫ РАЗЛИЧНЫХ ЭЛЕМЕНТОВ

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
    print(nums[i], nums[j])

ТРОЙКИ РАЗЛИЧНЫХ ЭЛЕМЕНТОВ

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
    print(nums[i], nums[j], nums[k])
'''

f = open('37373.txt', 'r')
nums = []
for line in f:
    nums.append(int(line))
counter = 0
maximum = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) % 36 == 0 and (nums[i] % 13 == 0 or nums[j] % 13 == 0):
            counter += 1
            maximum = max(abs(nums[i] - nums[j]), maximum)
print(counter, maximum)
```

**Ответ:** 212587 9972

## №18 - Робот-сборщик монет

## №19 - Теория игр. Задание 1

### Примеры

[**_Сайт Константина Полякова - №5376_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5376)

```python
from functools import lru_cache

def moves(num_1, num_2):
    return [(num_1 + 1, num_2), (num_1, num_2 + 1), (num_1 * 2, num_2), (num_1, num_2 * 2)]

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 >= 259:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if any(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'

for S in range(1, 242):
    if game(17, S) == 'L1':
        print(S)
        break
```

**Ответ:** 61

[**_Сайт Константина Полякова - №3489_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3489)

```python
from functools import lru_cache

def moves(num_1, num_2):
    result = []
    if num_1 > 0:
        result.append((num_1 - 1, num_2))
        result.append(((num_1 - (num_1 % 2)) // 2, num_2))
    if num_2 > 0:
        result.append((num_1, num_2 - 1))
        result.append((num_1, (num_2 - (num_2 % 2)) // 2))
    return result

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 <= 18:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'

for M in range(10, 100):
    if game(M, M) == 'L1':
        print(M)
        break
```

**Ответ:** 13

## №20 - Теория игр. Задание 2

### Примеры

[**_Сайт Константина Полякова - №5376_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5376)

```python
from functools import lru_cache

def moves(num_1, num_2):
    return [(num_1 + 1, num_2), (num_1, num_2 + 1), (num_1 * 2, num_2), (num_1, num_2 * 2)]

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 >= 259:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'
    if any(game(i, j) == 'L1' for i, j in moves(num_1, num_2)):
        return 'W2'

for S in range(1, 242):
    if game(17, S) == 'W2':
        print(S)
```

**Ответ:** 112 120

[**_Сайт Константина Полякова - №3489_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3489)

```python
from functools import lru_cache

def moves(num_1, num_2):
    result = []
    if num_1 > 0:
        result.append((num_1 - 1, num_2))
        result.append(((num_1 - (num_1 % 2)) // 2, num_2))
    if num_2 > 0:
        result.append((num_1, num_2 - 1))
        result.append((num_1, (num_2 - (num_2 % 2)) // 2))
    return result

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 <= 18:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'
    if any(game(i, j) == 'L1' for i, j in moves(num_1, num_2)):
        return 'W2'

for S in range(6, 100):
    if game(13, S) == 'W2':
        print(S)
```

**Ответ:** 14 27

## №21 - Теория игр. Задание 3

### Примеры

[**_Сайт Константина Полякова - №5376_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5376)

```python
from functools import lru_cache

def moves(num_1, num_2):
    return [(num_1 + 1, num_2), (num_1, num_2 + 1), (num_1 * 2, num_2), (num_1, num_2 * 2)]

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 >= 259:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'
    if any(game(i, j) == 'L1' for i, j in moves(num_1, num_2)):
        return 'W2'
    if all(game(i, j) == 'W1' or game(i, j) == 'W2' for i, j in moves(num_1, num_2)):
        return 'L2'

for S in range(1, 242):
    if game(17, S) == 'L2':
        print(S)
        break
```

**Ответ:** 111

[**_Сайт Константина Полякова - №3489_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3489)

```python
from functools import lru_cache

def moves(num_1, num_2):
    result = []
    if num_1 > 0:
        result.append((num_1 - 1, num_2))
        result.append(((num_1 - (num_1 % 2)) // 2, num_2))
    if num_2 > 0:
        result.append((num_1, num_2 - 1))
        result.append((num_1, (num_2 - (num_2 % 2)) // 2))
    return result

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 <= 18:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'
    if any(game(i, j) == 'L1' for i, j in moves(num_1, num_2)):
        return 'W2'
    if all(game(i, j) == 'W1' or game(i, j) == 'W2' for i, j in moves(num_1, num_2)):
        return 'L2'

for N in range(10, 100):
    if game(N, N) == 'L2':
        print(N)
        break
```

**Ответ:** 14

## №22 - Многопроцессорные системы

## №23 - Поиск количества программ

### Примеры

[**_РешуЕГЭ - №15932_**](https://inf-ege.sdamgia.ru/problem?id=15932)

```python
data = [0] * 45
data[2] = 1
for i in range(3, 14):
    data[i] = data[i - 1]
    if i % 2 == 0 and i // 2 >= 2:
        data[i] += data[i // 2]
    if i % 3 == 0 and i // 3 >= 2:
        data[i] += data[i // 3]
for i in range(14, 45):
    if i != 29:
        data[i] = data[i - 1]
        if i % 2 == 0 and i // 2 >= 13:
            data[i] += data[i // 2]
        if i % 3 == 0 and i // 3 >= 13:
            data[i] += data[i // 3]
print(data[44])
```

**Ответ:** 150

[**_Сайт Константина Полякова - №5543_**](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5543)

В задачах подобного типа необходимо знать не только количество программ, но и траектории вычисления, соответствующие
этим программам. Для решения можно написать подобную программу, но этот алгоритм далеко не самый оптимальный

```python
data = [[] for i in range(601)]
data[1].append([[1], True])
for i in range(2, 601):
    if i - 2 >= 1:
        for way, statement in data[i - 2]:
            new_way = way.copy()
            new_way.append(i)
            if len(new_way) >= 2 and new_way[-2] % 2 != 0 and new_way[-1] % 2 != 0:
                statement = False
            data[i].append([new_way, statement])
    if i % 3 == 0 and i // 3 >= 1:
        for way, statement in data[i // 3]:
            new_way = way.copy()
            new_way.append(i)
            if len(new_way) >= 2 and new_way[-2] % 2 != 0 and new_way[-1] % 2 != 0:
                statement = False
            data[i].append([new_way, statement])
    if i % 4 == 0 and i // 4 >= 1:
        for way, statement in data[i // 4]:
            new_way = way.copy()
            new_way.append(i)
            if len(new_way) >= 2 and new_way[-2] % 2 != 0 and new_way[-1] % 2 != 0:
                statement = False
            data[i].append([new_way, statement])
counter = 0
for way, statement in data[600]:
    if statement:
        counter += 1
print(counter)
```

Первым числом в каждой траектории вычисления является 1. Следующее число должно быть четным, единственный вариант - 4.
Можно заметить, что с помощью любой команды из четного числа может получиться только четное число, а это значит, что
можно использовать любую последовательность команд. Таким образом, для решения данной задачи достаточно посчитать
количество путей из 4 в 600.

**Ответ:** 20375

## №24 - Обработка символьных строк

### Примеры

[**_РешуЕГЭ - №27421_**](https://inf-ege.sdamgia.ru/problem?id=27421)

```python
f = open('files/27421.txt', 'r')
line = f.readline()
counter = 1
maximum = 1
for i in range(1, len(line)):
    if line[i] != line[i - 1]:
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 1
print(maximum)
```

**Ответ:** 35

[**_РешуЕГЭ - №27686_**](https://inf-ege.sdamgia.ru/problem?id=27686)

```python
f = open('files/27686.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'X':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('X' * 19))
# print(line.count('X' * 20))
```

**Ответ:** 19

[**_РешуЕГЭ - №27689_**](https://inf-ege.sdamgia.ru/problem?id=27689)

```python
f = open('files/27689.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if ((symbol == 'X' and counter % 3 == 0) or
        (symbol == 'Y' and counter % 3 == 1) or
        (symbol == 'Z' and counter % 3 == 2)):
        counter += 1
        maximum = max(counter, maximum)
    else:
        if symbol == 'X':
            counter = 1
        else:
            counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('XYZ' * 4 + 'X'))
# print(line.count('XYZ' * 4 + 'XY'))
```

**Ответ:** 15

[**_РешуЕГЭ - №33103_**](https://inf-ege.sdamgia.ru/problem?id=33103)

```python
f = open('files/33103.txt', 'r')
counter = 0
for line in f:
    if line.count('A') > line.count('E'):
        counter += 1
print(counter)
```

**Ответ:** 485

[**_РешуЕГЭ - №33526_**](https://inf-ege.sdamgia.ru/problem?id=33526)

```python
f = open('files/33526.txt', 'r')
line = f.readline()
counter = {}
for i in range(1, len(line) - 1):
    if line[i - 1] == line[i + 1]:
        counter[line[i]] = counter.get(line[i], 0) + 1
maximum = 0
for key, val in counter.items():
    if val > maximum:
        maximum = val
        max_letter = key
print (max_letter)

# f = open('files/33526.txt', 'r')
# line = f.readline()
# counter = [0] * 26
# for i in range(1, len(line) - 1):
#     if line[i - 1] == line[i + 1]:
#         counter[ord(line[i]) - ord('A')] += 1
# max_ind = 0
# for i in range(len(counter)):
#     if counter[i] > counter[max_ind]:
#         max_ind = i
# print(chr(ord('A') + max_ind))

# f = open('files/33526.txt', 'r')
# line = f.readline()
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# counter = [0] * 26
# for i in range(1, len(line) - 1):
#     if line[i - 1] == line[i + 1]:
#         counter[letters.find(line[i])] += 1
# max_ind = 0
# for i in range(len(counter)):
#     if counter[i] > counter[max_ind]:
#         max_ind = i
# print(letters[max_ind])
```

**Ответ:** D

[**_РешуЕГЭ - №35482_**](https://inf-ege.sdamgia.ru/problem?id=35482)

```python
f = open('files/35482.txt', 'r')
minimum = 10 ** 12
for line in f:
    if line.count('G') < minimum:
        minimum = line.count('G')
        min_line = line
maximum = 0
for code in range(ord('A'), ord('Z') + 1):
    if min_line.count(chr(code)) >= maximum:
        maximum = min_line.count(chr(code))
        max_letter = chr(code)
print(max_letter)
```

**Ответ:** T

[**_РешуЕГЭ - №35998_**](https://inf-ege.sdamgia.ru/problem?id=35998)

```python
f = open('files/35998.txt', 'r')
maximum = 0
for line in f:
    if line.count('A') < 25:
        for code in range(ord('A'), ord('Z') + 1):
            maximum = max(line.rfind(chr(code)) - line.find(chr(code)), maximum)
print(maximum)
```

**Ответ:** 1004

[**_РешуЕГЭ - №47228_**](https://inf-ege.sdamgia.ru/problem?id=47228)

```python
f = open('files/47228.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
i = 0
while i < len(line):
    if line[i] in 'CDF' and line[i + 1] in 'AO':
        counter += 1
        maximum = max(counter, maximum)
        i += 2
    else:
        counter = 0
        i += 1
print(maximum)
```

**Ответ:** 95

## №25 - Обработка целочисленной информации

### Примеры

[**_РешуЕГЭ - №27422_**](https://inf-ege.sdamgia.ru/problem?id=27422)

```python
for num in range(174457, 174506):
    divs = []
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
            if len(divs) > 2:
                break
    if len(divs) == 2:
        print(divs)
```

**Ответ:**  
3 58153  
7 24923  
59 2957  
13 13421  
149 1171  
5 34897  
211 827  
2 87251

[**_РешуЕГЭ - №27850_**](https://inf-ege.sdamgia.ru/problem?id=27850)

```python
for num in range(245690, 245757):
    counter = 0
    for div in range(2, num):
        if num % div == 0:
            counter += 1
            break
    if counter == 0:
        print(num - 245689, num)
```

**Ответ:**  
22 245711  
30 245719  
34 245723  
52 245741  
58 245747  
64 245753  

[**_РешуЕГЭ - №29673_**](https://inf-ege.sdamgia.ru/problem?id=29673)

**_Нечетное количество делителей <=> Корень числа - целое число_**

```python
for root in range(11112, 14949):
    num = root ** 2
    divs = [root]
    for div in range(2, root):
        if num % div == 0:
            divs.append(div)
            divs.append(num // div)
            if len(divs) > 3:
                break
    if len(divs) == 3:
        print(num, max(divs))
```

**Ответ:**  
131079601 1225043  
141158161 1295029  
163047361 1442897

[**_РешуЕГЭ - №33197_**](https://inf-ege.sdamgia.ru/problem?id=33197)

```python
for num in range(1000000, 2000001):
    counter = 0
    for div in range(int(num ** 0.5), 949, -1):
        if num % div == 0:
            if num // div - div <= 100:
                counter += 1
            else:
                break
    if counter >= 3:
        print(num)
```

**Ответ:**  
1113840  
1179360  
1208844  
1499400

[**_РешуЕГЭ - №33527_**](https://inf-ege.sdamgia.ru/problem?id=33527)

```python
# 2^1 * x^1 - 2 четных делителя
# 2^1 * x^2 - 3 четных делителя
# 2^1 * x^1 * y^1 - 4 четных делителя
# 2^2 * x^1 - 4 четных делителя
# 2^3 - 3 четных делителя

# 101000000 <= 2^1 * x^2 <= 102000000
# 50500000 <= x^2 <= 51000000
# 7107 <= x <= 7141

for num in range(7107, 7142):
    counter = 0
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            counter += 1
            break
    if counter == 0:
        print(2 * (num ** 2))
```

**Ответ:**  
101075762  
101417282  
101588258  
101645282

[**_РешуЕГЭ - №35483_**](https://inf-ege.sdamgia.ru/problem?id=35483)

```python
# 2^K - 1 нечетный делитель
# 2^K * x^1 - 2 нечетных делителя
# 2^K * x^2 - 3 нечетных делителя
# 2^K * x^3 - 4 нечетных делителя
# 2^K * x^4 - 5 нечетных делителей
# 2^K * x^1 * y^1 - 4 нечетных делителя
# 2^K * x^2 * y^1 - 6 нечетных делителей
# 2^K * x^1 * y^1 * z^1 - 8 нечетных делителей

# 35000000 <= 2^K * x^4 <= 40000000
# x^4 <= 40000000
# x <= 79

def is_prime(num):
    answer = True
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            answer = False
            break
    return answer

answer = []
for num in range(2, 80):
    if is_prime(num):
        mult = 1
        while mult * num ** 4 <= 40000000:
            if 35000000 <= mult * num ** 4 <= 40000000:
                answer.append(mult * num ** 4)
            mult *= 2
answer.sort()
print(answer)
```

**Ответ:**  
35819648  
38950081  
39037448  
39337984

[**_РешуЕГЭ - №35999_**](https://inf-ege.sdamgia.ru/problem?id=35999)

```python
# 2^m <= 400000000 => m = [0, 28]
# 3^n <= 400000000 => n = [1, 17]

answer = []
for m in range(0, 29, 2):
    for n in range(1, 18, 2):
        if 200000000 <= 2 ** m * 3 ** n <= 400000000:
            answer.append(2 ** m * 3 ** n)
answer.sort()
print(answer)
```

**Ответ:**  
201326592  
229582512  
254803968  
322486272

[**_РешуЕГЭ - №45259_**](https://inf-ege.sdamgia.ru/problem?id=45259)

```python
for i in range(10):
    for j in range(10):
        num = int('12345' + str(i) + '7' + str(j) + '8')
        if num % 23 == 0:
            print(num, num // 23)
```

**Ответ:**  
123450798 5367426  
123451718 5367466  
123453788 5367556  
123454708 5367596  
123456778 5367686  
123459768 5367816

[**_РешуЕГЭ - №46983_**](https://inf-ege.sdamgia.ru/problem?id=46983)

```python
num = 460000001
counter = 0
while counter < 5:
    divs = []
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
    if len(divs) >= 7:
        divs.sort()
        M = divs[-6]
        print(M)
        counter += 1
    num += 1
```

**Ответ:**  
41818182  
261959  
5  
271  
57500001

[**_РешуЕГЭ - №47229_**](https://inf-ege.sdamgia.ru/problem?id=47229)

[**_Библиотека fnmatch_**](https://docs-python.ru/standart-library/modul-fnmatch-python)

```python
from fnmatch import *

for num in range(0, 10 ** 10 + 1, 2023):
    if fnmatch(str(num), '1?2139*4'):
        print(num, num // 2023)

# for num in range(0, 10 ** 10 + 1, 2023):
#     s = str(num)
#     if s[0] == '1' and s[2:6] == '2139' and s[-1] == '4':
#         print(num, num // 2023)
```

**Ответ:**  
162139404 80148  
1321399324 653188  
1421396214 702618  
1521393104 752048

## №26 - Обработка целочисленной информации

### Примеры

[**_РешуЕГЭ - №27423_**](https://inf-ege.sdamgia.ru/problem?id=27423)

[**_РешуЕГЭ - №29674_**](https://inf-ege.sdamgia.ru/problem?id=29674)

[**_РешуЕГЭ - №33198_**](https://inf-ege.sdamgia.ru/problem?id=33198)

[**_РешуЕГЭ - №33528_**](https://inf-ege.sdamgia.ru/problem?id=33528)

[**_РешуЕГЭ - №35484_**](https://inf-ege.sdamgia.ru/problem?id=35484)

[**_РешуЕГЭ - №40742_**](https://inf-ege.sdamgia.ru/problem?id=40742)

[**_РешуЕГЭ - №45260_**](https://inf-ege.sdamgia.ru/problem?id=45260)

[**_РешуЕГЭ - №47023_**](https://inf-ege.sdamgia.ru/problem?id=47023)

[**_РешуЕГЭ - №47230_**](https://inf-ege.sdamgia.ru/problem?id=47230)

## №27 - Программирование

### Примеры

[**_РешуЕГЭ - №27424_**](https://inf-ege.sdamgia.ru/problem?id=27424)

[**_РешуЕГЭ - №27891_**](https://inf-ege.sdamgia.ru/problem?id=27891)

[**_РешуЕГЭ - №33199_**](https://inf-ege.sdamgia.ru/problem?id=33199)

[**_РешуЕГЭ - №33529_**](https://inf-ege.sdamgia.ru/problem?id=33529)

[**_РешуЕГЭ - №35485_**](https://inf-ege.sdamgia.ru/problem?id=35485)

[**_РешуЕГЭ - №36001_**](https://inf-ege.sdamgia.ru/problem?id=36001)

[**_РешуЕГЭ - №37162_**](https://inf-ege.sdamgia.ru/problem?id=37162)

[**_РешуЕГЭ - №38961_**](https://inf-ege.sdamgia.ru/problem?id=38961)

[**_РешуЕГЭ - №45261_**](https://inf-ege.sdamgia.ru/problem?id=45261)

[**_РешуЕГЭ - №46985_**](https://inf-ege.sdamgia.ru/problem?id=46985)

[**_РешуЕГЭ - №47231_**](https://inf-ege.sdamgia.ru/problem?id=47231)
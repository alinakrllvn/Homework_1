# Домашнее задание №1

## Формат сдачи

Приватный GitHub репозиторий (уточнения чуть позже)\
Под каждое задание отведен отдельный файл (например, `task_1.py` для задания №1)


## Дедлайн и алгоритм оценивания

**Мягкий дедлайн**\
23.10.2024 23:59

**Максимальный балл:** 8 баллов

**Если работа сдана до мягкого дедлайна**\
Балл за задание рассчитывается по формуле: $\text{Балл за дз} = min(\text{Балл за дз}, 8)$.


**Если работа сдана после мягкого дедлайна**\
Балл за задание рассчитывается по формуле:

$\text{Балл за дз} = max(0, \text{Балл за дз} \times \text{Штраф})$\
$\text{Штраф} = (1-(\dfrac{(\dfrac{x}{1440})}{5})^2), \text{где x -количество минут после мягкого дедлайна}$

Так, опоздав на сутки (1440 минут), штраф составит $1-\frac{1}{25}=0.96$ (т.е. лишаетесь 4% оценки)\
Штраф снимает баллы нелинейно. Опоздав на 4 дня, он составит $1-\frac{16}{25}=0.36$ (приведя к потеря 64% оценки)\
Опоздав более чем на 5 дней, оценка составит 0 баллов.


# Задачи
## Задача 1. Названия переменных (1 балл)


Мы обсуждали на лекциях и семинарах, что в Python существуют именные конвенции; в частности, такие конвенции существуют для переменных ([напоминание](https://peps.python.org/pep-0008/#function-and-variable-names))

Напишите программу, которая принимает на вход строку (название переменной) и выполняет следующие преобразования в попытке её исправить:
1) **(0.2 балла)** символы `-` заменяются на `_` 
2) **(0.2 балла)** если переменная написана в формате CamelCase, каждое слово должно быть разделено нижним подчеркиванием и приведено к нижнему регистру (-> `camel_case`). В частности, переменные типа `ABC` -> `a_b_c`
3) **(0.2 балла)** любые пробелы во вводе переменной заменяются на `_`, после чего избыточное количество символов `_` заменяется на один.
Пробелы по бокам должны обрезаться и не быть заменены на `_`. Пример: "this is my&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" -> "this_is_my_name"
4) **(0.2 балла)** если переменная начинается с цифр, они должны быть удалены; пример: `1myname` -> `myname` (но `myname1` -> `myname1`)
5) **(0.2 балла)** если после всех преобразований имя переменной содержит что-то кроме цифр ([0-9]), букв английского алфавита ([A-z]) и нижнего подчеркивания "\_", выводится "Введено некорректное имя переменной". Иначе выводится исправленное имя переменной с учетом всех преобразований 

Примечание: **регулярные выражения использовать нельзя**

## Задача 2. Вендинговый автомат (1 балл)

Представьте, что вам необходимо реализовать интерфейс для доступа к вендинговому автомату, содержащему следующие товары:

| ID  | ProductName | Цена |
|-----|-------------|------|
| 001 | Батончик    | 70   |
| 002 | Вода        | 45   |
| 003 | Газировка   | 64   |
| 004 | Булочка     | 33   |

Условия:
1) **(0.2 балла)** При запуске программы должна выводиться таблица выше (форматирование не должно поплыть) 
2) **(0.2 балла)** После вывода таблицы пользователю необходимо ввести ID желаемого товара (0.2 балла)
	- Если ID не существует, выводится сообщение "Товара с таким ID не существует", после чего выполнение программы завершается
	- Если ID существует, выводится сообщение "Внесите {x} тугриков", где {x} - цена товара, как в таблице. После этого программа вновь ожидает ввода от пользователя
3) **(0.2 балла)** "Внесение" тугриков осуществляется через input(). Будем считать, что существуют лишь купюры номинала 10/50/100/500 тугриков.
При попытке внесения купюры неправильного номинала программа должна выводить "Внесена фальшивая куплюра" и вновь переходить в режим ожидания внесения купюр **(0.2 балла)**
4) **(0.2 балла)** При каждом внесении нефальшивых купюр должна происходить проверка: **(0.2 балла)**
	- Если номинал купюры >= цены товара, должна выводиться строка "Ваша сдача: x тугриков" (x - целое положительное число [0; 467]). После этого выполнение программы завершается
	- Если номинал купюры < цены товара, должна выводиться строка "Осталось внести x тугриков" (х - остаток после внесения введенной пользователем цены). После этого программа снова переходит в режим ожидания пользовательского ввода. Выполнение программы будет завершено, когда будет внесена вся сумма (последовательно или за один раз). Перед завершением должна выводиться строка "Ваша сдача: x тугриков" (x - целое положительное число [0; 467])
5) **(0.2 балла)** На любом этапе при вводе чего-либо пользователь может написать "ОТМЕНА" (в верхнем регистре), и тогда выполнение программы завершается **(0.2 балла)**


## Задача 3. Энакин Скайуокер (1 балл)

Дан следующий список:

```python
person = ['Энакин Скайуокер', 
		  41, 
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'], 
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]
``` 

Реализуйте программу, которая принимает на вход число, соответствующее номеру задания ниже. После ввода числа должен быть выполнен соответствующий ему функционал. Если пользователь вводит "выход", программа прекращает выполнение. \
Используйте шаблон, предоставленный в файле `task_3.py`\
Проверка данного задания будет производиться на измененном списке `person`. Поэтому не пытайтесь "захардкодить" функционал.

**По 0.1 балла за каждый пункт:**

1. Выведите фамилию и имя Энакина в формате "Персона: {Фамилия}, {Имя}".
2. Выведите возраст Энакина.
3. Напечатайте все места, связанные с крупными событиями вселенной Star Wars, в которых участвовал Энакин, через запятую.
4. Найдите количество таких мест и выведите это количество.
5. Если среди мест службы Энакина есть 'Звезда Смерти', то он служит Империи. Выведите True или False.
6. Напечатайте цвет светового меча Энакина.
7. Измените возраст Энакина на 42 и обновите список. Выведите новый возраст.
8. Добавьте новое место в список важных мест - 'Эндор'. Выведите обновленный список. Примечание: если "Эндор" уже содержится в списке важных мест, повторно его добавлять не нужно.
9. Проверьте, содержит ли список характеристик Энакина ранг 'лорд ситхов'. Если да, выведите "Энакин - лорд ситхов", иначе - "Энакин - джедай".
10. Если у Энакина в списке мест более 4 мест, выведите "Энакин побывал во многих местах". Если 4 или меньше - "Энакин не так много путешествовал".

## Задача 4. Срезы списков (0.5 балла)

Используя список `companions`, выведите на экран с помощью срезов следующие списки: 
```
["Gale", "Karlach", "Lae'zel"]
["Gale", "Lae'zel", "Wyll", "Halsin", "Halsin", "Minsc", "Alfira"]
["Alfira", "Jaheira", "Wyll", "Karlach"]
["Astarion", "Losiir"]
```

```python
companions = ["Astarion", "Gale", "Karlach", "Lae'zel",  
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",  
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]
```

**Примечание 1.** Проверка данного задания будет производиться на измененном списке `companions`. Поэтому не пытайтесь "захардкодить" функционал\
**Примечание 2.** Использование срезов обязательно


## Задача 5. Снаряжение для авантюристов (0.5 балла)

Группа из 3 авантюристов выбирает снаряжение для экспедиции из списка: меч, лук, топор, щит, зелье. 
Предметы будут включены в общий набор, если все три авантюриста сочтут их нужными (выберут их). 
Каждый авантюрист может выбрать минимум один и максимум три предмета. \
Нужно посчитать количество предметов, которые войдут в общий набор. Вввод предметов реализуется через пробел с маленькой буквы. 

**Примечание.** Если после ввода названий предметов программа обнаруживает что-то кроме вышеуказанных предметов, печатается "Неверный предмет, попробуйте снова"; после этого программа не должна останавливать выполнение, а ожидать правильную строку с предметами.

### _Примеры:_

(ввод) и (вывод) здесь обозначают этапы ввода и вывода и указаны в примерах исключительно для удобства их восприятия

**Пример 1**
```
(ввод) меч зелье щит
(ввод) топор зелье
(ввод) лук щит меч
(вывод) 0
```

**Пример 2**
```
(ввод) лук меч топор  
(ввод) меч лук  
(ввод) меч лук топор
(вывод) 2
```

**Пример 3**
```
(ввод) лук меч топор  
(ввод) меч луккк
(вывод) Неверный предмет, попробуйте снова
(ввод) меч лук
(ввод) меч лук топор
(вывод) 2
```

## Задача 6. Про Поросёнка Петра (0.5 балла)

На плоскости в точке (0,0) стоит Поросёнок Пётр. Он умеет ходить влево, вправо, вверх и вниз. Расстояние его прохода в какую-либо сторону измеряется в шагах. Когда он идет вправо, его первая координата увеличивается, когда влево - уменьшается. Когда он идет вверх, его вторая координата увеличивается, а когда вниз - уменьшается.

С клавиатуры считывается число N - число ходов, которые сделает Пётр. После чего на каждом шаге спрашивается, сколько шагов и в какую сторону за этот ход Пётр сделает. Так происходит, пока Пётр не осуществит все N ходов.

Программа должна вывести, сколько шагов Пётр должен был бы сделать, чтобы кратчайшим путем прибыть из своей начальной точки (0,0) в свою конечную точку. Напоминание: Пётр умеет ходить только вверх-вниз, и влево-вправо, но не по диагонали.

### _Примеры_

Пользовательский ввод в примере идёт после двоеточия и пробела:

**Пример 1**
```
Введите N: 3
Ход 1: Вверх
Ход 2: Вниз
Ход 3: Вверх
```
Вывод:
```
1
```

**Пример 2**
```
Введите N: 4
Ход 1: Вверх
Ход 2: Вверх
Ход 3: Вверх
Ход 4: Вправо
```
Вывод:
```
4
```

## Задача 7. Развернуть число (0.5 балла)

Вам на вход подается произвольное целое число. "Разверните" его, не используя преобразование к строке (это единственное ограничение)

**Пример 1:**

```
Ввод: 12345890
Вывод: 9854321
```

**Пример 2:**
```
Ввод: 10000
Вывод: 0
```
## Задача 8. Текст песни (1 балл)

Выполните следующие задания, связанные с редактированием текста песни. Хардкодить нельзя (считайте, что ваш функционал должен работать, если вместо данного текста будет подставлен текст другой песни в таком же формате)\
Используйте шаблон, предоставленный в файле `task_8.py`\
Полный текст песни также можно найти в файле `task_8.py`

При вводе пользователем числа должен быть выполнен соответствующий ему функционал. Если пользователь вводит "выход", программа прекращает выполнение. 

1)  **(0.33 балла)** Создайте отдельный список или словарь (подумайте, какая структура будет более удобной) для хранения:
	- куплета 1
	- куплета 2
	- предприпева 1
	- предприпева 2
	- припева
    
После ввода числа 1 (соответствующего номеру данного задания) пользователь может ввести название одного из этих элементов песни для его вывода. Пример:
```
Ввод: 1
Вввод: припев

Вывод: 
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
```

2)  **(0.33 балла)** Реализуйте вывод текста песни, выравненного по центру. Удалите метки типа [Куплет 1], [Припев] и т.д.
Пример (обрезано для краткости):

```
Ввод: 2
```

Вывод:

<div style="text-align: center;">

   
   В истерике кружилась мама Валя  
   На заднем фоне замер папа Толя  
   В радиусе метра воцарился жесточайший хаос  
   Когда всем понятно стало: сын остался без диплома  
   Мама, не кричи, хватит плакать, не смей  
   
...

   Вдруг увидел солнце — и тогда себе я сказал:  
												   
     
   Я выбираю — жить в кайф!  
   Я выбираю — жить в кайф!  
   Я выбираю — жить в кайф!  
   Я выбираю — жить в кайф!  

</div>

	
3) **(0.33 балла)** Реализуйте подсчет слов в тексте песни, который бы работал следующим образом. После ввода числа 3 (соответствующего номеру данного задания) пользователь может ввести:
	- "куплет". В таком случае выводятся 3 самых частых слова из всей песни, которая содержит только куплеты (т.е. слова из припевов и других частей не должны считаться)
	- "песня". В таком случае выводятся 3 самых частых слова из всей песни целиком

**Примечание 1**. Перед подсчетом количества слов:
- Переведите все слова в нижний регистр
- Удалите специальные символы (кроме слов, содержащих дефис)
- Приводить слова к начальной форме не нужно

**Примечание 2**. Вывод осуществляется в следующем формате:

```
1. "слово" - х раз
2. "слово" - х раз
3. "слово" - х раз
```


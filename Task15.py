#Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. Сделайте по одному вызову каждой из функций
def cat_voice():
  print('Meow!')

def dog_voice():
  print('Woof!')
cat_voice()
dog_voice()
#Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно. Выведите на экран 'Meow!' и 'Woof!' по 2 раза
def cat_voice():
  return 'Meow!'

def dog_voice():
  return 'Woof!'
print(cat_voice())
print(dog_voice())
print(cat_voice())
print(dog_voice())
#Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным знаком.
def get_voice(t):
  return t+'!'

def get_voice(text = ''):
  return str(text) + '!'

print(get_voice('Get voice'))

#Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться в форме объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него
def odd_numbers(a = 0, b = 0):
  odd_numbers_list = []
  for i in range(a,b + 1):
    if i % 2 !=0:
      odd_numbers_list.append(i)
  return odd_numbers_list

print(odd_numbers(0, 10))


def odd_numbers2(a = 0, b = 0):
  return [i for i in range(a, b + 1) if i % 2 != 0]

print(odd_numbers2(0, 10))

# второй вариант
# With List Comprehension
def get_odd_number_list(a, b):
  number_list = list(range(a, b + 1))
  odd_number_list = [number for number in number_list if number % 2 == 1]
  return odd_number_list
print(get_odd_number_list(4,14))


# Without List Comprehension
def get_odd_number_list(a, b):
  number_list = list(range(a, b + 1))
  odd_number_list = []
  for number in number_list:
    if number % 2 == 1:
      odd_number_list.append(number)
  return odd_number_list
print(get_odd_number_list(12,17))
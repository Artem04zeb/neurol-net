# 123
import random

# Каждая цифра, потом в общий массив цифр
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
# Список всех цифр от О до 9 в едином массиве
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# ctrl + /(eng)
# for num in nums:
#     k = 0
#     s = ''
#     for i in range(15):
#         s += str(num[i])
#         k += 1
#         if k == 3:
#             print(s)
#             s = ''
#             k = 0
#     print()

tema = 5  # Чему обучаем
n_sens = 15  # Кол-во сенсоров

weights = [0 for i in range(15)]  # Инициализация вессов для связей с сумматором


# Функция определяет, является ли полученное изображение цифрой 5
# Возвращает ДА, если признано, что это 5.
def perceptron(sensor):
    b = 7
    s = 0
    for i in range(n_sens):  #
        s += int(sensor[i]) * weights[i]
    if s >= b:
        return True  # Сумма превысила порог
    else:
        return False  # Порог не пройден


bb = 7  # Порог активации


# Уменьшение значений весов
# Если сеть ошиблась и выдала ДА при входной цифре, отличной от 5

def decrease_number(number):
    for i in range(n_sens):
        if int(number[i]) == 1:
            weights[i] -= 1


#  Увеличение значений весов
#  Если сеть не ошиблась и выдала ДА при поданной на вход цифре 5
def increase(number):
    for i in range(n_sens):
        if int(number[i]) == 1:
            weights[i] += 1


# Тренировка сети
n = 100000  # Кол-во уроков

for i in range(n):
    j = random.randint(0, 9)
    r = perceptron(nums[j])  # Результат обращения к сумматору (ответ ДА или НЕТ)

    if j != tema:  # Если генератор выдал случайное число j, не равное 5
        if r:  # Если сумматор сказал ДА(это пятёрка), а j это не 5. ОШИБСЯ
            decrease_number(nums[j])  # Наказываем сеть - уменьшаем значения весов
    else:  # Если генератор выдал случайное число j, равное 5
        if not r:
            increase(nums[tema])  # Поощряем сеть - увеличиваем значения весов

print(weights)

# print('0 is 5?', perceptron(num0))
# print('1 is 5?', perceptron(num1))
# print('2 is 5?', perceptron(num2))
# print('3 is 5?', perceptron(num3))
# print('4 is 5?', perceptron(num4))
# print('5 is 5?', perceptron(num5))
# print('6 is 5?', perceptron(num6))
# print('7 is 5?', perceptron(num7))
# print('8 is 5?', perceptron(num8))
# print('9 is 5?', perceptron(num9))

num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

print("5 is 51", perceptron(num51))
print("5 is 52", perceptron(num52))
print("5 is 53", perceptron(num53))
print("5 is 54", perceptron(num54))
print("5 is 55", perceptron(num55))
print("5 is 56", perceptron(num56))

















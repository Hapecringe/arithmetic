# Пример вычисления простой арифметики

# Функция для сложения двух чисел
def add(a, b):
    return a + b

# Функция для вычитания двух чисел
def subtract(a, b):
    return a - b

# Функция для умножения двух чисел
def multiply(a, b):
    return a * b

# Функция для деления двух чисел
def divide(a, b):
    # Проверка деления на ноль
    if b == 0:
        return "Ошибка: деление на ноль"
    else:
        return a / b

# Пример использования функций
num1 = 10
num2 = 5

print("Сложение:", add(num1, num2))
print("Вычитание:", subtract(num1, num2))
print("Умножение:", multiply(num1, num2))
print("Деление:", divide(num1, num2))

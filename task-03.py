import timeit
import re

# Завантаження текстових файлів
def load_text(filename):
    with open(filename, 'r', encoding='Windows-1251') as file:
        return file.read()

article1_text = load_text("article1.txt")
article2_text = load_text("article2.txt")

# Функція для виконання пошуку підрядка з використанням алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    return re.search(pattern, text)

# Функція для виконання пошуку підрядка з використанням алгоритму Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    return re.search(pattern, text)

# Функція для виконання пошуку підрядка з використанням алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern):
    return re.search(pattern, text)

# Завдання: Вимірювання часу виконання для реального та вигаданого підрядка на кожному тексті
# Для кожного алгоритму використовуйте функцію timeit.timeit() з відповідними аргументами
# І виведіть результати

# Реальний підрядок
real_pattern = "The"
# Вигаданий підрядок
fake_pattern = "Python"

# Вимірювання часу виконання для кожного алгоритму на статті 1 для реального підрядка
print("Boyer-Moore на статті 1 (реальний підрядок):", timeit.timeit(lambda: boyer_moore_search(article1_text, real_pattern), number=1))
print("KMP на статті 1 (реальний підрядок):", timeit.timeit(lambda: kmp_search(article1_text, real_pattern), number=1))
print("Rabin-Karp на статті 1 (реальний підрядок):", timeit.timeit(lambda: rabin_karp_search(article1_text, real_pattern), number=1))

# Вимірювання часу виконання для кожного алгоритму на статті 1 для вигаданого підрядка
print("Boyer-Moore на статті 1 (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(article1_text, fake_pattern), number=1))
print("KMP на статті 1 (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(article1_text, fake_pattern), number=1))
print("Rabin-Karp на статті 1 (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(article1_text, fake_pattern), number=1))

# Вимірювання часу виконання для кожного алгоритму на статті 2 для реального підрядка
print("Boyer-Moore на статті 2 (реальний підрядок):", timeit.timeit(lambda: boyer_moore_search(article2_text, real_pattern), number=1))
print("KMP на статті 2 (реальний підрядок):", timeit.timeit(lambda: kmp_search(article2_text, real_pattern), number=1))
print("Rabin-Karp на статті 2 (реальний підрядок):", timeit.timeit(lambda: rabin_karp_search(article2_text, real_pattern), number=1))

# Вимірювання часу виконання для кожного алгоритму на статті 2 для вигаданого підрядка
print("Boyer-Moore на статті 2 (вигаданий підрядок):", timeit.timeit(lambda: boyer_moore_search(article2_text, fake_pattern), number=1))
print("KMP на статті 2 (вигаданий підрядок):", timeit.timeit(lambda: kmp_search(article2_text, fake_pattern), number=1))
print("Rabin-Karp на статті 2 (вигаданий підрядок):", timeit.timeit(lambda: rabin_karp_search(article2_text, fake_pattern), number=1))

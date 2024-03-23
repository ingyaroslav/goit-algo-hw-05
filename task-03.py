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

# Функція для вимірювання часу виконання кожного алгоритму пошуку підрядка для кожного тексту
def measure_algorithm_speeds(text, real_pattern, fake_pattern):
    results = {}
    
    # Вимірювання часу виконання для реального підрядка
    results['Boyer-Moore'] = timeit.timeit(lambda: boyer_moore_search(text, real_pattern), number=1)
    results['KMP'] = timeit.timeit(lambda: kmp_search(text, real_pattern), number=1)
    results['Rabin-Karp'] = timeit.timeit(lambda: rabin_karp_search(text, real_pattern), number=1)
    
    # Вимірювання часу виконання для вигаданого підрядка
    results['Boyer-Moore fake'] = timeit.timeit(lambda: boyer_moore_search(text, fake_pattern), number=1)
    results['KMP fake'] = timeit.timeit(lambda: kmp_search(text, fake_pattern), number=1)
    results['Rabin-Karp fake'] = timeit.timeit(lambda: rabin_karp_search(text, fake_pattern), number=1)
    
    return results

# Визначення реального та вигаданого підрядків
real_pattern = "The"
fake_pattern = "Python"

# Вимірювання часу виконання кожного алгоритму для кожного тексту
article1_results = measure_algorithm_speeds(article1_text, real_pattern, fake_pattern)
article2_results = measure_algorithm_speeds(article2_text, real_pattern, fake_pattern)

# Визначення найшвидшого алгоритму для кожного тексту
article1_fastest_algorithm = min(article1_results, key=article1_results.get)
article2_fastest_algorithm = min(article2_results, key=article2_results.get)

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

print("Найшвидший алгоритм для статті 1:", article1_fastest_algorithm)
print("Найшвидший алгоритм для статті 2:", article2_fastest_algorithm)
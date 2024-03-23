## Висновки *(task-03.py)*
Після аналізу близько десятка результатів можемо зробити наступні висновки:
### Для статті 1:
1. Реальний підрядок:
   * Найшвидший алгоритм: Rabin-Karp.
   * Результати алгоритмів в порядку швидкості: Rabin-Karp, Boyer-Moore, KMP.
2. Вигаданий підрядок:
   * Найшвидший алгоритм: Rabin-Karp.
   * Результати алгоритмів в порядку швидкості: Rabin-Karp, Boyer-Moore, KMP.
### Для статті 2:
1. Реальний підрядок:
   * Найшвидший алгоритм: Rabin-Karp.
   * Результати алгоритмів в порядку швидкості: Rabin-Karp, Boyer-Moore, KMP.
2. Вигаданий підрядок:
   * Найшвидший алгоритм: KMP.
   * Результати алгоритмів в порядку швидкості: KMP, Boyer-Moore, Rabin-Karp.
### Загальні висновки:
* **Rabin-Karp** виявився найшвидшим алгоритмом для пошуку підрядка у текстах з обох статей, особливо коли підрядок реальний.
* У випадку реального підрядка **KMP** виявився другим за швидкістю для статті 1, але для статті 2 був третім.
* **Boyer-Moore** був найшвидшим для статті 2, коли підрядок був вигаданий, але для статті 1 його швидкість була середньою.
* Швидкість алгоритмів може значно відрізнятися в залежності від тексту та підрядка. В цілому, **Rabin-Karp** може бути хорошим вибором для пошуку підрядка у текстах, а **KMP** ефективний для деяких типів підрядків. **Boyer-Moore** також може бути швидким, але його ефективність може коливатися в залежності від тексту.
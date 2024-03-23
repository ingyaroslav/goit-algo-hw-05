class HashTable:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data  # Замінюємо існуюче значення
                return
            # Колізії: використовуємо лінійне пробування для пошуку вільної позиції
            index = (index + 1) % self.size
        # Зберігаємо ключ та значення
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            # Колізії: використовуємо лінійне пробування
            index = (index + 1) % self.size
        # Ключ не знайдено
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            # Колізії: використовуємо лінійне пробування
            index = (index + 1) % self.size

    def hash_function(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % self.size
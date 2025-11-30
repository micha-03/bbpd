# Практическая работа №5 - Операции с массивами
# Вариант 20
import random

class OperacionesMatriz:
    def __init__(self):
        self.matriz = []
        self.filas = 0
        self.columnas = 0
    
    def crear_matriz_ejemplo(self):
        """Создать пример матрицы для тестирования"""
        self.matriz = [
            [1, 2, 3, 4],
            [5, 6, 7, 8], 
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.filas = 4
        self.columnas = 4
        print("Пример матрицы создан:")
        self.mostrar_matriz()
    
    def ingresar_tamano(self):
        """Функция 1: Ввод размера массива"""
        try:
            self.filas = int(input("Введите количество строк: "))
            self.columnas = int(input("Введите количество столбцов: "))
            if self.filas <= 0 or self.columnas <= 0:
                print("Ошибка: Размер должен быть положительным")
                return False
            print(f"Размер установлен: {self.filas}x{self.columnas}")
            return True
        except ValueError:
            print("Ошибка: Введите корректные числа")
            return False
    
    def crear_matriz_manual(self):
        """Создать матрицу manualmente"""
        self.matriz = []
        print("Ручной ввод элементов:")
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                while True:
                    try:
                        valor = int(input(f"Элемент [{i},{j}]: "))
                        fila.append(valor)
                        break
                    except ValueError:
                        print("Введите корректное число")
            self.matriz.append(fila)
        print("Массив создан вручную")
    
    def crear_matriz_automatica(self):
        """Создать матрицу automáticamente"""
        self.matriz = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(random.randint(0, 100))
            self.matriz.append(fila)
        print("Массив создан автоматически")
    
    def crear_matriz(self):
        """Функция 2: Создание массива"""
        if self.filas == 0 or self.columnas == 0:
            print("Сначала введите размер массива")
            return
        
        print("\n1. Ручной ввод")
        print("2. Автоматическое заполнение (0-100)")
        print("3. Назад")
        
        opcion = input("Выберите опцию: ")
        
        if opcion == "1":
            self.crear_matriz_manual()
        elif opcion == "2":
            self.crear_matriz_automatica()
    
    def mostrar_matriz(self):
        """Функция 3: Просмотр созданного массива"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        print(f"\nМассив {self.filas}x{self.columnas}:")
        for i in range(self.filas):
            for j in range(self.columnas):
                print(f"{self.matriz[i][j]:4}", end=" ")
            print()

    def funcion_4(self):
        """Функция 4: Сумма элементов с нечетными индексами"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        suma_total = 0
        elementos = []
        
        for i in range(self.filas):
            for j in range(self.columnas):
                if i % 2 == 1 and j % 2 == 1:
                    suma_total += self.matriz[i][j]
                    elementos.append(f"[{i},{j}]={self.matriz[i][j]}")
        
        print(f"Элементы с нечетными индексами: {', '.join(elementos)}")
        print(f"Общая сумма: {suma_total}")
        return suma_total
    
    def funcion_6(self):
        """Функция 6: Сумма по строкам и столбцам"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        print("\nСумма по строкам:")
        for i in range(self.filas):
            suma_fila = sum(self.matriz[i])
            print(f"Строка {i}: {suma_fila}")
        
        print("\nСумма по столбцам:")
        for j in range(self.columnas):
            suma_columna = 0
            for i in range(self.filas):
                suma_columna += self.matriz[i][j]
            print(f"Столбец {j}: {suma_columna}")
    
    def funcion_7(self):
        """Функция 7: Главная и побочная диагонали"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        print("Главная диагональ:")
        diagonal_principal = []
        for i in range(min(self.filas, self.columnas)):
            diagonal_principal.append(str(self.matriz[i][i]))
        print("[" + ", ".join(diagonal_principal) + "]")
        
        print("Побочная диагональ:")
        diagonal_secundaria = []
        for i in range(min(self.filas, self.columnas)):
            j = self.columnas - 1 - i
            diagonal_secundaria.append(str(self.matriz[i][j]))
        print("[" + ", ".join(diagonal_secundaria) + "]")
    
    def funcion_16(self):
        """Функция 16: Строки с числом 10"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        filas_con_10 = []
        for i in range(self.filas):
            if 10 in self.matriz[i]:
                filas_con_10.append(i)
        
        if filas_con_10:
            print(f"Строки, содержащие хотя бы одну 10: {filas_con_10}")
        else:
            print("Нет строк, содержащих число 10")
        
        return filas_con_10
    
    def funcion_27(self):
        """Функция 27: Удалить столбец с максимальным элементом"""
        if not self.matriz:
            print("Массив не создан")
            return
        
        # Найти максимальный элемент и его столбец
        max_valor = self.matriz[0][0]
        columna_max = 0
        
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] > max_valor:
                    max_valor = self.matriz[i][j]
                    columna_max = j
        
        print(f"Максимальный элемент: {max_valor} в столбце {columna_max}")
        
        if self.columnas > 1:
            # Создать новую матрицу без столбца с максимумом
            nueva_matriz = []
            for i in range(self.filas):
                nueva_fila = []
                for j in range(self.columnas):
                    if j != columna_max:
                        nueva_fila.append(self.matriz[i][j])
                nueva_matriz.append(nueva_fila)
            
            self.matriz = nueva_matriz
            self.columnas -= 1
            print("Столбец удален. Новый массив:")
            self.mostrar_matriz()
        else:
            print("Невозможно удалить, только один столбец")

def main():
    operaciones = OperacionesMatriz()
    
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ - ОПЕРАЦИИ С МАССИВАМИ")
        print("="*50)
        print("1. Ввод размера массива")
        print("2. Создание массива")
        print("3. Просмотр созданного массива")
        print("4. Выполнение функций")
        print("5. Выход")
        
        opcion = input("Выберите опцию: ")
        
        if opcion == "1":
            operaciones.ingresar_tamano()
        elif opcion == "2":
            operaciones.crear_matriz()
        elif opcion == "3":
            operaciones.mostrar_matriz()
        elif opcion == "4":
            if not operaciones.matriz:
                print("Сначала создайте массив")
                continue
                
            print("\nДОСТУПНЫЕ ФУНКЦИИ:")
            print("a. Функция 4: Сумма элементов с нечетными индексами")
            print("b. Функция 6: Сумма по строкам и столбцам")
            print("c. Функция 7: Главная и побочная диагонали")
            print("d. Функция 16: Строки с числом 10")
            print("e. Функция 27: Удалить столбец с максимумом")
            print("f. Назад")
            
            opcion_funcion = input("Выберите функцию: ").lower()
            
            if opcion_funcion == "a":
                operaciones.funcion_4()
            elif opcion_funcion == "b":
                operaciones.funcion_6()
            elif opcion_funcion == "c":
                operaciones.funcion_7()
            elif opcion_funcion == "d":
                operaciones.funcion_16()
            elif opcion_funcion == "e":
                operaciones.funcion_27()
            elif opcion_funcion == "f":
                continue
            else:
                print("Неверная опция")
        elif opcion == "5":
            print("До свидания!")
            break
        else:
            print("Неверная опция")

if __name__ == "__main__":
    main()
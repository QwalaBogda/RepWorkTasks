#Задание №1
def multiplication_table(n):
    print(" " * 4, end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print()

    for i in range(1, n + 1):
        print(f"{i:4}", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

#если нужно ввести число 1-10
#s1=int(input())

#пример из задания с 5
multiplication_table(5)

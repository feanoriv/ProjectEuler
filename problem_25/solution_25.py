from my_tools.tools import timer

"""
Задача 25
Последовательность Фибоначчи определяется рекурсивным правилом:
Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
Таким образом, первые 12 членов последовательности равны:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?
"""


@timer
def problem_25(n=1000) -> int:
    a1, a2, f = 1, 1, 2
    while True:
        a1, a2 = a2, a1 + a2
        f += 1
        if len(str(a2)) >= n:
            return f


if __name__ == "__main__":
    print(problem_25())

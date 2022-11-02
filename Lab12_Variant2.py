import sys

if len(sys.argv) != 2:
    print("Имя файла необходимо передать в качестве аргумента.")
    quit()

try:
    inf = open(sys.argv[1], "r")
except FileNotFoundError:
    print("Файл ", sys.argv[1], " не найден. Попробуйте еще.")
    quit()

line = inf.readlines()
print(*line[-10:], sep=' ')

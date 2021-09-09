from webbrowser import open
from random import choice, randint
from string import ascii_lowercase
from time import sleep
link = []
while True:
    try:
        repeats = int(input("Ile razy ma być wylosowany link: "))
        break
    except ValueError:
        print("Wprowadź liczbę!")
for i in range(repeats):
    a = choice(ascii_lowercase) + choice(ascii_lowercase) + str(randint(1000, 9999))
    link.append(a)
for i in range(repeats):
    open(f"https://prnt.sc/{link[i]}", new=2)
    sleep(5)

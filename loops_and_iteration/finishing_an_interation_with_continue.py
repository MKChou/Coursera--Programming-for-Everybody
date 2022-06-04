from ast import While

from regex import P


while True:
    line = input("enter a number:")
    if line == "aaa":
        continue
    if line == "done":
        break
    print(line)
print("all done")

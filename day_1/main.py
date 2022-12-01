import time

def exercise_1():
    """Calculate the top calories carried by one elf"""
    amount = 0
    top = 0

    with open("./input.txt") as file:
        for index, line in enumerate(file):
            if line.strip():
                amount += int(line)
            else:
                # Empty line aka next elf after this line, use this line to calculate top calories
                if amount > top:
                    top = amount
                amount = 0

    print("Most amount of calories carried by one elf:", top)

def exercise_2():
    """Calculate the top calories carried by the top 3 elves"""
    amount = 0
    top = [0, 0, 0]  # max length of 3

    with open("./input.txt") as file:
        for line in file:
            if line.strip():
                amount += int(line)
            else:
                # Empty line aka next elf after this line, use this line to calculate top calories
                for index, calories in enumerate(top):
                    if amount > calories:
                        top.insert(index, amount)
                        top.pop()
                        break
                amount = 0

    print("Top 3 calories carried by elves:", top, "\nWith a total of:", sum(top))

def main():
    """Time and run all exercises"""
    tick = time.perf_counter()
    exercise_1()
    tock = time.perf_counter()
    print(f"Ran the first exercise in: {tock - tick:04f} seconds")

    tick2 = time.perf_counter()
    exercise_2()
    tock2 = time.perf_counter()
    print(f"Ran the second exercise in: {tock2 - tick2:04f} seconds")

if __name__ == "__main__":
    main()
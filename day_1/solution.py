from operator import le
import os

if __name__ == "__main__":
    # +'/adventofcode_2021_day_1_input.txt'
    print("start")
    input_path = os.path.join(os.getcwd(), 'adventofcode_2021_day_1_input.txt')
    print(input_path)

    file = open(input_path)
    line = file.readline()
    count = 0
    while line:
        next = file.readline()
        if next > line:
            count = count + 1
        line = next
    file.close()

    print(count)


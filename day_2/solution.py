from operator import le
import os

def solution():
    root_path = os.path.dirname(__file__)
    input_path = os.path.join(root_path, 'input.txt')

    file = open(input_path)
    line = file.readline()
    horizontal, vertical = 0, 0
    while line:
        line = line.replace('\n', '')
        action, v = line.split(' ')
        if action == 'forward':
            horizontal+=int(v)
        elif action == 'up':
            vertical-=int(v)
        elif action == 'down':
            vertical+=int(v)
        line = file.readline()
    file.close()
    print(horizontal * vertical)

if __name__ == "__main__":
    solution()


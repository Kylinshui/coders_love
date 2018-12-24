#!/bin/usr/python3
import time
def main(words="I LOVE U"):
  for c in words.split():
    line = []
    for y in range(15, -15, -1):
        line_c = []
        letters = ''
        for x in range(-30, 30):
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += c[(x-y) % len(c)]
            else:
                letters += ' '
        line_c.append(letters)
        line += line_c
    print('\033[1;31m')
    print('\n'.join(line))
    print('\033[0m')
    time.sleep(1)

if __name__ == '__main__':
    main("L Y Y I L O V E Y O U")

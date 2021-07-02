import pycom
import time

pycom.heartbeat(False)

black = 0x000000
blue = 0x0000FF
red = 0xFF0000

letters = {' ': ' ',
           'A': '.-',
           'B': '-...',
           'C': '-.-.',
           'D': '-..',
           'E': '.',
           'F': '..-.',
           'G': '--.',
           'H': '....',
           'I': '..',
           'J': '.---',
           'K': '-.-',
           'L': '.-..',
           'M': '--',
           'N': '-.',
           'O': '---',
           'P': '.--.',
           'Q': '--.-',
           'R': '.-.',
           'S': '...',
           'T': '-',
           'U': '..-',
           'V': '...-',
           'W': '.--',
           'X': '-..-',
           'Y': '-.--',
           'Z': '--..'}


def dot():
    pycom.rgbled(blue)
    time.sleep(0.2)
    pycom.rgbled(black)
    time.sleep(0.2)


def dash():
    pycom.rgbled(red)
    time.sleep(0.5)
    pycom.rgbled(black)
    time.sleep(0.2)


input = 'HELLO WORLD'
for letter in input:
    for symbol in letters[letter.upper()]:
        if symbol == '-':
            dash()
        elif symbol == '.':
            dot()
        else:
            time.sleep(0.5)
    time.sleep(0.5)


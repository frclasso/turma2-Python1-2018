#!/usr/bin/env python3

import time

seconds = 4
while seconds != 0:
    print(f"Voce tem {seconds} segundos para respoder...>")
    time.sleep(2)
    seconds -=1
print('Game Over, You Will Die!')
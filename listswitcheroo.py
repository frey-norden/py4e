#!/usr/bin/python3
# File: listswitcheroo.py


def lotto():
    lotto = [2, 14, 26, 41, 63]
    print('Here are lotto nums:', lotto)
    print("Let's change the second value")
    a = input('Pick a number: ')
    lotto[1] = int(a)
    print("Here are you're new numbers", lotto)
def guess():
    lotto = [2, 14, 26, 41, 63]
    x = False
    print(len(lotto), '**Just a hint**wink,wink**')
    val = len(lotto)
    while x == False:
        try:
            fråga = input('How many values in lotto numbers: ')
        except:
            print('Bro, it has to be a number')
            quit()
        if int(fråga) == val:
            break
    print('Right answer.')

def main():
    lotto()
    guess()

if __name__ == "__main__":
    main()

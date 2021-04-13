from random import randint

def play():
    rand_int = randint(0,700)
    #print(rand_int)

    while True:
        intnumber = int(input("please input a number:"))

        if intnumber == rand_int:
            print(f"you found the number ({rand_int}), congratulation!")
            break

        elif intnumber < rand_int:
            print("the number you input is less than the number we guess.")
            continue

        elif intnumber > rand_int:
            print("the number you input is bigger than the number we guess.")
            continue

if __name__ == "__main__":
    play()
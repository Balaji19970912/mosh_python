secret_number = 9

guess_count = 0;

guess_limit = int(input("How many guess limits you want ? "))
# print(guess_limit)

while guess_count <= guess_limit:
    guess_count += 1
    print("\n")
    guess_number = int(input("Guess the number : "))
    if(guess_number == secret_number):
        print("You Won!")
        break
    else:
        print('Try Again!\n')
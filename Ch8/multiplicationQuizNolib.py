import random
import time, inputimeout

count_correct = 0
for i in range(1, 11):
    num1, num2 = random.randint(0, 9), random.randint(0, 9)
    print("#%s %s x %s:\n" % (i, num1, num2))
    try:
        guess = int(inputimeout.inputimeout(prompt="> ", timeout=8))
    except ValueError:
        print("Only numbers are allowed\n")
        continue
    except inputimeout.TimeoutOccurred:
        print("Incorrect (timed out). Moving on...")
        continue

    if guess == num1 * num2:
        count_correct += 1
        print("Correct")
        time.sleep(1)
    else:
        n_attepmts = 1
        while n_attepmts != 3:
            print("Incorrect. You have %s more attempts" % (3 - n_attepmts))
            guess = int(input("> "))
            if guess == num1 * num2:
                print("Correct")
                time.sleep(1)
                count_correct += 1
                break

            else:
                n_attepmts += 1


print("%s/%s" % (count_correct, 10))

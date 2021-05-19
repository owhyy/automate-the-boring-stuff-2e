
import random

def head_tails(number_of_tosses):
    toss_list = []
    number_of_streaks = 0
    for toss in range(number_of_tosses):
        toss_list.append(random.randint(0, 1)) # 0 is head 1 is tails
   
    for toss in range(number_of_tosses):
        if toss_list[toss : toss + 6] == [0, 0, 0, 0, 0, 0] or toss_list[toss : toss + 6] == [1, 1, 1, 1, 1, 1]:
            number_of_streaks += 1
    return number_of_streaks/100
print(head_tails(10000))

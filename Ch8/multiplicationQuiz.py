import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)  # choose 2 random numbers between 0->10
    num2 = random.randint(0, 9)
    prompt = "#%s: %s x %s\n> " % (question_number, num1, num2)  # question format
    try:
        pyip.inputStr(
            prompt,  # print the question
            allowRegexes=[
                "^%s$" % (num1 * num2)
            ],  # allow only numbers that are num1 * num2
            blockRegexes=[(".*", "Incorrect!")],  # and block anything else
            timeout=8,  # 8 seconds max
            limit=3,  # 3 tries max
        )
    except pyip.TimeoutException:  # if no time:
        print("Out of time!")
        break
    except pyip.RetryLimitException:  # if no more tries:
        print("Out of tries!")
        break
    else:
        print("Correct!")
        correct_answers += 1  # increment the score
        time.sleep(1)  # and wait 1 sec to display
print(
    "Score: %s / %s" % (correct_answers, number_of_questions)
)  # print the score after finishing

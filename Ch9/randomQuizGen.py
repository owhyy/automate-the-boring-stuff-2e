import random

# randomize 35 pop-quizzes based on 50 multiple-choice options in random order

capitals = {  # list of possible choices
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

for quiz_num in range(35):  # for every quiz:
    quiz_f = open(f"capitalsquiz{quiz_num + 1}.txt", "w")  # open  quiz file as write
    answer_key_f = open(
        f"capitalsquiz_answers{quiz_num + 1}.txt", "w"
    )  # open file which contains the answers

    quiz_f.write(
        "Name:\n\nDate:\n\nPeriod:\n\n"
    )  # print a form for the name, date and period
    quiz_f.write(
        (" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})"
    )  # print the title and the nr of the quiz
    quiz_f.write("\n\n")
    states = list(capitals.keys())  # name of states
    random.shuffle(states)  # randomize them

    for question_num in range(50):  # for every question

        # correct answer is a random capital
        correct_answer = capitals[states[question_num]]

        # make a copy of all the capitals
        wrong_answers = list(capitals.values())
        # delete the current correct answer from list of wrong values
        del wrong_answers[wrong_answers.index(correct_answer)]

        wrong_answers = random.sample(wrong_answers, 3)  # select 3 random wrong answers
        answer_options = wrong_answers + [correct_answer]
        # 4 answer options: 3 wrong, 1 correct

        random.shuffle(answer_options)  # shuffle answer options

        quiz_f.write(
            f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
        )  # write to quiz file

        for i in range(4):
            quiz_f.write(f"{'ABCD'[i]}. {answer_options[i]}\n")
            # write 4 answer options

            answer_key_f.write(
                f"{question_num + 1}.{'ABCD'[answer_options.index(correct_answer)]}\n"  # write the correct values in file
            )
        quiz_f.write("\n")
    quiz_f.close()
    answer_key_f.close()

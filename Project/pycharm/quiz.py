from myClass import Question

list_of_questions = [
    "1. What is the current club of Eden Hazard?\n(a) Chelsea\n(b) Real Madrid\n(c) Lille\n(d) Kopenhagen\n\n",
    "2. What number is Emerson Palmieri wearing at Chelsea?\n(a) 33\n(b) 3\n(c) 27\n(d) 15\n\n",
    "3. Which club was the last England team to won the UCL?\n(a) Man City\n(b) Liverpool\n(c) Chelsea\n(d) Man Utd\n\n",
    "4. Who is the best player in the world?\n(a) Lionel Messi\n(b) Eden Hazard\n(c) Van Dijk\n(d) Cristiano Ronaldo\n\n",
    "5. Which manager has manged to win Champion League with 2 different clubs?\n(a) Pep Guardiola\n(b) Zinedine Zidane\n(c) Jose Mourinho\n(d) Jurgen Klop\n\n",
    "6. How many times did Liverpool win the UCL?\n(a) 5\n(b) 6\n(c) 7\n(d) 8\n\n"
]

question_prompt = [
    Question(list_of_questions[0], "b"),
    Question(list_of_questions[1], "a"),
    Question(list_of_questions[2], "b"),
    Question(list_of_questions[3], "d"),
    Question(list_of_questions[4], "c"),
    Question(list_of_questions[5], "b"),
]

def runtest(questions):
    score = 0
    print("Type in the correct answer for these following question: ")
    for question in questions:
        print(question.prompt)
        ans = input("Type in the correct answer for this question: ")
        if ans == question.answer:
            score += 1
            print("Nice job, bitch!\n\n")
        else:
            print(':)\n')
    if score == 0:
        print('YOU ARE ALL WRONG! You suck!!')
    else:
        print('You got', score, "out of", len(questions),'questions. Congratulation')

runtest(question_prompt)

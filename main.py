from questions import questions

print("Only Type a or b or c")

question_prompts = [
    "Largest Software Company in the world - \n" "a. Microsoft\n" "b. IBM\n" "c. Banglalink\n\n",
    "Creator of Facebook - \n" "a. Mark Abulburg\n" "b. Mark Rohimburg\n" "c. Mark Zuckerburg\n\n",
    "Top search engine - \n" "a. Duckduckgo\n" "b. Google\n" "c. Bing\n\n",
    "Programming Language - \n" "a. Python\n" "b. Physics\n" "c. Biology\n\n",
    "Computer understand - \n" "a. 0 & 1\n" "b. 1 & 2\n" "c. 4 & 0\n\n",
]

question = [
    questions(question_prompts[0], "a"),
    questions(question_prompts[1], "c"),
    questions(question_prompts[2], "b"),
    questions(question_prompts[3], "a"),
    questions(question_prompts[4], "a"),
]
def run_test(question):
    score = 0
    for questions in question:
        answer = input(questions.prompt)
        if answer == (questions.answer):
            score += 1
    print("YOU GOT " + str(score) + " OUT OF " + str(len(question)))


run_test(question)

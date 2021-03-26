class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

print("Enter a or b or c only")

question_list = [
    "Largest Software Company in the world - \n" "a. Microsoft\n" "b. IBM\n" "c. Banglalink\n\n",
    "Creator of Facebook - \n" "a. Mark Abulburg\n" "b. Mark Rohimburg\n" "c. Mark Zuckerburg\n\n",
    "Top search engine - \n" "a. Duckduckgo\n" "b. Google\n" "c. Bing\n\n",
    "Programming Language - \n" "a. Python\n" "b. Physics\n" "c. Biology\n\n",
    "Computer understand - \n" "a. 0 & 1\n" "b. 1 & 2\n" "c. 4 & 0\n\n",
]

questions = [
    question(question_list, "a"),
    question(question_list, "c"),
    question(question_list, "b"),
    question(question_list, "a"),
    question(question_list, "a"),
]

def run_test (question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == answer.prompt:
        score += 1

    print ("YOU GOT " + str(score) + " OUT OF " + str(len(questions)))

run_test(question)

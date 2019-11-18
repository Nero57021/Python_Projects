from Question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green\n(b) purple \n(c) orange \n:",
    "which do you like more? \n(a) Cars \n(b) shoes \n(c) Gadgets \n:"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[1], "b"),
]


def run_test(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Correct answer " + str(score) + " out of " + str(len(questions)))


# driver code
run_test(questions)

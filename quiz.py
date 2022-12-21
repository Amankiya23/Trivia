# -------------------------
class trivia_question():
    def question_big(self):
        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions_big:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions_big.get(key), guess)
            question_num += 1


        display_score(correct_guesses, guesses)


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions_big:
        print(questions_big.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions_big)) * 100)
    print("Your score is: " + str(score) + "%")


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


questions_big = {
    "How many players are there in a basketball game?": "A",
    "Who was the first president of the U.S?": "B",
    "In which year the first covid-19 case was discovered?": "C",
    "How many continents are there in the world?": "A",
    "How many planets are there in the solar system?": "D",
    "What is the capital city of Spain?": "B",
    "What was the first soft drink in space?": "B",
    "Who holds the record for 100 metres dash?": "C",
    "What’s the hardest rock?": "A",
    "How many states does the U.S is have?": "B"
}

options = [["A. 10", "B. 5", "C. 12", "D. 8"],
           ["A. Abraham Lincoln", "B. George Washington", "C. John Tyler", "D. John Adams"],
           ["A. 2018", "B. 2001", "C. 2019", "D.2020"],
           ["A. Seven", "B. Five", "C. Four", "D. Six"],
           ["A. Six", "B. Seven", "C. Nine", "D. Eight"],
           ["A. Barcelona", "B. Madrid", "C. Lisbon", "D. Paris"],
           ["A. Water", "B. Coca Cola", "C. Fanta", "D. Pepsi"],
           ["A. Asafa Powell", "B. Yohan Blake", "C. Usain Bolt", "D. Tyson Gay"],
           ["A. Diamond", "B. Corundum", "C. Quartz", "D. Apatite"],
           ["A. 48", "B. 50", "C. 51", "D. 52"]]


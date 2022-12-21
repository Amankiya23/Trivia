from server import filled
# ----------------------------------
class trivia_question_pro():
    def question_pro(self):
        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions_pro:
            print("__________________________")
            print(key)
            for i in options_pro[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions_pro.get(key), guess)
            question_num += 1
        display_score(correct_guesses, guesses)
        filled()


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for p in questions_pro:
        print(questions_pro.get(p), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions_pro)) * 100)
    print("Your score is: " + str(score) + "%")

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0



questions_pro = {
    "What is Earth's largest continent?: ": "A",
    "What's the smallest country in the world?: ": "B",
    "Area 51 is located in which U S state?: ": "C",
    "What country has the most natural lakes?: ": "A",
    "How old is the universe?:": "B",
    "What are the three primary colors?:": "B",
    "How many bones does a human body have?": "A",
    "Which planet has the most gravity in the solar system?": "C",
    "What is the height of the tallest man in the world in 2021?": "D",
    "What is the most valued company in the world?": "A",
    "Who created python?": "B",
    "How many oceans are there in the world?": "A",
    "What is the distance between earth and mars?": "A",
    "In which year the first windows version was released?": "D"
}

options_pro = [["A. Asia", "B. Africa", "C. America", "D. Europe"],
               ["A. Croatia", "B. Vatican City", "C. uganda", "D. peru"],
               ["A. Los_angeles", "B. Texas", "C.Nevada", "D. canada"],
               ["A. Canada", "B. Italia", "C. Brazil", "D. Egypt"],
               ["A. 5.3 billion years old", "B. 13.8 billion years old", "C. 115.5 billion years ago",
                "D. 241.1 billion years old"],
               ["A. Red, yellow, and green", "B. Red, yellow, and blue", "C. Green, red, and blue",
                "D. Black, yellow, and red"],
               ["A. 206", "B. 54", "C. 251", "D. 180"],
               ["A. Neptune", "B. Mars", "C. Jupiter", "D. Earth"],
               ["A. 2.35 meters", "B. 2.47 meters", "C. 2.71 meters", "D. 2.51 meters"],
               ["A. Apple", "B. Google", "C. Microsoft", "D. Amazon"],
               ["A. Brendan Eich", "B. Van Rossum", "C. Bjarne Stroustrups", "D. Dennis Ritchie"],
               ["A. Five", "B. Ten", "C. Seven", "D. Three"],
               ["A. 366.82 million km", "B. 251.87 million km", "C. 1.578 milion km", "D. 350.34 milion km"],
               ["A. 1999", "B. 2001", "C. 1983", "D. 1985"]]


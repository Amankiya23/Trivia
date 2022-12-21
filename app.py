from quiz import trivia_question
from quizpro import trivia_question_pro



def app():
    while True:
        print("\t\t\t\t\t\tWELLCOME TO TRIVIA QUIZ GAME: ")
        print("\t\t\t\t\t\tplease Select the Category below")
        print("\tEnter 1 For Beginner")
        print("\tEnter 2 For professional ")
        choice = input("In which topic you interested : ")
        if choice == "1":
            print("\nWelcome to quiz for beginners Trivia Question\n")

            c = trivia_question()
            c.question_big()

        elif choice == "2":
            print("\nWelcome to Professional Trivia Question\n")

            d = trivia_question_pro()
            d.question_pro()

        stop = input("Do you want to play? \ty/n: ")
        if stop == "y":
            app()
        elif stop == "n":
            print("\t\t\t\tThank you for playing with us")
            break



app()

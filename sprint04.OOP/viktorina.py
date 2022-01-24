# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла
import sys, pickle
records = []
f = open("picklesviktorina", "wb")


def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding="utf-8")
    except IOError as e:
        print("невозможно открыть файл", file_name, ". Работа программы будет завершена \n", e)
        input("\n нажмите Ентер что бы выйти")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Return formatted string of game file"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """return next block of data from game file"""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    points = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)
    return category, question, answers, correct,points, explanation


def welcome(title):
    """welcomes player and tell him theme of the game"""
    print("\t\t Welcome in game 'victorina'\n")
    print("\t\t", title, "\n")


def main():
    name = input("Enter your name: ")
    trivia_file = open("trivia.txt", "r", encoding="utf-8")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # output first block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:

        # output question on the screen
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # incoming answer
        answer = input("Your answer: ")

        # check answer
        if answer == correct:
            print("\nNice!", end="")
            points = int(points)
            score += points


        else:
            print("\nNo", end="")
        print(explanation)
        print("score: ", score, "\n\n")
        # switch to the next question
        category, question, answers, correct, points, explanation = next_block(trivia_file)
    trivia_file.close()
    print("It was last question!")
    records.append(f"'{name}':{score}")
    print(f"Mr.{name} your score is, {score}")
    pickle.dump(records, f)
    print(records)
    f.close()

main()
input("\n\n press Enter to exit.")



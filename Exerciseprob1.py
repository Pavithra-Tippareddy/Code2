def check_input(tested_sentence: str, result: str = "Too short"):
    if len(tested_sentence) >= 10:
        if "X" in tested_sentence:
            result = tested_sentence + "\nX spotted!"
        else:
            result = tested_sentence
    return result


def main():
    while True:
        sentence = input("Write something (quit ends): ")
        if sentence == "quit":
            break
            print(check_input(sentence))


if __name__ == '__main__':
    main()
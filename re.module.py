def morse_number(str_char):
    result = []
    for char in str_char:
        if char == "1":
            result.append(".----")
        elif char == "2":
            result.append("..---")
        elif char == "3":
            result.append("...--")
        elif char == "4":
            result.append("....-")
        elif char == "5":
            result.append(".....")
        elif char == "6":
            result.append("-....")
        elif char == "7":
            result.append("--...")
        elif char == "8":
            result.append("---..")
        elif char == "9":
            result.append("----.")
        elif char == "0":
            result.append("-----")
    return " ".join(result)

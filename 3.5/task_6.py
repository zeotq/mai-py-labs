translit_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ъ": "",
    "Ь": ""
}


def eu_ru_translit(text: str = "Hello") -> str:
    encoded_text = ''
    for i in text:
        if i.upper() in translit_dict:
            if i.islower():
                encoded_text += translit_dict[i.upper()].lower()
            else:
                encoded_text += translit_dict[i].capitalize()
        else:
            encoded_text += i
    return encoded_text


def main():
    FILE_INPUT = open("task_6_in.txt", encoding="UTF-8")
    FILE_OUTPUT = open("task_6_out.txt", "w")

    result = list(map(eu_ru_translit, FILE_INPUT.readlines()))    
    FILE_OUTPUT.writelines(result)

    FILE_INPUT.close()
    FILE_OUTPUT.close()


if __name__ == "__main__":
    main()
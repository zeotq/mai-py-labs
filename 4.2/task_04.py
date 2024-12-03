def month(num: int, lg: str = "ru") -> str:
    month_name_from_num = {
        1: {"en": "January", "ru": "Январь"},
        2: {"en": "February", "ru": "Февраль"},
        3: {"en": "March", "ru": "Март"},
        4: {"en": "April", "ru": "Апрель"},
        5: {"en": "May", "ru": "Май"},
        6: {"en": "June", "ru": "Июнь"},
        7: {"en": "July", "ru": "Июль"},
        8: {"en": "August", "ru": "Август"},
        9: {"en": "September", "ru": "Сентябрь"},
        10: {"en": "October", "ru": "Октябрь"},
        11: {"en": "November", "ru": "Ноябрь"},
        12: {"en": "December", "ru": "Декабрь"}
    }
    return month_name_from_num[num][lg]
 

def main():
    result = month(1, "en")
    print(result)
    result = month(7)
    print(result)


if __name__ == "__main__":
    main()
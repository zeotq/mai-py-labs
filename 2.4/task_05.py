def main():
    """Ищем количество местностей, в которых есть зайца.
    
       Описание местности кончается словом "всё".
    """

    n = int(input())
    rabbits = 0
    keys = True
    ends = 0
    while ends < n:
        word = input().lower()
        rabbits, keys = ((rabbits + 1, False) 
                         if (word == "зайка" and keys is True) 
                         else (rabbits, keys))
        ends, keys = ((ends + 1, True) 
                      if (word == "всё") 
                      else (ends, keys))
    print(rabbits)


if __name__ == "__main__":
    main()

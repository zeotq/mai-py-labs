def reversed_dict(sourse_dict: dict) -> dict:
    result = dict()
    for i in sourse_dict.keys():
        for j in sourse_dict[i]:
            if j in result:
                result[j].update({i})
            else:
                result[j] = {i}

    return result


def task19_parser(s: str) -> dict:
    s = s.replace(" ", "")
    key, values = s.split(":")
    values = set(values.split(","))

    return {key: values}


def main():
    person_to_toys = dict()
    array_of_oneperson_to_toys = [task19_parser(input()) for _ in range(int(input()))]

    for i in array_of_oneperson_to_toys:
        person_to_toys.update(i)

    toy_to_owners = reversed_dict(person_to_toys)
    one_owner_toys = list()
    
    for j in toy_to_owners:
        if len(toy_to_owners[j]) == 1:
            one_owner_toys.append(j)

    print(*sorted(one_owner_toys), sep="\n") 
    return 0


if __name__ == "__main__":
    main()
  
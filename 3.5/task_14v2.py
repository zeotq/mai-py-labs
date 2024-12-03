import json


def merge_user_data(users, updates):
    """
    Объединяет данные пользователей из двух списков.
    При совпадении имен пользователей выбирается лексикографически большее значение для каждого поля.
    """
    new_dict = {}
    name_key = "name"

    for data in users:
        name = data.pop(name_key)
        new_dict[name] = data

    for data in updates:
        name = data.pop(name_key)
        if name not in new_dict:
            new_dict[name] = {}
        for key, value in data.items():
            if new_dict[name].get(key, "") < value:
                new_dict[name][key] = value

    return new_dict


def main():
    users_file = input().strip()
    updates_file = input().strip()

    with open(users_file, "r", encoding="utf-8") as f:
        users = json.load(f)

    with open(updates_file, "r", encoding="utf-8") as f:
        updates = json.load(f)

    merged_data = merge_user_data(users, updates)

    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False, sort_keys=False)


if __name__ == "__main__":
    main()

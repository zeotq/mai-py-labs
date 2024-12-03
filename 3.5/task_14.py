import json


def user_parser(*args): 
    user_from_name = dict()
    for pars_block in args:
        for block in pars_block:
            if 'name' not in block:
                continue
            name = block.pop('name')
            if name not in user_from_name:
                user_from_name[name] = {}
                
            for key, value in block.items():
                if user_from_name[name].get(key, "") < value:
                    user_from_name[name][key] = value

    return user_from_name


def main():
    #users_filelink = input()
    #updates_filelink = input()
    users_filelink = "3.5/task_14_users.json"
    updates_filelink = "3.5/task_14_updates.json"

    with open(users_filelink, mode="r+", encoding="UTF-8") as USERS, \
         open(updates_filelink, mode="r", encoding="UTF-8") as UPDATES:
        users = json.load(USERS)
        updates = json.load(UPDATES)
        merged_users = user_parser(users, updates)

        USERS.seek(0)
        json.dump(merged_users, USERS, indent=4, ensure_ascii=False, sort_keys=False)
        USERS.truncate()


if __name__ == "__main__":
    main()

import json


def user_parser(users, updates): 
    user_from_name = dict()
    for block in users + updates:
        if 'name' not in block:
            continue

        name = block['name']
        address = block.get('address', '')
        phone = block.get('phone', '')

        if name in user_from_name:
            if address:
                user_from_name[name]['address'] = max(address, user_from_name[name].get('address', ''))
            if phone:
                user_from_name[name]['phone'] = max(phone, user_from_name[name].get('phone', ''))
        else:
            new_dict = {}
            if address:
                new_dict['address'] = address
            if phone:
                new_dict['phone'] = phone
            user_from_name[name] = new_dict

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


dict().get()
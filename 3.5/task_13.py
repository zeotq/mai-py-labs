import json
from sys import stdin


def main():
    # TARGET_FILE = open(input(), mode="r+", encoding="UTF-8")
    TARGET_FILE = open("3.5/task_13.json", mode="r+", encoding="UTF-8")
    updates = json.load(TARGET_FILE)
    TARGET_FILE.seek(0)

    print(updates)
    for line in stdin:
        key, value = [i.strip() for i in line.split("==")]
        updates.update({key: value})
    json.dump(updates, TARGET_FILE, indent=4, ensure_ascii=False)
    TARGET_FILE.truncate()
    TARGET_FILE.close()


if __name__ == "__main__":
    main()
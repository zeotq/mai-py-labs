import requests


def main():
    seen_responses = set()
    all_strings = set()

    while True:
        response = requests.get("http://127.0.0.1:5000/")
        if response.status_code != 200:
            break

        try:
            data = tuple(response.json())
        except Exception:
            continue

        if data in seen_responses:
            break

        seen_responses.add(data)
        all_strings.update(data)

    sorted_strings = sorted(all_strings, key=lambda x: x.lower())
    for s in sorted_strings:
        print(s)


if __name__ == "__main__":
    main()

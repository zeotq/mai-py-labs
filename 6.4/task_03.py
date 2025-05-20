import csv


def main():
    L = float(input())
    cities = []

    with open("6.4/city.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row["geo_lat"])
                capital = int(row["capital_marker"])
                city = row["city"].strip()
                population = int(row["population"])
                foundation_year = int(row["foundation_year"])

                if lat < L and capital in [2]:
                    cities.append((city, population, foundation_year))
            except (ValueError, KeyError):
                continue

    cities.sort(key=lambda x: x[0])

    for city in cities:
        print(f"{city[0]} {city[1]} {city[2]}")


if __name__ == "__main__":
    main()  
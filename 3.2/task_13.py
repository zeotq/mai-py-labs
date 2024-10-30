def inputDishes(count: int = 0) -> set:
    dishes = set()
    for _ in range(count):
        dishes.add(input())
    return dishes


def main():
    menu = inputDishes(int(input()))
    dishes_cooked_on_week = set()
    for _ in range(int(input())):
        dishes_cooked_on_week.update(inputDishes(int(input())))

    result = list(sorted(menu.difference(dishes_cooked_on_week)))

    if result:
        print(*result, sep='\n')
    else:
        print("Готовить нечего")
        

if __name__ == "__main__":
    main()

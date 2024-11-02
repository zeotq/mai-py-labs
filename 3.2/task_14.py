def inputDishes(count: int = 0) -> set:
    dishes = set()
    for _ in range(count):
        dishes.add(input())
    return dishes


def main():
    products_in_stock = inputDishes(int(input()))
    dishes = []
    for _ in range(int(input())):
        dish = input()
        if all([input() in products_in_stock for i in range(int(input()))]):
            dishes.append(dish)
    if dishes:
        print(*sorted(dishes), sep='\n')
    else:
        print('Готовить нечего')

        
if __name__ == "__main__":
    main()

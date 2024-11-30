class Coffee(object):
    global in_stock

    def __init__(self, coffee = 0, milk = 0, cream = 0):
        self.coffee = coffee
        self.milk = milk
        self.cream = cream

    def can_be_cooked(self) -> bool:
        if self.coffee <= in_stock["coffee"] and self.milk <= in_stock["milk"] and self.cream <= in_stock["cream"]:
            return True
        return False

    def remove_from_stock(self):
        in_stock['coffee'] -= self.coffee
        in_stock['milk'] -= self.milk
        in_stock['cream'] -= self.cream


craft_from_coffe = {
    "Эспрессо": Coffee(coffee=1),
    "Капучино": Coffee(coffee=1, milk=3),
    "Макиато": Coffee(coffee=2, milk=1),
    "Кофе по-венски": Coffee(coffee=1, cream=2),
    "Латте Макиато": Coffee(coffee=1, milk=2, cream=1),
    "Кон Панна": Coffee(coffee=1, cream=1)
}


def order(*args):
    for name in args:
        if craft_from_coffe[name].can_be_cooked():
            craft_from_coffe[name].remove_from_stock()
            return name
    else:
        return "К сожалению, не можем предложить Вам напиток"


def main():
    global in_stock
    in_stock = {"coffee": 1, "milk": 2, "cream": 3}
    print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
    print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
    print("\n\n\n")
    in_stock = {"coffee": 4, "milk": 4, "cream": 0}
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))


if __name__ == "__main__":
    main()
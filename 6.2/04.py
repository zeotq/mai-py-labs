import pandas as pd


def cheque(price_list, **kwargs):
    def gen(): 
        for product, count in sorted(kwargs.items(), key=lambda a: a[0]):
            price = price_list[product]
            yield product, price, count, price * count

    return pd.DataFrame(gen(), columns=["product", "price", "number", "cost"])


def discount(cheque_frame: pd.DataFrame):
    discounted_frame = cheque_frame.copy()
    discounted_frame.loc[discounted_frame['number'] > 2, 'cost'] *= 0.5
    return discounted_frame


def test_1():
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    with_discount = discount(result)
    print(result)
    print(with_discount)


if __name__ == "__main__":
    test_1()

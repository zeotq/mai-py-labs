import pandas as pd


def cheque(price_list, **kwargs):
    def gen(): 
        for product, count in sorted(kwargs.items(), key=lambda a: a[0]):
            price = price_list[product]
            yield product, price, count, price * count

    return pd.DataFrame(gen(), columns=["product", "price", "number", "cost"])


def test_1():
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    print(result)


if __name__ == "__main__":
    test_1()

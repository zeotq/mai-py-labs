import matplotlib.pyplot as plt


def statistics(title, color, data):
    items = list(data.keys())
    counts = list(data.values())
    plt.bar(items, counts, color=color)
    plt.title(title)
    plt.savefig('result.png')
    plt.close()


def test_1():
    data = {'картина': 17, 'корзина': 9, 'картонка': 13}
    statistics('Багаж', 'limegreen', data)


def main():
    test_1()


if __name__ == "__main__":
    main()
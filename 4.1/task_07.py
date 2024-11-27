def can_eat(murder_pos: tuple[int], slave_pos: tuple[int]) -> bool:
    murder_pos_x, murder_pos_y = murder_pos
    slave_pos_x, slave_pos_y = slave_pos
    if abs(slave_pos_x - murder_pos_x) == 2 and abs(slave_pos_y - murder_pos_y) == 1:
        return True
    if abs(slave_pos_y - murder_pos_y) == 2 and abs(slave_pos_x - murder_pos_x) == 1:
        return True
    return False


def main():
    is_can_eat = can_eat((2, 1), (4, 2))
    print(is_can_eat)
    is_can_eat = can_eat((5, 5), (6, 6))
    print(is_can_eat)


if __name__ == "__main__":
    main()
result = set()


def bunny(start: int,
          finish: int,
          target_jump_count: int,
          actual_jump_count: int = 0,
          trace: list[int] = None,
          jump_variants: list[int] = [-3, -1, 1, 3]):
    if trace is None:
        trace = [start]

    if actual_jump_count == target_jump_count and start == finish:
        result.add(tuple(trace))
        return
    
    elif actual_jump_count > target_jump_count or start == finish:
        return
    
    for i in jump_variants:
        bunny(start - i, finish, target_jump_count, actual_jump_count + 1, trace + [start - i])

    return list(map(list, result))


def main():
    result = bunny(7, 10, 3)
    print(*result, sep="\n")

if __name__ == "__main__":
    main()
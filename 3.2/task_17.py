def bonds2dict(bonds: list) -> dict:
    result = {}
    for line in bonds:
        for index, name in enumerate(line):
            temp_line = list(line)
            temp_line.pop(index)
            if name in result:
                for i in temp_line:
                    result[name].add(i)
            else:
                result[name] = set(temp_line)

    return result


def handshake_pits(base_handshakes: dict, lvl: int = 2) -> dict:
    handshakes = dict()
    already_shaked_and_self = dict()

    for name in base_handshakes.keys():

        handshakes[name] = dict()
        already_shaked_and_self[name] = {name}

        for iter in range(lvl):
            if iter == 0:
                iter_handshakes = set().union(base_handshakes[name])
            else:
                iter_handshakes = set()
                for new_name in handshakes[name][iter - 1]:
                    if new_name in base_handshakes:
                        iter_handshakes.update(base_handshakes[new_name])

            handshakes[name].update({iter: iter_handshakes.difference(already_shaked_and_self[name])})
            already_shaked_and_self[name].update(iter_handshakes)

    return handshakes


if __name__ == "__main__":
    hs = []
    while (z := input()) != '':
        hs.append(z.split())

    temp = bonds2dict(bonds=hs)
    res = handshake_pits(temp)

    for i in sorted(res.keys()):
        print(f'{i}: {", ".join(sorted(res[i].get(1)))}')
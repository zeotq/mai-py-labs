def dividers(n: int) -> set:
    result = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result.update({i, n // i})
    return result.union({n}) if result else {n}


def mutually_prime_numbers(nums: set):
    nums_to_dividers = dict()
    mp_nums = dict()

    for i in nums:
        nums_to_dividers[i] = dividers(i)

    for i in nums_to_dividers.keys():
        for j in nums_to_dividers.keys():
            optimization_conditions = (i != j) and (i not in nums_to_dividers[j])
            if optimization_conditions and nums_to_dividers[i].intersection(nums_to_dividers[j]) == set():
                if i in mp_nums:
                    mp_nums[i].update({j})
                else:
                    mp_nums[i] = {j}
                if j in mp_nums:
                    mp_nums[j].update({i})
                else:
                    mp_nums[j] = {i}
    
    return mp_nums


def main():
    nums = set(map(int, input().replace(" ", "").split(";")))
    nums_to_mpn = mutually_prime_numbers(nums)
    for i in sorted(nums_to_mpn.keys()):
        print(f'{i} - {", ".join(map(str, sorted(list(nums_to_mpn[i]))))}')


if __name__ == "__main__":
    main()
  
from sys import stdin
import json


def isPrime(n: int) -> bool:
    if n in [-1, 0, 1]:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    primes2mult = dict()
    nums = set()

    for line in stdin:
        num = int(line)
        nums.add(num)
    nums2 = list(sorted(nums))
    primes = [i for i in range(1, max(nums2) + 2) if isPrime(i)]

    for prime in primes:
        multiples = [num for num in nums2 if num % prime == 0]
        if multiples:
            primes2mult[prime] = multiples

    converted_data = {str(key): list(value) for key, value in primes2mult.items()}
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(converted_data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
from random import randint

def hashCheck4Legit(block: int, prev_block: int = 0) -> bool:
    """_summary_

    Args:
        info (int): usefull digit info from 0 to 255
        prev_block (int, optional): hash of previus block. Defaults to 0.

    Returns:
        bool: is block legit
    """

    # Bn = Hn + Rn * 256 + Mn * 256^2
    hashN = block % 256
    if hashN >= 100:
        return False
    return True



def main():
    n = int(input())
    hashes = [int(input()) for i in range(n)]
    last_block = 0
    flag_block = True

    for index, element in enumerate(hashes):
        if not hashCheck4Legit(element, last_block):
            print(index + 1)
            flag_block = False
            break
        last_block = element

    if flag_block:
        print(-1)
            

if __name__ == "__main__":
    main()

import math

def polar_to_decart(r: float, angle_radian: float) -> tuple:
    return (math.cos(angle_radian) * r, math.sin(angle_radian) * r)


def main():
    Decoy_coords = map(float, input().split())
    Poly_rvec, Poly_angle = map(float, input().split())
    Poly_coords = polar_to_decart(Poly_rvec, Poly_angle)
    print(math.dist(Decoy_coords, Poly_coords))


if __name__ == "__main__":
    main()
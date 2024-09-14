# mass_1 + mass_2 = mass
# price_1 * mass_1 + price_2 * mass_2 = mass * price

mass, price, price_1, price_2 = [int(input()) for i in range(4)]

# => price_1 * (mass - mass_2) + price_2 * mass_2 = mass * price
# => (price_2 - price_1) * mass_2 = mass * (price - price_1)

mass_2 = mass * (price - price_1) / (price_2 - price_1)
mass_1 = mass - mass_2
print(round(mass_1), round(mass_2))
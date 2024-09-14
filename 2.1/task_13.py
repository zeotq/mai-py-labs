children, lolly = [int(input()) for i in range(2)]
dose = lolly // children
keep = lolly - dose * children

print(dose, keep, sep='\n')
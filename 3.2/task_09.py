def main():
    types_of_entity = {}

    while (line := input()) != "": 
        for el in line.split():
            if el in types_of_entity:
                types_of_entity[el] += 1
            else:
                types_of_entity[el] = 1
    
    return types_of_entity
        

if __name__ == "__main__":
    final = main()
    for i in final:
        print(i, final[i])

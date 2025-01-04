from checkers_game import *


def main():
    field = Checkers_Field(8, 8)
    # field.fill_matrix(lines=3)
    checkers = Checkers_Game(field=field)
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("C7"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("E7"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("G7"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("C5"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("E5"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("G5"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("C3"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("E3"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("G3"), Checker("b"))
    checkers.field.fill_cell(checkers.coords_letter_to_tuple("H2"), Checker("w"))
    checkers.start()


if __name__ == "__main__":
    main()
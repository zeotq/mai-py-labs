class Checker():
    images = {
            "w": "⚪",
            "b": "⚫",
            "none": " ▫️"
        }

    def __init__(self, 
                 team: str = None, 
                 rang: str = "default", 
                 custom_images: dict = images):
        """
        Initializes a Checker object.

        Args:
            team (str, optional): The color of the team. Possible values are:
                "b": Black team
                "w": White team
                Defaults to None.

            rang (str, optional): The rank of the checker. Possible values are:
                "default": The initial rank of the checker.
                "queen": A checker that has reached the end of the board.
                Defaults to "default".

            custom_images (dict, optional): images (emoji) for checkers 
                Defaults to Checker.images
        """

        self.team = team
        self.rang = rang
        self.images = custom_images

    def status(self):
        """Returns a status symbol for the checker.

        Returns:
            str: "B" for black, "W" for white, "X" for no team.
        """
        if self.team is not None:
            return self.team.upper()
        return "X"
    
    def image(self):
        """Returns a visual representation of the checker.

        Returns:
            str: image (emoji) for no currect Checker.
        """
        if self.team in self.images:
            return self.images[self.team]
        return self.images['none']

    def __str__(self):
        """String representation of the checker.

        Returns:
            str: Status symbol of the checker.
        """
        return self.status()


class Checkers_Field():
    def __init__(self, size_x: int = 8, size_y: int = 8):
        """Generates a game field for Checkers.

        Args:
            size_x (int, optional): Width of the field. Defaults to 8.
            size_y (int, optional): Height of the field. Defaults to 8.
        """
        self.size_x = size_x
        self.size_y = size_y
        self.matrix = [[None for _ in range(self.size_x)] for _ in range(self.size_y)]

    def get_cell_value(self, coords: tuple) -> Checker:
        """Gets the object at the specified coordinates.

        Args:
            coords (tuple): The (row, col) coordinates.

        Returns:
            Checker | None: The checker at the specified cell, or None if empty.
        """
        if not self.position_is_not_wrong(coords):
            raise ValueError
        cell = self.matrix[coords[0]][coords[1]]
        if isinstance(cell, Checker):
            return cell
        return None

    def get_matrix(self) -> list[list]:
        """Returns the entire field matrix.

        Returns:
            list[list]: The field matrix.
        """
        return self.matrix

    def fill_cell(self, coords: tuple, checker: Checker) -> None:
        """Fills a specific cell with a checker.

        Args:
            coords (tuple): The (row, col) coordinates.
            checker (Checker): The checker to place in the cell.
        """
        self.matrix[coords[0]][coords[1]] = checker

    def fill_matrix(self, lines: int = 3) -> None:
        """Fills the initial positions on the field with checkers.

        Args:
            lines (int, optional): Count of lines with checkers. Defaults to 3.
        """
        for i in range(0, lines):
            if (i % 2) == 1: 
                for j in range(0, self.size_x, 2):
                    self.matrix[i][j] = Checker("b")
                    self.matrix[self.size_y - i - 1][j + 1] = Checker("w")
            else:
                for j in range(1, self.size_x, 2):
                    self.matrix[i][j] = Checker("b")
                    self.matrix[self.size_y - i - 1][j - 1] = Checker("w")

    def clear_cell(self, coords: tuple):
        self.matrix[coords[0]][coords[1]] = None

    def position_is_not_wrong(self, coords: tuple) -> bool:
        if 0 <= coords[0] < self.size_x and 0 <= coords[1] < self.size_y:
            return True
        return False

    def __str__(self):
        """Draws the field in a visually appealing format.

        Returns:
            str: A string representation of the full field.
        """
        res = "   "
        for i in range(self.size_x):
            res += f" {chr(i + ord('A'))}"
        res += '\n'
        for i, el in enumerate(self.matrix):
            res += f"{self.size_y - i}  "
            for j in el:
                if isinstance(j, Checker):
                    res += j.image()
                else:
                    res += Checker().image()
            res += f"  {self.size_y - i}\n"
        res += "   "
        for i in range(self.size_x):
            res += f" {chr(i + ord('A'))}"
        return res
 

class Checkers_Game():
    def __init__(self, field: Checkers_Field = None):
        """Initializes a Checkers game.

        Args:
            field (Checkers_Field, optional): The game field. Defaults to a new Checkers_Field with default values.
        """
        if isinstance(field, Checkers_Field):
            self.field = field
        else:
            self.field = Checkers_Field()
            self.field.fill_matrix()
        self.state = "START"

    def start(self):
        self.state = "PLAYER_WHITE_MOVE"
        self.next_turn()

    def next_turn(self):
        """Proceeds to the next turn based on the current state."""
        if self.state == "PLAYER_WHITE_MOVE":
            print("\n\n\nWhite's turn!")
            while not self.turn("w"):
                continue
            self.state = "PLAYER_BLACK_MOVE"
            self.next_turn()

        elif self.state == "PLAYER_BLACK_MOVE":
            print("\n\n\nBlack's turn!")
            while not self.turn("b"):
                continue
            self.state = "PLAYER_WHITE_MOVE"
            self.next_turn()

    def player_choose_checker(self, team: str) -> tuple:
        """Give the player interface to choose a checker to move.

        Args:
            team (str): Player team.

        Returns:
            tuple: Coords (row, col).
        """
        while True:
            inp = input("Input cell to move from: ").upper()
            if len(inp) < 2 or not self.coords_letter_format_is_not_wrong(inp):
                print("Wrong format!")
                continue
            coords = self.coords_letter_to_tuple(inp)
            if not self.field.position_is_not_wrong(coords):  # Check coords
                print("Wrong position!")
                continue
            if self.get_cell(coords) is None:  # Check cell is not empty
                print("You choose empty cell, choose you checker!")
                continue
            if self.get_cell(coords).team != team:  # Check checker at cell team
                print("Choose you checker!", end=" ")
                continue
            if (self.get_moves(coords)) == []:  # Check moves variants is not empty
                print("This checker can't move! Choose another!", end=" ")
                continue
            break
        return coords

    def player_choose_move(self, moves: dict, double: bool = False) -> dict:
        """Give the player interface to choose move.

        Args:
            moves (dict): Move variants. 
            double_turn (bool, optional): After one turn player can eat other checker if he ate one. Defaults to False.

        Returns:
            dict: Selected move
        """
        print("Choose you move:")
        if double is False:
            for i, el in enumerate(moves):
                if "eat_at" in el.keys():
                    print(f"{i + 1}. To {self.coords_tuple_to_letter(el['res_pos'])}" + 
                    f" and eat enemy at {self.coords_tuple_to_letter(el['eat_at'])}")
                else:
                    print(f"{i + 1}. To {self.coords_tuple_to_letter(el['res_pos'])}")

            while not((move := input("Input move id: ")).isdigit() and (move := int(move)) > 0 and move <= len(moves)):
                print("Wrong move! Input move id!")

            return move - 1  # Return index

        else:
            custom_index = 0
            indexes = []
            for i, el in enumerate(moves):
                if "eat_at" in el.keys():
                    print(f"{custom_index + 1}. To {self.coords_tuple_to_letter(el['res_pos'])}" + 
                    f" and eat enemy at {self.coords_tuple_to_letter(el['eat_at'])}")
                    indexes.append(i)
                    custom_index += 1
            print(f"{custom_index + 1}. Pass")
            indexes.append(i + 1)
            
            while not((move := input("Input move id: ")).isdigit() and (move := int(move)) > 0 and move <= custom_index + 1):
                print("Wrong move! Input move id!")
            return indexes[move - 1]  # Returns cleared index

    def turn(self, team: str = "w", double: bool = False, start_pos: tuple = None) -> bool:
        self.draw()  # Draw game field in console

        if double is False and start_pos is None:
            checker = self.player_choose_checker(team)
        else:
            checker = start_pos
            if self.get_moves(checker, double) == []:
                return True

        if (moves := self.get_moves(checker, double)) is None:  # Check for currect return
            return False

        move = self.player_choose_move(moves, double)  # Give player choise for move

        if move == len(moves) and double is True:  # Player passed double turn
            return True
        
        if move == len(moves) and double is False:  # Player can't pass first turn move
            return False

        if (self.move(moves[move])) is False:
            return False
        
        self.turn(team=team, double=True, start_pos=moves[move]['res_pos'])  # Recursion call for double eats
        return True

    def move(self, move: dict) -> bool:
        if "res_pos" not in move.keys() or "from_pos" not in move.keys():
            return False
        if "eat_at" in move.keys():
            self.field.clear_cell(move['eat_at'])

        self.field.fill_cell(move['res_pos'], self.get_cell(move["from_pos"]))
        self.field.clear_cell(move['from_pos'])

        return True

    def get_moves(self, checker_pos: tuple | str = "A1", double: bool = False) -> list[dict]:

        if isinstance(checker_pos, str):
            checker_pos = self.coords_letter_to_tuple(checker_pos)

        if self.field.position_is_not_wrong(checker_pos):
            checker = self.get_cell(checker_pos)

            if checker is None:
                return None

            if checker.rang == "default" and double is False:
                return self.default_moves(checker_pos, checker.team)
            
            elif checker.rang == "default" and double is True:
                return self.double_moves(checker_pos, checker.team)
            
            elif checker.rang == "queen":
                return self.queen_moves(checker_pos, checker.team)
            
        return None

    def default_moves(self, coords: tuple = (0, 0), team: str = None) -> list[dict]:
        team_flag = 1 if team == 'b' else -1
        moves = [
            {   
                "from_pos": coords,
                "res_pos": (coords[0] + team_flag, coords[1] - 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] + team_flag, coords[1] + 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] + 2 * team_flag, coords[1] - 2),
                "eat_at": (coords[0] + team_flag, coords[1] - 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] + 2 * team_flag, coords[1] + 2),
                "eat_at": (coords[0] + team_flag, coords[1] + 1)
            }
        ]
        res = []
        for i in moves:
            if "eat_at" not in i.keys():
                if (self.field.position_is_not_wrong(i["res_pos"])
                    and self.get_cell(i["res_pos"]) is None):
                        res.append(i)
            else:
                if (self.field.position_is_not_wrong(i["eat_at"])
                    and self.field.position_is_not_wrong(i["res_pos"])
                    and self.get_cell(i["res_pos"]) is None
                    and self.get_cell(i["eat_at"]) is not None
                    and self.get_cell(i["eat_at"]).team != team):
                        res.append(i)

        return res

    def double_moves(self, coords: tuple = (0, 0), team: str = None) -> list[dict]:
        team_flag = 1 if team == 'b' else -1
        moves = [
            {
                "from_pos": coords,
                "res_pos": (coords[0] + 2 * team_flag, coords[1] - 2),
                "eat_at": (coords[0] + team_flag, coords[1] - 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] + 2 * team_flag, coords[1] + 2),
                "eat_at": (coords[0] + team_flag, coords[1] + 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] - 2 * team_flag, coords[1] - 2),
                "eat_at": (coords[0] - team_flag, coords[1] - 1)
            },
            {
                "from_pos": coords,
                "res_pos": (coords[0] - 2 * team_flag, coords[1] + 2),
                "eat_at": (coords[0] - team_flag, coords[1] + 1)
            }
        ]
        res = []
        for i in moves:
            if (self.field.position_is_not_wrong(i["eat_at"])
                and self.field.position_is_not_wrong(i["res_pos"])
                and self.get_cell(i["res_pos"]) is None
                and self.get_cell(i["eat_at"]) is not None
                and self.get_cell(i["eat_at"]).team != team):
                    res.append(i)

        return res

    def queen_moves(self, coords: tuple = (0, 0), team: str = None) -> list:  # to do
        return None
        team_flag = 1 if team == 'b' else -1
        moves = [
            (coords[0] + team_flag, coords[1] + 1),
            (coords[0] + team_flag, coords[1] - 1)
        ]
        for i in range(1, min(self.field.size_x, self.field.size_y)):
            moves.append((coords[0] - i, coords[1] - i))
            moves.append((coords[0] - i, coords[1] + i))
            moves.append((coords[0] + i, coords[1] - i))
            moves.append((coords[0] + i, coords[1] + i))
        return moves

    def force_move(self, from_pos: tuple | str = "A1", to_pos: tuple | str = "A1") -> bool:
        """Moves a checker from one position to another.

        Args:
            from_pos (tuple | str, optional): The starting position. Defaults to "A1".
            to_pos (tuple | str, optional): The target position. Defaults to "A1".

        Returns:
            bool: True if the move was successful.
        """
        if isinstance(from_pos, str):
            from_pos_coords = self.coords_letter_to_tuple(from_pos)
        if isinstance(to_pos, str):
            to_pos_coords = self.coords_letter_to_tuple(to_pos)
        self.field.fill_cell(to_pos_coords, self.get_cell(from_pos))
        self.field.clear_cell(from_pos_coords)

        return True
    
    def draw(self):
        print(self.field)

    def coords_letter_format_is_not_wrong(self, coords: str = "A1") -> bool:
        if not coords[0].isalpha():
            return False
        if not coords[1::].isdigit():
            return False
        return True

    def coords_letter_to_tuple(self, coords: str = "A1") -> tuple:
        """Converts named coordinates to matrix indices.

        Args:
            coords (str, optional): Named coordinates (e.g., "A1"). Defaults to "A1".

        Returns:
            tuple: (row, col) coordinates in matrix format.
        """
        if not self.coords_letter_format_is_not_wrong(coords):
            raise ValueError

        col = self.field.size_y - int(coords[1::])
        row = ord(coords[0]) - ord('A')

        return (col, row)
    
    def coords_tuple_to_letter(self, coords: tuple) -> str:
        """Converts matrix indices to named coordinates.

        Args:
            tuple: (row, col) coordinates in matrix format.

        Returns:
            coords (str, optional): Named coordinates (e.g., "A1"). Defaults to "A1".
        """
        return chr(coords[1] + ord('A')) + str(self.field.size_y - coords[0])

    def get_cell(self, coords: tuple | str = "A1") -> Checker | None:
        """Gets the checker at the specified coordinates.

        Args:
            coords (tuple | str, optional): Either matrix indices (row, col) or named coordinates (e.g., "A1"). Defaults to "A1".

        Returns:
            Checker | None: The checker at the cell, or None if empty.
        """
        if isinstance(coords, str):
            coords = self.coords_letter_to_tuple(coords)
        return self.field.get_cell_value(coords)

    def __str__(self) -> str:
        return str(self.field)
    

def main():
    pass


if __name__ == "__main__":
    main()

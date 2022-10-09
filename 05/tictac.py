"""
Module for class TicTacGame
"""


class TicTacGame:
    """
    This class creates the tic tac game and allows
    two players play consequently until one of them win or it will be a draw
    """

    def __init__(self):
        self.is_first_player = True
        self.is_second_player = False
        self.board = [str(i) for i in range(1, 10)]

    def show_board(self) -> None:
        """
        This method prints the tic tac game board
        """
        for i in range(3):
            print(" | ".join(pos for pos in self.board[3 * i: 3 * (i + 1)]))

    def validate_input(self, player_input: str) -> bool:
        """
        This method checks the input move of the player
        :param player_input: input move of the player
        :return: correct or incorrect input
        """
        if not player_input.strip().lstrip("-").isdigit():
            print("Incorrect input! Please input digit")
            return False
        player_input = int(player_input)
        if player_input < 1 or player_input > 9:
            print("Incorrect input! Number of cell must be between 1 and 9")
            return False
        if self.board[player_input - 1] in {"X", "O"}:
            print("Incorrect input! This cell is already occupied!")
            return False
        return True

    def make_move(self, player_symbol: str) -> None:
        """
        This method validates input until it is correct
        and change the board state
        :param player_symbol: "X" or "O" symbol of current player
        """
        print(f"Print the number where you want to put {player_symbol}")
        pos = input()
        while not self.validate_input(pos):
            pos = input()
        pos = int(pos)
        self.board[pos - 1] = player_symbol

    def start_game(self) -> None:
        """
        This method starts the game and perform moves of the players
        """
        print("Welcome to TicTac game!")
        self.show_board()
        while not self.check_winner():
            if self.is_first_player:
                self.make_move("X")
                self.is_second_player = True
                self.is_first_player = False
            elif self.is_second_player:
                self.make_move("O")
                self.is_first_player = True
                self.is_second_player = False
            self.show_board()

    def check_winner(self) -> bool:
        """
        This method checks if there is a winning combination on the board
        :return: does board have a winning combination in it
        """
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        for cmb in win_combinations:
            if self.board[cmb[0]] == self.board[cmb[1]] == self.board[cmb[2]]:
                if self.board[cmb[0]] == "X":
                    print("First player is a winner!")
                else:
                    print("Second player is a winner!")
                return True
        if self.board.count("X") + self.board.count("O") == len(self.board):
            print("Draw! There is no space left to place the symbol")
            return True
        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()

import unittest
from unittest import mock
from parameterized import parameterized

from tictac import TicTacGame
from utils_for_test import generate_tests_input, combine_strategies


class TestTicTac(unittest.TestCase):
    @parameterized.expand([
        [
            "str",
            "abcde",
            "Incorrect input! Please input digit"],
        [
            "less_than_one",
            "-1",
            "Incorrect input! Number of cell must be between 1 and 9"],
        [
            "more_than_nine",
            "100",
            "Incorrect input! Number of cell must be between 1 and 9"],
    ])
    def test_incorrect_input(self, name, val, str_error):
        game = TicTacGame()
        with mock.patch("builtins.print") as mock_print:
            self.assertFalse(game.validate_input(val))
            mock_print.assert_called_with(str_error)

    def test_occupied_cell(self):
        game = TicTacGame()
        game.board[0] = "X"
        val = "1"
        str_error = "Incorrect input! This cell is already occupied!"
        with mock.patch("builtins.print") as mock_print:
            self.assertFalse(game.validate_input(val))
            mock_print.assert_called_with(str_error)

    def test_correct_input(self):
        game = TicTacGame()
        game.board[0] = "X"
        val = "2"
        self.assertTrue(game.validate_input(val))

    @parameterized.expand(
        generate_tests_input()
    )
    def test_game_result_first_player(self, name, first_player_strategy, second_player_strategy):
        game = TicTacGame()
        with mock.patch("builtins.input") as mock_input, mock.patch("builtins.print") as mock_print:
            mock_input.side_effect = combine_strategies(
                first_player_strategy=first_player_strategy,
                second_player_strategy=second_player_strategy,
                input_steps=[]
            )
            game.start_game()
            mock_print.assert_called_with("First player is a winner!")

    @parameterized.expand(
        generate_tests_input()
    )
    def test_game_result_second_player(self, name, second_player_strategy, first_player_strategy):
        game = TicTacGame()
        with mock.patch("builtins.input") as mock_input, mock.patch("builtins.print") as mock_print:
            mock_input.side_effect = combine_strategies(
                first_player_strategy=first_player_strategy,
                second_player_strategy=second_player_strategy,
                input_steps=[]
            )
            game.start_game()
            mock_print.assert_called_with("Second player is a winner!")

    def test_game_with_incorrect_input(self):
        game = TicTacGame()
        with mock.patch("builtins.input") as mock_input, mock.patch("builtins.print") as mock_print:
            mock_input.side_effect = combine_strategies(
                first_player_strategy=[1, 3, 5, 7],
                second_player_strategy=[2, 4, 6, 8],
                input_steps=["1"]
            )
            game.start_game()
            mock_print.assert_called_with("First player is a winner!")

    def test_draw(self):
        game = TicTacGame()
        with mock.patch("builtins.input") as mock_input, mock.patch("builtins.print") as mock_print:
            mock_input.side_effect = combine_strategies(
                first_player_strategy=[1, 3, 8, 6, 7],
                second_player_strategy=[2, 5, 4, 9],
                input_steps=[]
            )
            game.start_game()
            mock_print.assert_called_with("Draw! There is no space left to place the symbol")

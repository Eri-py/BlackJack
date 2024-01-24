from blackjack_helper import *
from test_helper import *
import unittest


class TestBlackjackHelper(unittest.TestCase):
    # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
    # WRITE YOUR TESTS BELOW.
    def test_print_card_name(self):
        self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
        self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
        self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
        self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
        self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
        self.assertEqual(get_print(print_card_name, -1), "BAD CARD\n")
        self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
        self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
        self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

    def test_draw_card(self):
        self.assertEqual(mock_random([1], draw_card), 11)
        self.assertEqual(mock_random([11], draw_card), 10)
        self.assertEqual(mock_random([12], draw_card), 10)
        self.assertEqual(mock_random([13], draw_card), 10)
        self.assertEqual(mock_random([8], draw_card), 8)

    def test_print_header(self):
        self.assertEqual(
            get_print(print_header, "DEALER TURN"),
            "-----------\nDEALER TURN\n-----------\n",
        )
        self.assertEqual(
            get_print(print_header, "eRi tuRN1"),
            "-----------\neRi tuRN1\n-----------\n",
        )

    def test_draw_starting_hand(self):
        self.assertEqual(mock_random([1, 2], draw_starting_hand, "Jojo"), 13)
        self.assertEqual(mock_random([12, 13], draw_starting_hand, "1111"), 20)
        self.assertEqual(mock_random([1, 11], draw_starting_hand, "HEHEH"), 21)
        self.assertEqual(mock_random([2, 5], draw_starting_hand, "HeHe"), 7)

    def test_print_end_turn_status(self):
        self.assertEqual(get_print(print_end_turn_status, 17), "Final hand: 17.\n")
        self.assertEqual(
            get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n"
        )
        self.assertEqual(
            get_print(print_end_turn_status, 22), "Final hand: 22.\nBUST.\n"
        )

    def test_print_end_game_status(self):
        self.assertEqual(
            get_print(print_end_game_status, 21, 21),
            "-----------\nGAME RESULT\n-----------\nPush.\n",
        )
        self.assertEqual(
            get_print(print_end_game_status, 19, 19),
            "-----------\nGAME RESULT\n-----------\nPush.\n",
        )
        expected_output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
        self.assertEqual(get_print(print_end_game_status, 21, 19), expected_output)
        self.assertEqual(get_print(print_end_game_status, 17, 22), expected_output)
        self.assertEqual(get_print(print_end_game_status, 18, 17), expected_output)
        expected_output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
        self.assertEqual(get_print(print_end_game_status, 19, 21), expected_output)
        self.assertEqual(get_print(print_end_game_status, 22, 17), expected_output)
        self.assertEqual(get_print(print_end_game_status, 22, 22), expected_output)
        self.assertEqual(get_print(print_end_game_status, 22, 30), expected_output)


if __name__ == "__main__":
    unittest.main()

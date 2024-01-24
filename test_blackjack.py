from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):
    '''
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):

        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.

        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    '''
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    # Write all your tests above this. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_1(self, input_mock, randint_mock):
        #When both dealer and user get blackjack
        output = run_test([10,1], [], [5, 5, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_2(self, input_mock, randint_mock):
        #When user gets blackjack and the dealer gets less than 21
        output = run_test([5,5,1], ['x','y'], [5, 5, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n"\
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_3(self, input_mock, randint_mock):
        #When user gets blackjack and the dealer gets greater than 21(Bust)
        output = run_test([5,5,1], ['x','y'], [5, 8, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n"\
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_4(self, input_mock, randint_mock):
        #When the user is below 21 and the dealer is above 21.
        output = run_test([5,5,7], ['x','y','n'], [5, 8, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n"\
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_5(self, input_mock, randint_mock):
        #When the user is below 21 and the dealer is also below 21 but the user wins.
        output = run_test([5,5,8], ['x','y','n'], [5, 8, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n"\
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew a 4\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_6(self, input_mock, randint_mock):
        #When the dealer get's 21 and the user is below 21.
        output = run_test([5,5,7], ['x','y','n'], [5, 5, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n"\
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_7(self, input_mock, randint_mock):
        #When the dealer get's 21 and the user is above 21.
        output = run_test([7,8,7], ['y'], [5, 5, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew an 8\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_8(self, input_mock, randint_mock):
        #When the dealer is below 21 and the user is also below 21 but the dealer wins
        output = run_test([7,8,3], ['y','n'], [5, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew an 8\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_9(self, input_mock, randint_mock):
        #When both the user and dealer are above 21
        output = run_test([7,8,8], ['y'], [7, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew an 8\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 6\n" \
                   "Dealer has 13.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_10(self, input_mock, randint_mock):
        #When both the user and dealer are above 21 but it's the same number
        output = run_test([7,8,8], ['y'], [7, 5, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew an 8\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "Dealer has 12.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_scenerio_11(self, input_mock, randint_mock):
        #When both the user and dealer are below 21 but it's the same number
        output = run_test([4,3,12], ['y','n'], [4, 3, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 3\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a Queen\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 3\n" \
                   "Dealer has 7.\n" \
                   "Drew a King\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

if __name__ == '__main__':
    main()

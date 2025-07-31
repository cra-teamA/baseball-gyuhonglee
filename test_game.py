import pytest
from game import Game
from game_result import GameResult


@pytest.fixture
def game():
    return Game()

def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, invalid_input):
    assert_illegal_argument(game, invalid_input)

def test_return_solved_result_if_matched_number(game):
    game.question= "123"
    result:GameResult = game.guess("123")

    assert result is not None
    assert result._solved == True
    assert result._strikes == 3
    assert result._balls == 0

def test_return_solved_result_if_unmatched_number(game):
    game.question= "123"
    result:GameResult = game.guess("456")

    solved = False
    strikes = 0
    balls = 0

    assert_matched_number(balls, result, solved, strikes)


def assert_matched_number(balls, result, solved, strikes):
    assert result is not None
    assert result._solved == solved
    assert result._strikes == strikes
    assert result._balls == balls


from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number) -> GameResult:
        self._assert_illegal_value(guess_number)
        return GameResult(True, 3, 0)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError()

        if len(guess_number) != 3:
            raise TypeError()

        if not guess_number.isdigit():
            raise TypeError()

        if self._is_duplicate_number(guess_number):
            raise TypeError()

    def _is_duplicate_number(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]
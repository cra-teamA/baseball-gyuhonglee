from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)

        balls, strikes = self.calc_baseball(guess_number)

        return GameResult(False, strikes, balls)

    def calc_baseball(self, guess_number):
        balls = 0
        strikes = 0
        for idx in range(len(guess_number)):
            if guess_number[idx] == self._question[idx]:
                strikes += 1
            elif guess_number[idx] in self._question:
                balls += 1
        return balls, strikes

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
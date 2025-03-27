import enum

class CardSuit(enum.Enum):

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other):
        if isinstance(other, CardSuit):
            return self.value == other.value

    def __lt__(self, other):
        if isinstance(other,CardSuit):
            return self.value < other.value

    def __gt__(self, other):
        if isinstance(other,CardSuit):
            return self.value > other.value

    def __hash__(self):
        return hash(self.value)

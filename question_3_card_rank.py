import enum

class CardRank(enum.Enum):

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __eq__(self, other):
        if isinstance(other,CardRank):
            return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        if isinstance(other,CardRank):
            return self.value < other.value

    def __gt__(self, other):
        if isinstance(other,CardRank):
            return self.value > other.value
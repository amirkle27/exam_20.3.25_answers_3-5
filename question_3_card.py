from question_3_card_rank import CardRank
from question_3_card_suit import CardSuit

class Card:
    def __init__(self, suit:CardSuit, rank:CardRank, face_up:bool = True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        else:
            return self._rank == other._rank and self._suit == other._suit

    def __lt__(self, other):
        if isinstance(other, Card):
            if self._rank == other._rank:
                return self._suit < other._suit
            return self._rank < other._rank

    def __gt__(self, other):
        if isinstance(other,Card):
            if self._rank == other._rank:
                return self._suit > other._suit
            return self._rank > other._rank

    def __hash__(self):
        return hash((self._suit, self._rank))

    def __str__(self):
        if self._face_up:
            return self.get_display_name()
        return "?"

    def __repr__(self):
        return f"Card(suit = {self._suit}, rank = {self._rank}, face_up = {self._face_up})"

    @property
    def suit(self):
        return self._suit.name

    @property
    def rank(self):
        return self._rank.name

    @property
    def face_up(self):
        return self._face_up

    def flip(self):
        if self._face_up:
            self._face_up = False
        else:
            self._face_up = True

    def get_display_name(self):
        return f"{self._rank.name} of {self._suit.name} "

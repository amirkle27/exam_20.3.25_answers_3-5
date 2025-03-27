from deck_cheating_error import DeckCheatingError
import enum
from random import shuffle
from copy import deepcopy

def fair_deck(func):
    def wrapper(self):
        print(f"\nInitial Deck:\n  {self._cards}")
        print("Shuffling once:")

        first_shuffle = deepcopy(func(self))
        print(" ", first_shuffle)

        print("Shuffling again:")
        second_shuffle = deepcopy(func(self))

        print(" ", second_shuffle)
        if first_shuffle == second_shuffle:
            raise DeckCheatingError
        else:
            print(f"\nSecond shuffle didn't produced same result as First shuffle. Hence, Deck is fair.\n\nDeck after First shuffle: {first_shuffle}\nDeck after Second shuffle: {second_shuffle}")
            return first_shuffle
    return wrapper

class CardSuit(enum.Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other):
        if not isinstance(other, CardSuit):
             return NotImplemented
        else:
            return self.value == other.value

    def __lt__(self, other):
        if isinstance(other,CardSuit):
            return self.value < other.value

    def __gt__(self, other):
        if isinstance(other,CardSuit):
            return self.value > other.value

    def __hash__(self):
        return hash(self.value)

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

class Card:
    def __init__(self, suit:CardSuit, rank:CardRank, face_up:bool = True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    def __eq__(self, other):
        if isinstance(other, Card):
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
        return (f"Card(suit = {self._suit}, rank = {self._rank}, face_up = {self._face_up})")

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

class Deck(DeckCheatingError):
    def __init__(self):
        self._cards = [(rank.name,suit.name) for rank in CardRank for suit in CardSuit]
        self._index = 0
        self.suit = CardSuit
        self.rank = CardRank

    def __len__(self):
        return  len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._cards):
            card = self._cards[self._index]
            self._index +=1
            return card
        else:
            raise StopIteration

    @property
    def cards(self):
        return self._cards

    @fair_deck
    def shuffle(self):
        shuffle(self._cards)
        return self._cards

    def draw(self):
            if len(self._cards) > 0:
                return self._cards.pop(0)
            else:
                return "Empty Deck"

    def add_card(self,card):
        self._cards.append(card)

ace_of_spades = Card(CardSuit.SPADES, CardRank.ACE)
king_of_hearts = Card(CardSuit.HEARTS, CardRank.KING)
print(f"First card: {ace_of_spades}")
print(f"Second card: {king_of_hearts}")
if ace_of_spades > king_of_hearts:
    print(f"{ace_of_spades} is higher than {king_of_hearts}")
ace_of_spades.flip()
print(f"After flipping: {ace_of_spades}")
deck = Deck()
print(f"Deck size: {len(deck)}")
try:
    new_deck = deck.shuffle()
    print("Deck shuffled successfully")
except DeckCheatingError:
    print("Cheating detected! Deck not shuffled properly!")
card1 = deck.draw()
card2 = deck.draw()
print(f"Drawn cards: {card1}, {card2}")
print(f"Deck size after drawing: {len(deck)}")
print("\nAccessing cards directly by index:")
for i in range(5):
    print(f"Card at index {i}: {deck[i]}")
    print("\nIterating through all cards in the deck:")
for card in deck:
    print(card)

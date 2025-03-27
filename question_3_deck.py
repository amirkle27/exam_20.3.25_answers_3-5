from question_3_card_suit import CardSuit
from question_3_card_rank import CardRank
from question_3_card import Card
from random import shuffle
from copy import deepcopy
from deck_cheating_error import DeckCheatingError

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

class Deck:
    def __init__(self):
        self._cards = [Card(suit,rank) for rank in CardRank for suit in CardSuit]
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
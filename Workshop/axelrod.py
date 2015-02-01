"""
Recreate Axelrod's tournament


"""
import itertools
import random

class Axelrod:
    """
    A class for an iterated prisoner's dilemma.

    Take a list of players (see the Player class):

        >>> P1 = Defector()
        >>> P2 = Cooperator()
        >>> axelrod = Axelrod(P1, P2)
        >>> axelrod.round_robin(turns=10)
        >>> for player in sorted(axelrod.players, key=lambda x: x.score):
        ...     print player, player.score
        Defector 0
        Cooperator 50
    """
    def __init__(self, *args):
        """
        Initiate a tournament of players:

            >>> P1 = Defector()
            >>> P2 = Defector()
            >>> P3 = Defector()
            >>> axelrod = Axelrod(P1, P2, P3)
            >>> axelrod.players
            [Defector, Defector, Defector]
        """
        self.players = list(args)

    def round_robin(self, turns=200):
        """
        Plays a round robin where each match lasts turns.

        Defector viciously punishes Cooperator:

            >>> P1 = Defector()
            >>> P2 = Cooperator()
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.round_robin(turns=10)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Defector 0
            Cooperator 50

        Defector does very well against Tit for Tat:

            >>> P1 = Defector()
            >>> P2 = TitForTat()
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.round_robin(turns=10)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Defector 36
            Tit For Tat 41

        Cooperator does very well WITH Tit for Tat:

            >>> P1 = Cooperator()
            >>> P2 = TitForTat()
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.round_robin(turns=10)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Cooperator 20
            Tit For Tat 20

        Automatically runs all results as required for games with more players, taking
        the random player out:

            >>> P1 = Defector()
            >>> P2 = Cooperator()
            >>> P3 = TitForTat()
            >>> axelrod = Axelrod(P1, P2, P3)
            >>> axelrod.round_robin(turns=200)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Defector 796
            Tit For Tat 1201
            Cooperator 1400

        We see here that Tit for Tat does very poorly (compared to the Defector)
        despite the well known results. Why is this? Let us introduce another
        'aggressive' strategy

            >>> P1 = Defector()
            >>> P2 = Cooperator()
            >>> P3 = TitForTat()
            >>> P4 = Grudger()
            >>> axelrod = Axelrod(P1, P2, P3, P4)
            >>> axelrod.round_robin(turns=200)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Defector 1592
            Tit For Tat 1601
            Grudger 1601
            Cooperator 1800

        We see that Tit for Tat is much closer. Let us add in another strategy.

            >>> P1 = Defector()
            >>> P2 = Cooperator()
            >>> P3 = TitForTat()
            >>> P4 = Grudger()
            >>> P5 = GoByMajority()
            >>> axelrod = Axelrod(P1, P2, P3, P4, P5)
            >>> axelrod.round_robin(turns=200)
            >>> for player in sorted(axelrod.players, key=lambda x: x.score):
            ...     print player, player.score
            Tit For Tat 2001
            Grudger 2001
            Go By Majority 2001
            Cooperator 2200
            Defector 2388

        Now Tit for Tat is top of the pile and in fact the defector is at the bottom.
        Take a look at the various strategies.
        """
        for p1, p2 in itertools.combinations(self.players, 2):
            turn = 0
            p1.history = []
            p2.history = []
            while turn < turns:
                turn += 1
                p1.play(p2)
            scores = self.calculate_scores(p1, p2)
            p1.score += scores[0]
            p2.score += scores[1]

    def calculate_scores(self, p1, p2):
        """
        Calculates the score for two players based their history and on following:

        - C vs C both get 2
        - D vs D both get 4
        - C vs D => C gets 5 and D gets 0

            >>> P1 = Player()
            >>> P1.history = ['C', 'C', 'D']
            >>> P2 = Player()
            >>> P2.history = ['C', 'D', 'D']
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.calculate_scores(P1, P2)
            (11, 6)

            >>> P1 = Player()
            >>> P1.history = ['C', 'C', 'C']
            >>> P2 = Player()
            >>> P2.history = ['C', 'C', 'C']
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.calculate_scores(P1, P2)
            (6, 6)

            >>> P1 = Player()
            >>> P1.history = ['D', 'D', 'D']
            >>> P2 = Player()
            >>> P2.history = ['D', 'D', 'D']
            >>> axelrod = Axelrod(P1, P2)
            >>> axelrod.calculate_scores(P1, P2)
            (12, 12)
        """
        s1, s2 = 0, 0
        for pair in zip(p1.history, p2.history):
            if pair[0] == pair[1] == 'C':
                s1 += 2
                s2 += 2
            if pair[0] == pair[1] == 'D':
                s1 += 4
                s2 += 4
            if pair[0] == 'C' and pair[1] == 'D':
                s1 += 5
                s2 += 0
            if pair[0] == 'D' and pair[1] == 'C':
                s1 += 0
                s2 += 5
        return s1, s2


class Player:
    """
    A class for a player
    """
    def __init__(self):
        """
        Initiates an empty history and 0 score for every player

            >>> P1 = Player()
            >>> P1.history
            []
            >>> P1.score
            0
        """
        self.history = []
        self.score = 0

    def play(self, opponent):
        """
        This pits two players against each other: note that this will raise
        an error if no strategy method is defined (which are defined through
        class inheritance).

            >>> P1, P2 = Player(), Player()
            >>> P1.play(P2)
            Traceback (most recent call last):
            ...
            AttributeError: Player instance has no attribute 'strategy'

        Also note that it does not matter which player plays the other:

            >>> P2.play(P1)
            Traceback (most recent call last):
            ...
            AttributeError: Player instance has no attribute 'strategy'
        """
        s1, s2 = self.strategy(opponent), opponent.strategy(self)
        self.history.append(s1)
        opponent.history.append(s2)


class Defector(Player):
    """
    A player who only ever defects
    """
    def strategy(self, opponent):
        """
        Always returns 'D'

            >>> P1 = Defector()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'D'

        This is not affect by the history of either player:

            >>> P1.history = ['C', 'D', 'C']
            >>> P2  = ['C', 'C', 'D']
            >>> P1.strategy(P2)
            'D'
        >>>
        """
        return 'D'

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = Defector()
            >>> print P1
            Defector
        """
        return 'Defector'

class Cooperator(Player):
    """
    A player who only ever cooperates
    """
    def strategy(self, opponent):
        """
        Always returns 'C'

            >>> P1 = Cooperator()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'C'

        This is not affect by the history of either player:

            >>> P1.history = ['C', 'D', 'C']
            >>> P2.history  = ['C', 'C', 'D']
            >>> P1.strategy(P2)
            'C'
        >>>
        """
        return 'C'

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = Cooperator()
            >>> print P1
            Cooperator
        """
        return 'Cooperator'

class Random(Player):
    """
    A player who randomly chooses between cooperating and defecting
    """
    def strategy(self, opponent):
        """
        Always returns 'C'

            >>> random.seed(1)
            >>> P1 = Random()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'C'

        This is not affect by the history of either player:

            >>> random.seed(1)
            >>> P1.history = ['C', 'D', 'C']
            >>> P2.history = ['C', 'C', 'D']
            >>> P1.strategy(P2)
            'C'

        It is simply a random choice:

            >>> random.seed(2)
            >>> P1.strategy(P2)
            'D'
            >>> P1.strategy(P2)
            'D'
            >>> P1.strategy(P2)
            'C'
        >>>
        """
        return random.choice(['C','D'])

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = Cooperator()
            >>> print P1
            Cooperator
        """
        return 'Random'

class TitForTat(Player):
    """
    A player starts by cooperating and then mimics previous move by opponent.
    """
    def strategy(self, opponent):
        """
        Begins by playing 'C':

            >>> random.seed(1)
            >>> P1 = TitForTat()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'C'

        This is affected by the history of the opponent:

            >>> P1.history = ['C', 'D', 'C']
            >>> P2.history = ['C', 'C', 'D']
            >>> P1.strategy(P2)
            'D'

            >>> P1.history.append('D')
            >>> P2.history.append('C')
            >>> P1.strategy(P2)
            'C'
        >>>
        """
        try:
            return opponent.history[-1]
        except IndexError:
            return 'C'

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = Cooperator()
            >>> print P1
            Cooperator
        """
        return 'Tit For Tat'

class Grudger(Player):
    """
    A player starts by cooperating however will defect if at any point the opponent has defected
    """
    def strategy(self, opponent):
        """
        Begins by playing 'C':

            >>> P1 = Grudger()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'C'

        This is affected by the history of the opponent:

            >>> P1.history = ['C', 'C', 'C']
            >>> P2.history = ['C', 'C', 'C']
            >>> P1.strategy(P2)
            'C'

        If at any point the opponent defects then the player will forever defect:

            >>> P1.history = ['C', 'C', 'D', 'D', 'D']
            >>> P2.history = ['C', 'D', 'C', 'C', 'C']
            >>> P1.strategy(P2)
            'D'
        >>>
        """
        if 'D' in opponent.history:
            return 'D'
        return 'C'

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = Grudger()
            >>> print P1
            Grudger
        """
        return 'Grudger'

class GoByMajority(Player):
    """
    A player examines the history of the opponent: if the opponent has more defections than cooperations then the player defects
    """
    def strategy(self, opponent):
        """
        Begins by playing 'C':

            >>> P1 = GoByMajority()
            >>> P2 = Player()
            >>> P1.strategy(P2)
            'C'

        This is affected by the history of the opponent:

            >>> P1.history = ['C', 'C', 'C']
            >>> P2.history = ['C', 'C', 'C']
            >>> P1.strategy(P2)
            'C'

        As long as the opponent cooperates at least as often as they defect then the player will defect.

            >>> P1.history = ['C', 'D', 'D', 'D']
            >>> P2.history = ['D', 'D', 'C', 'C']
            >>> P1.strategy(P2)
            'C'

        If at any point the opponent has more defections than cooperations the player defects.

            >>> P1.history = ['C', 'C', 'D', 'D', 'D']
            >>> P2.history = ['C', 'D', 'D', 'D', 'C']
            >>> P1.strategy(P2)
            'D'
        >>>
        """
        if sum([s == 'D' for s in opponent.history]) > sum([s == 'C' for s in opponent.history]):
            return 'D'
        return 'C'

    def __repr__(self):
        """
i       The string method for the strategy:

            >>> P1 = GoByMajority()
            >>> print P1
            Go By Majority
        """
        return 'Go By Majority'

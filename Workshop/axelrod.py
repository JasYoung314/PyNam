"""
Recreate Axelrod's tournament


"""

class Axelrod:
    """
    A class for an iterated prisoner's dilemma.

    Take a list of players (see the Player class):

        >>> P1 = Defector()
        >>> P2 = Cooperator()
        >>> axelrod = Axelrod(P1, P2)
        >>> axelrod.round_robin(turns=10)
        >>> for player in sorted(axelrod.players, key=lambda x: x.score):
        ...     player.name, player.score
        P1, 0
        P2, 20
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

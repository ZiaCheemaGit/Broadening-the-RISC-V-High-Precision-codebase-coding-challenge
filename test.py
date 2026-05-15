import random
from hanoi import Hanoi


def test_number_of_moves():
    """
    Test if game is solved in perfect minimum number of moves
    with random inputs between 1 - 8
    """

    for _ in range(3):     
        n = random.randint(1, 8)
        game = Hanoi(n, False)
        game.solve()
        assert game.state.total_moves == 2**n - 1


def test_final_state():
    """
    Test if solution is correct 
    """
    
    for _ in range(3):  
        n = random.randint(1, 8)
        game = Hanoi(n, False)
        game.solve()
        assert game.state.towers == [
            [],
            [],
            list(range(n, 0, -1))
        ]


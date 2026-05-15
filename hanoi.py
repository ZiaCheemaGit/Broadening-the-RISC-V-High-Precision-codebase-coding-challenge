import sys


class HanoiState:
    """
    Store the current state of Game
    """
    def __init__(self, n: int, graphics: bool):

        self.total_moves = 0

        # Number of Disks
        self.n = n

        # Initial State of towers
        self.towers = [
            list(range(n, 0, -1)),  # [n, n-1, n-2, ..., 2, 1] 
            [],
            []
        ]

        # print Initial State
        if graphics:
            print("Initial State")
            self.display()
    
    def move(self, start: int, end: int):
        """
        Move top disk from tower number start to tower number end
        """

        disk = self.towers[start - 1].pop()
        self.towers[end - 1].append(disk)
        self.total_moves += 1

    def display(self):
        """
        Print the current state of towers
        """

        width = self.n * 2 + 1

        for level in range(self.n - 1, -1, -1):
            for tower in self.towers:
                if level < len(tower):
                    disk_size = tower[level]
                    disk = "=" * (disk_size * 2 - 1)
                else:
                    disk = "|"

                print(disk.center(width), end="   ")

            print()

        print("-" * ((width + 3) * 3))

        labels = ["A", "B", "C"]

        for label in labels:
            print(label.center(width), end="   ")

        print("\n")


class Hanoi:
    def __init__(self, n: int, graphics: bool):
        
        # Weather to print states of Game or not 
        self.graphics = graphics

        # Initialize state of towers
        self.state = HanoiState(n, graphics)   
        
        # Number of Disks
        self.n = n

    def solve(self, n: int = None, start: int = 1, end: int = 3):
        """
        Recursive solver function 
        """

        # Use self.n on first call 
        if n == None: 
            n = self.n

        # Move last disk to solve
        if n == 1:
            self.move_disk(start, end)
            return
        
        # temp tower where all disks except
        # the largest disk are to be moved
        other = 6 - (start + end)
        self.solve(n - 1, start, other)

        # Move largest disk
        self.move_disk(start, end)

        # Solve remainig disks
        self.solve(n - 1, other, end)

    def move_disk(self, start: int, end: int):
        """
        Move the disk and print that move along with state
        """ 

        self.state.move(start, end)
        print(f"{start} -> {end}")
        if self.graphics:
            self.state.display()


def main():
    
    numberOfDisks = 0
    graphics = True

    if len(sys.argv) == 2:
        numberOfDisks = int(sys.argv[1])

    elif len(sys.argv) == 3:
        numberOfDisks = int(sys.argv[1])
        graphics = sys.argv[2] == "True"

    else:
        print("Usage: python3 hanoi.py <N> <G>")
        print("N = number of disks (Accept a Natural Number E.g 1, 2, 3, ...)")
        print(f"G = print terminal graphics")
        sys.exit()

    if numberOfDisks < 1: 
        print("Invalid number of Disks")

    game = Hanoi(numberOfDisks, graphics)
    game.solve()
    print(f"Total Moves Performed = {game.state.total_moves}")

if __name__ == "__main__":
    main()




import random

CHOICES: tuple = ('R', 'P', 'S')
BEATS: dict = {
    'R': 'S',
    'S': 'P',
    'P': 'R'
}
RPS: dict = {
    'R': "Rock",
    'P': "Paper",
    'S': "Scissors"
}
MESSAGE: str = "Game modes: User vs. Computer (U) | Computer vs. Computer (C)"


class Player:
    def __init__(self):
        self.name: str = ""
        self.type: str = ""  # Either "user" or "bot"
        self.move: str = ''
        self.score: int = 0
    
    def play(self):
        """Make a move"""
        if self.type == "bot":
            self.move = random.choice(CHOICES)
        elif self.type == "user":
            while True:
                move = input("What's your choice?: ")
                if move.upper() in CHOICES:
                    self.move = move.upper()
                    break
                else:
                    print("Invalid input")
        else:
            print("Invalid player type")


class Game:
    def __init__(self):
        self.player1: Player = Player()
        self.player2: Player = Player()
    
    def gameMode(self):
        """Game modes: User vs. Computer (U) | Computer vs. Computer (C)"""
        while True:
            gameMode = input(f"Select game mode\n{MESSAGE}\n> ")
            if gameMode.upper() == 'U':
                self.player1.type = "user"
                self.player1.name = "You"
                self.player2.type = "bot"
                self.player2.name = "Computer"
                break
            elif gameMode.upper() == 'C':
                self.player1.type = "bot"
                self.player1.name = "Computer 1"
                self.player2.type = "bot"
                self.player2.name = "Computer 2"
                break
            else:
                print("Invalid input")
        
    def winner(self):
        """Returns the winner Player if there's a winner, None if there's a tie"""
        if BEATS[self.player1.move] == self.player2.move:
            return self.player1
        elif self.player1.move == self.player2.move:
            return None
        else:
            return self.player2
        
    def gameRound(self):
        """One round of Rock Paper Scissors"""
        self.player1.play()
        self.player2.play()
        print(f"{self.player1.name} played {RPS[self.player1.move]}")
        print(f"{self.player2.name} played {RPS[self.player2.move]}")
        if self.winner() != None:
            print(f"{self.winner().name} wins!" if self.winner().name != "You" else "You win!")
            if self.winner() == self.player1:
                self.player1.score += 1
            else:
                self.player2.score += 1
        else:
            print("Tie")
        print(f"{self.player1.name}: {self.player1.score} | {self.player2.name}: {self.player2.score}")
    
    def game(self):
        """The game itself"""
        self.gameMode()
        while True:
            try:
                rounds = int(input("How many rounds?\n> "))
            except:
                print("Enter an integer, please")
            else:
                if rounds > 0:
                    break
                else:
                    print("Enter a number that makes sense, please")
        for i in range(rounds):
            print(f"\nRound {i + 1}:")
            self.gameRound()


if __name__ == "__main__":
    G = Game()
    G.game()

"""
guesses a letter 
"""
from game.console import Console 

class Jumper:
    def __init__(self):
        self.console = Console()
    
    def guess(self):
        letter = self.console.read_stuff('Guess a letter [a-z]: ')
        return letter 
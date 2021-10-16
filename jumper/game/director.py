"""
Calls all the classes and methods
"""
from game.cutter import Cutter
from game.jumper import Jumper
from game.console import Console

class Director:

    def __init__(self):
        self.cutter = Cutter()
        self.jumper = Jumper()
        self.console = Console()
        self.keep_playing = True
        self.guess = ''
        self.win = ''
    
    def start_game(self):
        #assign the random word
        self.cutter.pick_random_word()
        self.console.print_stuff(self.cutter.blank_spaces())

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        #get the guessed letter
        self.guess = self.jumper.guess()

    def do_updates(self):
        self.output = (self.cutter.word_check(self.guess))
        if self.output == 'Game Over':
            self.keep_playing = False
        elif self.cutter.win_check():
            self.keep_playing = False
            self.win = ('You Win!')

    def do_outputs(self):
        self.cutter.para_print()
        print(self.output)
        print(self.win)
        print(self.cutter.clean_list)
        if self.output == 'Game Over':
            self.console.print_stuff(f"The word was {self.cutter.word_to_guess}")




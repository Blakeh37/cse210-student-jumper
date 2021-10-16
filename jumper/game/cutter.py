
"""
Has list of words
picks a random word
determines if the guess from the jumper is in the word
either cuts his parachute or displays the letter of the word
"""
import random

class Cutter:
    
    def __init__(self):
        
        self.guessed_letters = ['', '']
        self.blanks = []
        self.letters = []
        self.word_to_guess = ''
        self.parachute_index = 0
        self.clean_list = ''

        self.words = ['ribbon', 'peak', 'hardware', 'card', 'chain', 'adult', 'restaurant', 'failure',\
            'cheese', 'tape', 'celebration', 'memorial', 'victory', 'coding', 'water', 'chicken', 'portrait',\
            'accept', 'aluminium', 'choke', 'write', 'explosion', 'relate', 'discount', 'integrity', \
            'instrument', 'delicate', 'golf', 'computer', 'answer', 'potential', 'earthquake', 'education']

        self.parachute = ['''
             ___  
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \ ''', 
             ''' 
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \ ''',
             '''
            \   / 
             \ /  
              0   
             /|\  
             / \ ''',
             ''' 
             \ /  
              0 
             /|\  
             / \ ''',
             '''  
              X 
             /|\  
             / \ '''
             ]
        

    def pick_random_word(self):
        print(self.parachute[self.parachute_index])

        #gets a random number and uses that to find a random index of the list of words
        num_words = len(self.words) - 1
        num = random.randint(0, num_words)
        word = self.words[num]

        self.word_to_guess = word
        self.letters = list(word)

    def para_print(self):
        print(self.parachute[self.parachute_index])

    def blank_spaces(self):
        #determines amount of blanks to create
        num_blanks = len(self.word_to_guess)
        blanks = '_' * num_blanks

        self.blanks = list(blanks)
        self.clean_list = ' '.join(self.blanks)

        return (' '.join(self.blanks))

    def word_check(self, letter_guess):
        #check to see if the guessed letter is in the word
        
        if letter_guess in self.letters and letter_guess not in self.guessed_letters:
            self.guessed_letters.append(letter_guess)
            self.change_blanks()
            return ('Nice Job!')
        elif letter_guess in self.guessed_letters:
            return ('You already Guessed that letter')
        else:
            self.guessed_letters.append(letter_guess)
            self.parachute_index = self.parachute_index + 1
            if self.parachute_index == 4:
                return 'Game Over'
            else:
                return('Try again')
         

    def change_blanks(self):
        self.guess = self.guessed_letters[-1]
        length = len(self.blanks)
        
        for index in range(length):
            if self.guess == self.letters[index]:
                self.blanks[index] = self.guess
        self.clean_list =(' '.join(self.blanks))

    def win_check(self):
        if '_' not in self.blanks:
            return True
        else:
            return False

        

                
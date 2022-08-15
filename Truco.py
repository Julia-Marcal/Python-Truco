from ast import Pass
from itertools import count
from pickle import TRUE
import random
import string
from timeit import repeat

"""
#Array of cards and suits.
#Random list of cards of the pc and the user.
#Random card on the table.

#3 rounds 
#Make pc play smart (play strong cards when losing) (And teach how to lie). 

#Teach the rules of the game:
    #Cards
        #Manilha is the strongest card, it is the card after the "vira".
        #Vira is a random card put on the table to define what the manilha will be.
        #Order of the strongest number and suits.

    #Points (max 12 points)
        #Truco not accepted = 1 point.
        #Truco accepted = 3 Points.
        #Six (truco accepted with 6 additional points).
        #Nine (truco accepted with 9 additional points).
        #Twelve (truco accepted with 12 additional points).
    
    #Rules 
        #When someone has 11 points in the game is not legal to ask for truco.
        #When two player has 11 points everybody show their cards and play like this until the end.
        #You can choose not to show your card, but it won't have any value to the round.

    #Draw
        #If the game draws on the first round, the person who wins the second round wins. 
        #If the game draws on the second round, the person won the first round wins.
        #If the game draws on the first and second round, the one who wins the third will take the points.
        #If the game draws on the third round, the person won the first round wins.
        #if all rounds are draw the there is no points won.
    

"""

class Truco:
    truco_cards = ['3','2','a','k','j','q','7','6','5','4']
    truco_suits = ['Clover','Hearts','Spades','Diamonds']
    def __init__(self):
        
        self.user_cards = []
        self.pc_cards = []
        self.vira = random.choice(self.truco_cards)
        self.vira_pos = int(self.truco_cards.index(self.vira))

        try:
            self.manilha = self.truco_cards[self.vira_pos + 1]
        except:
            self.manilha = self.truco_cards[-1]
        
        print('\n')
        print('-'*15,'TRUCO','-'*15)
        print(f'The manilha is: {self.manilha}')

        #PC CARDS
        while True:
            self.pc_cards.append(random.choice(self.truco_cards))

            if len(self.pc_cards) > 2:
                break
        
        #USER CARDS
        while True:
            a_card = self.user_cards.append(random.choice(self.truco_cards))
            b_card = self.user_cards.append(random.choice(self.truco_cards))
            c_card = self.user_cards.append(random.choice(self.truco_cards))
            
            if c_card == b_card or  c_card == a_card or b_card == a_card:
                check_rep = TRUE

            if len(self.user_cards)> 2:
                break 

        #PC AND USER SUITS
        while True:
            self.user_cards.append(random.choice(self.truco_suits))
            self.pc_cards.append(random.choice(self.truco_suits))

            if len(self.pc_cards) > 5:
                break

        #Checking pc cards
        for cont in range(3):

            #Has Manilha card
            if self.pc_cards[cont] == self.manilha:
                if cont == 0:
                    first_card = "Manilha"
                    cont += 1

                elif cont == 1:
                    sec_card = "Manilha"
                    cont +=  1
                
                elif cont == 2:
                    third_card = "Manilha"
                    cont +=  1
                    
                    
                if cont == 3:
                    self.value_card = [first_card, sec_card, third_card]
                    break

            #Has Very good card       
            elif self.pc_cards[cont] in self.truco_cards[:3]:
                if cont == 0:
                    first_card = "Very Good"
                    cont += 1

                elif cont == 1:
                    sec_card = "Very Good"
                    cont +=  1
                
                elif cont == 2:
                    third_card = "Very Good"
                    cont +=  1
                    
                    
                if cont == 3:
                    self.value_card = [first_card, sec_card, third_card]
                    break

            #Has Good card           
            elif self.pc_cards[cont] in self.truco_cards[2:6]:
                if cont == 0:
                    first_card = "Good"
                    cont += 1 

                elif cont == 1:
                    sec_card = "Good"
                    cont += 1
                
                elif cont == 2:
                    third_card = "Good"
                    cont +=  1

                if cont == 3:
                    self.value_card = [first_card, sec_card, third_card]
                    break
            
            #Has Bad card   
            elif self.pc_cards[cont] in self.truco_cards[5:-1]:
                if cont == 0:
                    first_card = "Bad"
                    cont += 1 
                
                elif cont == 1:
                    sec_card = "Bad"
                    cont += 1 
                
                elif cont == 2:
                    third_card = "Bad"
                    cont +=  1
                
                if cont == 3:
                    self.value_card = [first_card, sec_card, third_card]
                    break    

        def strategy_pc():
            random_strategy = random.randint(1, 3)
            if random_strategy == 1:
                if self.value_card[0] == 'Manilha' or self.value_card[0] == 'Very Good':
                    if self.value_card[1] == 'Manilha' or self.value_card[1] == 'Very Good' or\
                        self.value_card[2] == 'Manilha' or self.value_card[2] == 'Very Good':
                        #if pc has this cards it can use this strategy
                        #so it can call truco 
                        pass
                else:
                    #can't use the strategy 
                    #play normal
                    #doesn't accept truco
                    print('ok2')
                    pass
        
        #rounds for user          
        for round in range(3):

            #First round
            if round == 0:
                print(f'Your cards are: {self.user_cards}')
                round_1 = input(f'What card do you want to use? ')
                
                #check if user uses repeated cards
                if check_rep:
                    
                    if round_1 == self.user_cards[0] and round_1 == self.user_cards[1]\
                        or round_1 == self.user_cards[0] and round_1 == self.user_cards[2]\
                            or round_1 == self.user_cards[1] and round_1 == self.user_cards[2]:
                        
                        if round_1 == self.user_cards[0] and round_1 == self.user_cards[1]:
                            print(f'\nThe cards {self.user_cards[0]} {self.user_cards[3]} and {self.user_cards[1]} {self.user_cards[4]} are repeated')
                            rep_round_1 = input(str('Do you wanna use the first card?\n[0=no, 1=yes]: '))

                            if rep_round_1 == 0:
                                #b_card
                                usercard_chose1 = [self.self.user_cards[1], self.user_cards[4]]
                                self.user_cards.remove(self.user_cards.remove[1])
                                self.user_cards.remove(self.user_cards.remove[4])
                                round += 1

                            elif rep_round_1 == 1:
                                #a_card 
                                usercard_chose1 = [self.self.user_cards[0], self.user_cards[3]]
                                self.user_cards.remove(self.user_cards.remove[0])
                                self.user_cards.remove(self.user_cards.remove[3])
                                round += 1

                        elif round_1 == self.user_cards[0] and round_1 == self.user_cards[2]:
                            print(f'\nThe cards {self.user_cards[0]} {self.user_cards[3]} and {self.user_cards[2]} {self.user_cards[5]} are repeated')
                            rep_round_1 = input(str('Do you wanna use the first card?\n[0=no, 1=yes]: '))

                            if rep_round_1 == 0:
                                #c_card
                                usercard_chose1 = [self.self.user_cards[2], self.user_cards[5]]
                                self.user_cards.remove(self.user_cards.remove[2])
                                self.user_cards.remove(self.user_cards.remove[5])
                                round += 1

                            elif rep_round_1 == 1:
                                #a_card 
                                usercard_chose1 = [self.self.user_cards[0], self.user_cards[3]]
                                self.user_cards.remove(self.user_cards.remove[0])
                                self.user_cards.remove(self.user_cards.remove[3])
                                round += 1

                        elif round_1 == self.user_cards[1] and round_1 == self.user_cards[2]:
                            print(f'\nThe cards {self.user_cards[1]} {self.user_cards[4]} and {self.user_cards[2]} {self.user_cards[5]} are repeated')
                            rep_round_1 = input(str('Do you wanna use the first card?\n[0=no, 1=yes]: '))

                            if rep_round_1 == 0:
                                #c_card
                                usercard_chose1 = [self.self.user_cards[2], self.user_cards[5]]
                                self.user_cards.remove(self.user_cards.remove[2])
                                self.user_cards.remove(self.user_cards.remove[5])
                                round += 1

                            elif rep_round_1 == 1:
                                #b_card 
                                usercard_chose1 = [self.self.user_card[1], self.user_cards[4]]
                                self.user_cards.remove(self.user_cards.remove[1])
                                self.user_cards.remove(self.user_cards.remove[4])
                                round += 1
 
                #else
                if round_1 in self.user_cards:
                    if round_1 == self.user_cards[0]:
                        usercard_chose1 = [self.self.user_cards[0], self.user_cards[3]]
                        self.user_cards.remove(self.user_cards[3])
                        self.user_cards.remove(round_1)
                        round += 1
                        
                    elif round_1 ==  self.user_cards[1]:
                        usercard_chose1 = [self.self.user_cards[1], self.user_cards[4]]
                        self.user_cards.remove(self.user_cards[4])
                        self.user_cards.remove(round_1)
                        round += 1

                    elif round_1 ==  self.user_cards[2]:
                        usercard_chose1 = [self.self.user_cards[2], self.user_cards[5]]
                        self.user_cards.remove(self.user_cards[5])
                        self.user_cards.remove(round_1)
                        round += 1
                


                #error
                else:
                    print('Error, this card is not available')
                    return

            #Second round
            if round == 1:
                print(f'\nNow the cards available are: {self.user_cards}')
                round_2 = input(f'Which one do you wanna use? ')

                #check if repeated cards are still available 
                if check_rep:

                    if round_2 == self.user_cards[0] and round_2 == self.user_cards[1]:
                            print(f'\nThe cards {self.user_cards[0]} {self.user_cards[2]} and {self.user_cards[1]} {self.user_cards[3]} are repeated')
                            rep_round_2 = input(str('Do you wanna use the first card in this order?\n[0=no, 1=yes]: '))

                            if rep_round_1 == 0:
                                #b_card
                                usercard_chose2 = [self.self.user_cards[1], self.user_cards[3]]
                                self.user_cards.remove(self.user_cards.remove[1])
                                self.user_cards.remove(self.user_cards.remove[3])
                                round += 1

                            elif rep_round_1 == 1:
                                #a_card 
                                usercard_chose2 = [self.self.user_cards[0], self.user_cards[2]]
                                self.user_cards.remove(self.user_cards.remove[0])
                                self.user_cards.remove(self.user_cards.remove[2])
                                round += 1


                if round_2 in self.user_cards:
                    if round_2 == self.user_cards[0]:
                        usercard_chose2 = [self.self.user_cards[0], self.user_cards[2]]
                        self.user_cards.remove(self.user_cards[2])
                        self.user_cards.remove(round_2)
                        round += 1
                        
                    elif round_2 ==  self.user_cards[1]:
                        self.user_cards.remove(self.user_cards[3])
                        self.user_cards.remove(round_2)
                        round += 1
                else:
                    print('Error, this card is not available')
                    return

            #Terceiro round
            if round == 2:
                print(f'The only card left is: {self.user_cards}')
                usercard_chose3 = [self.self.user_cards[0], self.user_cards[1]]
                self.user_cards.remove(self.user_cards[0] and self.user_cards[1])
                return

truco = Truco()

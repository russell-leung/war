import random

#Class to create the deck that will be used in the game
class Deck:
  def __init__(self):
    self.cards = []
    self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    self.numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

  #Puts together all the cards ie. Ace of Clubs, and adds them to an array, aka the deck
  def arrange_deck(self):
    for x in self.numbers:
      for y in self.suits:
        self.cards.append(f"{x} of {y}")

  #Utalizing random.shuffle, the cards inside of the deck are shuffled into a random order
  def shuffle_deck(self):
    random.shuffle(self.cards)

  #The shuffled deck is split in half, one half for each user
  def assign_cards(self):
    user1_deck = self.cards[:26]
    user2_deck = self.cards[26:]
    return [user1_deck, user2_deck]

#This class is where the program for the actual game of war is
class Game:
  def __init__(self, user_decks):
    self.user1 = user_decks[0]
    self.user2 = user_decks[1]

    #Game Statistics, will keep track of certain game stats while the game runs, printed at the end
    self.play_count = 0
    self.user1_wins = 0
    self.user2_wins = 0
    self.war_count = 0
    self.user1_war_wins = 0
    self.user2_war_wins = 0

  
  #Does all the actions in the game, converts the cards to number values to compare them to each other, asseses wars between users, and adds and removes won or lost cards into the users' correspinding decks
  def check_cards(self):
    cards1 = []
    cards2 = []

    #Takes out the first word of each card and puts it into an array for each user, returning an array containig both arrays
    def check_value():
      for x in self.user1:
        x = x.split()
        x = x.pop(0)
        cards1.append(x)

      for x in self.user2:
        x = x.split()
        x = x.pop(0)
        cards2.append(x)

      return cards1 + cards2
    
    #Assigns the number values to each card using the keywords of the cards pulled by the check_value function and returns a 2D array with the number vaues of each user's cards
    def assign_values(cards_numbers_words):
      for x in range(len(cards_numbers_words)):
        if(cards_numbers_words[x] == "Two"):
          cards_numbers_words[x] = 2
        if(cards_numbers_words[x] == "Three"):
          cards_numbers_words[x] = 3
        if(cards_numbers_words[x] == "Four"):
          cards_numbers_words[x] = 4
        if(cards_numbers_words[x] == "Five"):
          cards_numbers_words[x] = 5
        if(cards_numbers_words[x] == "Six"):
          cards_numbers_words[x] = 6
        if(cards_numbers_words[x] == "Seven"):
          cards_numbers_words[x] = 7
        if(cards_numbers_words[x] == "Eight"):
          cards_numbers_words[x] = 8
        if(cards_numbers_words[x] == "Nine"):
          cards_numbers_words[x] = 9
        if(cards_numbers_words[x] == "Ten"):
          cards_numbers_words[x] = 10
        if(cards_numbers_words[x] == "Jack"):
          cards_numbers_words[x] = 11
        if(cards_numbers_words[x] == "Queen"):
          cards_numbers_words[x] = 12
        if(cards_numbers_words[x] == "King"):
          cards_numbers_words[x] = 13
        if(cards_numbers_words[x] == "Ace"):
          cards_numbers_words[x] = 14

      user1_cards_numbers = cards_numbers_words[:26]
      user2_cards_numbers = cards_numbers_words[26:]
      return [user1_cards_numbers, user2_cards_numbers]

    #Places the two users cards against eachother (putting them in "war"), checks to see which card has the higher number or if the cards are equal, calls more functions within itself to add an remove cards based of the "wars"
    def check_cards_against_eachother(user_card_values):
      print(user_card_values)

      #If the cards are not equal, this function compares each users cards and adds both users cards to the end of the user's deck who had the higher card, then it removes the first card from both players' decks
      def normal_play(user_card_values):
        if int(user_card_values[0][0]) > int(user_card_values[1][0]) or  int(user_card_values[1][0]) > int(user_card_values[0][0]):
          if int(user_card_values[0][0]) > int(user_card_values[1][0]): 
            user_card_values[0].append(user_card_values[0][0])
            user_card_values[0].append(user_card_values[1][0])

            self.user1_wins += 1
            
            print("True")


          if int(user_card_values[1][0]) > int(user_card_values[0][0]):
            user_card_values[1].append(user_card_values[0][0])
            user_card_values[1].append(user_card_values[1][0])

            self.user2_wins += 1

            print("false")

          user_card_values[0].pop(0)
          user_card_values[1].pop(0)

      #War function, it makes sure that the cards are equal, then takes the value of the 4th card after the flipped one and compares them between the users, it will continue until one user has a lower card OR one user cannot supply enough cards for the war in which it will end the game
      def war(user_card_values):
        
        if int(user_card_values[0][0]) == int(user_card_values[1][0]):
          x = 0

          #Most important lines of the function, it using a count variable checks every 4th card after the first card until one player's card is greater than the other
          while int(user_card_values[0][x]) == int(user_card_values[1][x]):
            x += 4
            #These two if statments end the game if one player can't supply enough cards for the war
            if len(user_card_values[0]) < x + 1:
              self.user2_war_wins += 1
              return False
            
            if len(user_card_values[1]) < x + 1:
              self.user1_war_wins += 1
              return True

          #If the first user's 4x's card is greater than the other's it will add all the cards that were used in the war to the first user's deck and remove all the cards involved in the war from both players' decks
          if user_card_values[0][x] > user_card_values[1][x]:
            
            self.user1_war_wins += 1

            for num in range(x + 1):
              user_card_values[0].append(user_card_values[0][0])
              user_card_values[0].append(user_card_values[1][0])
              user_card_values[0].pop(0)
              user_card_values[1].pop(0)

          #Does the same thing as the function above just for user two
          elif user_card_values[1][x] > user_card_values[0][x]:

            self.user2_war_wins += 1

            for num in range(x + 1):
              user_card_values[1].append(user_card_values[0][0])
              user_card_values[1].append(user_card_values[1][0])
              user_card_values[0].pop(0)
              user_card_values[1].pop(0)

      #Runs while both players have cards in their deck
      while len(user_card_values[0]) != 0 or len(user_card_values[1]) != 0:

        #If either player doesn't have any cards these two if statements will end the game
        if len(user_card_values[0]) == 0:
          print("\nUser Two is the winner!")
          return
        
        if len(user_card_values[1]) == 0:
          print("\nUser One is the winner!")
          return

        self.play_count += 1

        #These two statments determine if the cards being placed are equal or not and calls the corespindgin functions to play the game 
        if int(user_card_values[0][0]) > int(user_card_values[1][0]) or int(user_card_values[1][0]) > int(user_card_values[0][0]):
          normal_play(user_card_values)

        elif int(user_card_values[0][0]) == int(user_card_values[1][0]):

          #If a user fails to war, these if statments will end the game
          winner = war(user_card_values)

          self.war_count += 1

          if winner == False:
            print("\nUser One, you have failed to WAR. User Two is the winner! ")
            return

          if winner == True:
            print("\nUser Two, you have failed to WAR. User One is the winner! ")
            return

        print(user_card_values)


    cards_numbers_words = check_value()
    user_card_values = assign_values(cards_numbers_words)
    check_cards_against_eachother(user_card_values)

    return [self.play_count, self.user1_wins, self.user2_wins, self.war_count, self.user1_war_wins, self.user2_war_wins]



deck = Deck()
deck.arrange_deck()
deck.shuffle_deck()
user_decks = deck.assign_cards()

print(user_decks)
print()
game = Game(user_decks)
game_stats = game.check_cards()

play_count = game_stats[0]
user1_wins = game_stats[1]
user2_wins = game_stats[2]
war_count = game_stats[3]
user1_war_wins = game_stats[4]
user2_war_wins = game_stats[5]

#Game Stats
print(f"Total Game Plays: {play_count}\nUser One Total Normal Play Wins: {user1_wins}\nUser Two Total Normal Play Wins: {user2_wins}\nTotal Number Of Wars: {war_count}\nUser One Total Wars Won: {user1_war_wins}\nUser Two Total Wars Won: {user2_war_wins}")

#find a way to display actions, ie after every turn put the amount of cards each side has, during the turn display the card placed down by both players
#I should make a counter with all the statistics, how many turns it took, how many turns each payer won, how many wars, etc
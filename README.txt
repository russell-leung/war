# Problem Statement
-----------------
War is a game in which two players utalize a deck of 52 cards, the deck is randomly suffled and put into 
two seperate decks of 26, one for each user. With he highet card being the ace and the lowest card being the 2,
the uses simotaniously flip the first card in their decks and the player with the highest value card takes
both player's cards. If the users both flip a card of the same value then a "war" will start. Both users will
place 3 cards face dow and flip their 4th card, the player with the highest value card will take all the cards.
If the users again place down the same value card, another war will start. The game continues until one player
has 0 cards left in their deck.


# Requirements
------------
- get shuffled deck
- wars
- lose/win conditions
- game stats display


# Algorithm (Pseudocode)
----------------------
Program creates a standard deck of 52 cards. Program shuffles deck of cards. Program splits the deck into two
smaller decks of 26 cards for each user. Program then begins simulation and simulates a game of war, comparing
the first card of each user and awarding both cards to the user with the highest value card (won cards are 
added to the end of the user's deck). If the user's both have a card of the same value, the program will 
begin a "war" in which it will skip the next 3 cards of the users' decks and compare the 4th card. The player
with the card of the most value will take all cards, including their original cards, the war cards, and the 
final card flipped. If both users happen to have the same card again, another war will simulate. The game will
continue until one user has either 0 cards or canot supply enough cards for a war, in which the program will 
end the game and declare the winner.

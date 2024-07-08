import random

#variable that holds the value for card counting
app.cardCounting = 0
countBox = [
    Rect(330, 0, 70, 70, fill = None, border = 'black'),
    Label('Count', 365, 17, size = 20)
    ]
count = Label(app.cardCounting, 365, 47, size = 40)

app.totalPlayedCards = 0
#how many cards the user has
app.currentCardCountUser = 1
#how many cards the dealer has 
app.currentCardCountDealer = 1
#what score the user currently has
app.currentScoreUser = 0 
#what score the dealer currently has
app.currentScoreDealer = 0 

app.userWins = 0
app.dealerWins = 0

#displays the current scores 
app.userScoreLabel = Label(app.currentScoreUser, 200, 220)
app.dealerScoreLabel = Label (app.currentScoreDealer, 200, 180)

#displays total number of wins
Label("User:", 190, 385, size = 25)
Label("Dealer:", 190, 15, size = 25)
app.userWinsLabel = Label(app.userWins, 230, 387, size = 25)
app.dealerWinsLabel = Label(app.dealerWins, 240, 16, size = 25)

centerLine = Line(0, 200, 400, 200)

# Start by making a function that creates the cards. Lets not worry too much about visual accuracy. 
#We just need the important information : suit, number, and then which side the card is on, user or dealer, and then also maybe which position the card is in (first card, second card, third card)
#I should try to make my own class "card". 


#Class that creates each card
class Card():
    def __init__(self, number, suit, position, side):
        self.number = number
        self.suit = suit
        self.side = side
        self.position = position
        
        
    def makeCard(self):
        #cards on the user side
        card = []
        if self.side == "user":

            
            base = Rect(200, 250, 70, 100, fill = 'white', border = 'black', borderWidth = 3)
    
            topCorner = [200, 250]
            bottomCorner = [270, 350]
            
            #if there is already a card on the user side, the new card is moved to the left 
            base.centerX -= 25 * (self.position -1)
            topCorner[0] -= 25 * (self.position -1)
            bottomCorner[0] -= 25 * (self.position -1)
            
            card.append(base)
                
        #do the same process, but on the dealer side 
        elif self.side == 'dealer':
            base = Rect(200, 50, 70, 100, fill = 'white', border = 'black', borderWidth = 3)
            topCorner = [200, 50]
            bottomCorner = [270, 150]
            
            base.centerX -= 25 * (self.position -1)
            topCorner[0] -= 25 * (self.position -1)
            bottomCorner[0] -= 25 * (self.position -1)
            
            card.append(base)

        #put in the value and suit of the card
        card.append(Label(self.number, topCorner[0] + 13, topCorner[1] + 13, size = 16))
        card.append(Label(self.number, bottomCorner[0] - 13, bottomCorner[1] - 13, size = 16))
        card.append(Label(self.suit, base.centerX, base.centerY))
        
        return card
            
suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
faceCards = ["J", "Q", "K", "A"]

#this is the original deck, not to be changed. Make copies of this deck to pull new cards from 
OGDeck = []

#place all 52 cards into the original deck
for suit in suits:
    for i in range(2, 11):
        OGDeck.append([i, suit])
    for face in faceCards:
        OGDeck.append([face, suit])
        
        
#make a copy of the deck to pull cards from
app.currentDeck = []
for card in OGDeck:
    app.currentDeck.append(card)


#when the player wants to take another card
HitMeButton= [
    Circle(350, 350, 35, fill = 'green'),
    Label("Hit Me", 350, 350, size = 18)
    ]

    
#when the player doesn't want a new card
NoThanksButton = [
    Circle(350, 255, 35, fill = 'red'),
    Label("No", 350, 245, size = 16),
    Label('Thanks', 350, 260, size = 16 )
    ]


#function to update count
def updateCount(value):
    if value not in faceCards:
        if value < 7:
            app.cardCounting += 1
        if value == 10:
            app.cardCounting -= 1
    else:
        app.cardCounting -= 1
        
    count.value = app.cardCounting

#list that holds all the current cards on the table
app.playedCards = []

#loads new deck
def newDeck():
    for card in OGDeck:
        app.currentDeck.append(card)

#function that brings in a new card from the current deck onto the users side#
def nextCardUser():
    #display the card and add it to played cards
    newCardKey = random.choice(app.currentDeck)
    
    #update the count with the newCard value
    updateCount(newCardKey[0])
    
    newCard = Card(newCardKey[0], newCardKey[1], app.currentCardCountUser, "user")
    app.playedCards.append(newCard.makeCard())
    
    #determine how much to add to the users score
    if newCard.number != 'J' and newCard.number != 'K' and newCard.number != 'Q' and newCard.number != 'A':
        app.currentScoreUser += newCard.number
    elif newCard.number == 'A':
        if app.currentScoreUser > 10:
            app.currentScoreUser += 1
        else:
            app.currentScoreUser += 11
    else:
        app.currentScoreUser += 10
    
    
    #update current hand score label 
    app.userScoreLabel.value = app.currentScoreUser
    
    #remove the card from the copy deck
    app.currentCardCountUser += 1
    app.currentDeck.remove(newCardKey)
    
    
    
#function that brings in a new card from the current deck onto the users side
def nextCardDealer():
    #display the card and add it to played cards
    newCardKey = random.choice(app.currentDeck)
    
    #update the count with the newCard value
    updateCount(newCardKey[0])

    newCard = Card(newCardKey[0], newCardKey[1], app.currentCardCountDealer, "dealer")
    app.playedCards.append(newCard.makeCard())
    
    #determine how much to add to the dealers score
    if newCard.number != 'J' and newCard.number != 'K' and newCard.number != 'Q' and newCard.number != 'A':
        app.currentScoreDealer += newCard.number
    elif newCard.number == 'A':
        if app.currentScoreDealer > 10:
            app.currentScoreDealer += 1
        else:
            app.currentScoreDealer += 11
    else:
        app.currentScoreDealer += 10
    
    #update curent hand score label
    app.dealerScoreLabel.value = app.currentScoreDealer
    
    #remove the card from the copy deck
    app.currentCardCountDealer += 1
    app.currentDeck.remove(newCardKey)




def whoWon():
    #checking if the user one or if the dealer one or if draw
    if app.currentScoreUser > app.currentScoreDealer and app.currentScoreUser <= 21:
        return 'user'
    elif app.currentScoreDealer > app.currentScoreUser and app.currentScoreDealer <= 21:
        return 'dealer'
    elif app.currentScoreDealer > 21 and app.currentScoreUser< 22:
        return 'user'
    elif app.currentScoreUser > 21 and app.currentScoreDealer < 22:
        return 'dealer'
    elif app.currentScoreDealer > 21 and app.currentScoreUser > 21:
        return 'draw'
    elif app.currentScoreDealer == app.currentScoreUser:
        return 'draw'
        



#clears all the cards at the end of round, resets scores and card counts
def clearScreen():
    #removing the cards from the screen
    for list in app.playedCards:
        for item in list:
            item.visible = False
            
    #reseting the counters
    app.currentCardCountUser = 1
    app.currentCardCountDealer = 1
    app.currentScoreUser = 0
    app.currentScoreDealer = 0
    app.userScoreLabel.value = app.currentScoreUser
    app.dealerScoreLabel.value = app.currentScoreDealer
    
    #reset the card placement order
    app.dealerGo = True
    



app.dealerGo = True

def onMousePress(mouseX, mouseY):
    #check if new deck is needed, call newDeck if so
    if len(app.currentDeck) < 1:
        newDeck()
    
    
    #user asks for another card
    if HitMeButton[0].contains(mouseX, mouseY):
        nextCardUser()
        #once the user asks for the first card, the dealers first 2 cards are revealed
        if app.dealerGo == True:
            app.dealerGo = False
            nextCardDealer()
            nextCardDealer()
        if app.currentScoreUser > 21: 
            app.over21 = True 
    #user holds
    elif NoThanksButton[0].contains(mouseX, mouseY):
        #once the user is done taking cards, the dealer gets more cards until they reach at least 17
        if app.currentScoreUser < 22:
            while app.currentScoreDealer < 17:
                nextCardDealer()
        sleep(1)
        winner = whoWon()
        clearScreen()
        #tallying total score of rounds
        if winner == 'user':
            app.userWins += 1
        elif winner == 'dealer':
            app.dealerWins += 1
        
        #updating total score label
        app.userWinsLabel.value = app.userWins
        app.dealerWinsLabel.value = app.dealerWins
    
        

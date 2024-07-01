#Hyperclass.py
#presets
import random

ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
colors = ['Black','Red']
fullMap = [["╔","═","═","╗","╔","╣"],
           ["║","╔","╦","╩","╣","║"],
           ["╚","╝","║","╥","╨","║"],
           ["╔","╦","╝","╨","╔","╝"],
           ["╩","╩","═","═","╩","╡"]]
curMap = [["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["╩","?","?","?","?","?"]]
baseMap = [["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["╩","?","?","?","?","?"]]

# Chat
class InteractionV1:
    def __init__(self,diaRoom):
        self.dia=diaRoom
        self.tE=0
        self.interacting=True
        self.nextGame="Chat"
        self.playerName="Temp"

    def setDia(self,diaRoom):
        self.dia=diaRoom

    def interT(self):
        self.interacting=True

    def interF(self):
        self.interacting=False

    def setNextGame(self,ng):
        if(ng=="CardWar"):
            self.nextGame="CardWar"
        elif(ng=="Zorc"):
            self.nextGame="Zorc"
        elif(ng=="Chat"):
            ng="Chat"
        elif(ng=="None"):
            ng="None"

    def getNextGame(self):
        return self.nextGame

    def getPlayerName(self):
        return self.playerName

    def dialogRoomA(self): #game intro
        self.tE=0
        print("Hello welcome to My Escape Game!")
        print("You are trapped my underground coloseum.")
        print("First, demonstrate your worth by defeating me in Card War!")
        self.playerName = str(input("Enter your Name: "))
        #transition to card war
        self.setNextGame("CardWar")
        self.interacting=False
        #for hyperclass for combined game...

    def dialogRoomB(self): #after losing card war
        print("Unfortunately your luck is weak. I will now drop you in to a maze.")
        print("Just try and escape Zorc!")
        print("[The floor underneath you disapears.]")
        print("[You see a path to right.]")
        print("[You walk right and find yourself in a maze.]")
        #transition to Zorc
        self.setNextGame("Zorc")
        self.interacting=False
        #for hyperclass for combined game...

    def dialogRoomC(self): #after winning card war
        print("Impressive, you were lucky and proved your worth!")
        print("Now I will test your intellegence.")
        print("How many cards were used in the game you just finished")#pose a question
        print("1. Half Deck without Jokers") #roomD
        print("2. Full Deck") #roomE
        print("3. 26 Cards") #roomF
        validC1=False
        while(validC1!=True):
            choice1=str(input("Enter your choice: "))
            if(choice1=="1" or choice1=="2" or choice1=="3"):
                validC1=True
        if(choice1=="1"):
            self.dia="D"
        elif(choice1=="2"):
            self.dia="E"
        elif(choice1=="3"):
            self.dia="F"
        else:
            print("Error invalid choice")
            self.dia="Y"
        self.tE=self.tE+1

    def dialogRoomD(self): #choice1=1
        print("What is the most fearsome insect")#pose a question
        print("1. Water Strider") #roomE
        print("2. Ant") #roomG
        print("3. Cockroach") #roomH
        validC2=False
        while(validC2!=True):
            choice2=str(input("Enter your choice: "))
            if(choice2=="1" or choice2=="2" or choice2=="3"):
                validC2=True
        if(choice2=="1"):
            self.dia="E"
        elif(choice2=="2"):
            self.dia="G"
        elif(choice2=="3"):
            self.dia="H"
        else:
            print("Error invalid choice")
            self.dia="Y"
        self.tE=self.tE+1

    def dialogRoomE(self): #choice1=2 or choice2=1 or choice3=3
        print("Hmm...")
        print("I don't like your answer.")
        print("Just try and escape Zorc!")
        print("[The floor underneath you disapears.]")
        print("[You see a path to right.]")
        print("[You walk right and find yourself in a maze.]")
        #transition to Zorc
        self.setNextGame("Zorc")
        self.interacting=False
        #for hyperclass for combined game...

    def dialogRoomF(self): #choice1=3
        print("What is my favorite Genre:")#pose a question
        print("1. Sci-Fi") #roomH
        print("2. Fantasy") #roomG
        print("3. Non-Fiction") #roomE
        validC3=False
        while(validC3!=True):
            choice3=str(input("Enter your choice: "))
            if(choice3=="1" or choice3=="2" or choice3=="3"):
                validC3=True
        if(choice3=="1"):
            self.dia="H"
        elif(choice3=="2"):
            self.dia="G"
        elif(choice3=="3"):
            self.dia="E"
        else:
            print("Error invalid choice")
            self.dia="Y"
        self.tE=self.tE+1

    def dialogRoomG(self): #choice2=2 or choice3=1
        print("You are smart. Hmm...")
        print("I will give you a choice now.")
        print("1. A minotaur isn't scary. It is easy to escape from.") #roomE
        print("2. I wish I could start over.")#roomZ
        print("3. Be couragous and attack your captor.")#roomI
        validC4=False
        while(validC4!=True):
            choice4=str(input("Enter your choice: "))
            if(choice4=="1" or choice4=="2" or choice4=="3"):
                validC4=True
        if(choice4=="1"):
            self.dia="E"
        elif(choice4=="2"):
            print("[You feel a sharp pain in the back of your head and black out.]")
            self.dia="Z"
        elif(choice4=="3"):
            self.dia="I"
        else:
            print("Error invalid choice")
            self.dia="Y"
        self.tE=self.tE+1

    def dialogRoomH(self): #choice2=3 or choice3=2
        print("Hmm... [Your Captor seems lathargic.]")
        print("[What shall you do?]")
        print("1. Try to assult your captor.") #roomI
        print("2. Try to run away.") #to Zorc
        validC5=False
        while(validC5!=True):
            choice5=str(input("Enter your choice: "))
            if(choice5=="1" or choice5=="2"):
                validC5=True
        if(choice5=="1"):
            self.dia="I"
        elif(choice5=="2"):
            print("Bad choice! Just try and escape Zorc!")
            print("[The floor underneath you disapears.]")
            print("[You see a path to right.]")
            print("[You walk right and find yourself in a maze.]")
            #transition to Zorc
            self.setNextGame("Zorc")
            self.interacting=False
            #for hyperclass for combined game...
        else:
            print("Error invalid choice")
            self.dia="Y"
        self.tE=self.tE+1

    def dialogRoomI(self): #choice4=3 or choice5=1
        print("[You attack your captor. But he defends himself.]")
        print("Oh! That was couragous of you! But a bad choice.")
        print("Hmm... It might have been worth it to see Zorc attack you.")
        print("However trying to attack me crossed a line!")
        print("[You feel a sharp pain in the back of your head and black out.]")
        self.dia="Z"

    def dialogRoomR(self): #exited via the entrance of the Zorc Room
        #print("[You exited the maze where you entered it.]")
        print("[You realize there is nothing in this direction.]")
        print("[You turn back around and reenter the maze, but all your mapping has been lost!]")
        #transition to Zorc
        self.setNextGame("Zorc")
        self.interacting=False
        #for hyperclass for combined game

    def dialogRoomS(self): #you escaped Zorc
        print("[You enter a new room. A hologram of your captor apears.]")
        print("Congrats! I didn't think you could escape.")
        print("I will let you go now. You won!")
        if(self.tE>=4):
            print("Just so you know: You where very into this game and made a lot of decisions.")
        elif(self.tE==3):
            print("Just so you know: You made several decisions during this game.")
        elif(self.tE==2):
            print("Just so you know: there was more dialog you could have experienced.")
        else: #self.tE<=1
            print("Just so you know: you experienced the bare minimum of this game.")
        #transition to game end
        self.setNextGame("None")
        self.interacting=False
        #for hyperclass for combined game

    def dialogRoomT(self): #tie card war
        print("Since a tie occured, lets play again")
        self.setNextGame("CardWar")
        self.interacting=False

    def dialogRoomY(self):
        print("You could have only entered here via an error. Reseting the game.")
        self.dia="A"

    def dialogRoomZ(self): #got caught by Zorc or choice4=2 or from RoomI
        print("[After blacking out, you wake up in a jail cell.]")
        print("[Your captor stands in front of you cell with an evil grin.]")
        print("Mwahaha! You couldn't escape! Too bad! It is game over for you!")
        print("[You black out once more.]")
        print("[When you next wake up, you find yourself in a familiar room.]")
        self.dia="A"
        #you lost, thus you return to the begining of the game

    def interactions(self):
        while(self.interacting==True):
            if(self.dia=="A"):
                self.dialogRoomA()
            elif(self.dia=="B"):
                self.dialogRoomB()
            elif(self.dia=="C"):
                self.dialogRoomC()
            elif(self.dia=="D"):
                self.dialogRoomD()
            elif(self.dia=="E"):
                self.dialogRoomE()
            elif(self.dia=="F"):
                self.dialogRoomF()
            elif(self.dia=="G"):
                self.dialogRoomG()
            elif(self.dia=="H"):
                self.dialogRoomH()
            elif(self.dia=="I"):
                self.dialogRoomI()
            elif(self.dia=="R"):
                self.dialogRoomR()
            elif(self.dia=="S"):
                self.dialogRoomS()
            elif(self.dia=="T"):
                self.dialogRoomT()
            elif(self.dia=="Y"):
                self.dialogRoomY()
            elif(self.dia=="Z"):
                self.dialogRoomZ()
            else:
                self.interacting=False

#CardWar
class card:
    def __init__(self,color,rank):
        self.color = color #B or R
        self.rank = rank #A, 2-10, J, Q, K

    def __str__(self):
        return f"{self.rank} of {self.color}"

    def toStr(self):
        return f"{self.rank} of {self.color}"

    def getValue(self):
        if(self.rank == 'A'):
            return 1
        elif(self.rank == 'J'):
            return 11
        elif(self.rank == 'Q'):
            return 12
        elif(self.rank == 'K'):
            return 13
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = [card(color,rank) for rank in ranks for color in colors]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class PlayerC:
    def __init__(self,name):
        self.name=name
        self.pdeck = []
        self.active = []
        self.discard = []

    def setName(self,newName):
        self.name=newName

    def toActive(self):
        temp = self.pdeck.pop(0)
        self.active.append(temp)

    def checkActive(self):
        return str(self.active[len(self.active)-1])

    def printActive(self):
        astr = f"{self.name}: "
        for item in range(len(self.active)):
            astr = astr + self.active[item].toStr()
            if(item != len(self.active)-1):
                astr = astr + ", "
        return print(astr)

    def clearActive(self):
        self.active.clear()

    def resetDeck(self):
        while(len(self.discard)>0):
            temp=self.discard.pop()
            self.pdeck.append(temp)
        #self.discard.clear()

    def activeToDiscard(self):
        while(len(self.active)>0):
            temp = self.active.pop()
            self.discard.append(temp)

class WarGame:
    def __init__(self,player1,player2):
        self.deck = Deck()
        self.p1 = PlayerC(player1)
        self.p2 = PlayerC(player2)
        self.setup_game()
        self.turncount=1
        self.winner=""

    def setup_game(self):
        while self.deck.cards:
            self.p1.pdeck.append(self.deck.draw())
            self.p2.pdeck.append(self.deck.draw())

    def playRound(self):
        self.p1.toActive()
        self.p2.toActive()
        self.checkTie()
        #print player 1's active cards
        self.p1.printActive()
        #print player 2's active cards
        self.p2.printActive()
        self.compare()
        if(len(self.p1.pdeck)==0):
            self.p1.resetDeck()
        if(len(self.p2.pdeck)==0):
            self.p2.resetDeck()
        self.turncount=self.turncount+1
        print(f"{self.p1.name}: Cards in deck: {len(self.p1.pdeck)}, Cards in Discard: {len(self.p1.discard)}")
        print(f"{self.p2.name}: Cards in deck: {len(self.p2.pdeck)}, Cards in Discard: {len(self.p2.discard)}")

    def checkTie(self):
        while(self.p1.active[len(self.p1.active)-1].getValue()==self.p2.active[len(self.p2.active)-1].getValue()):
            #print player 1's active cards
            self.p1.printActive()
            #print player 2's active cards
            self.p2.printActive()
            print("Due to a tie and additional card is played")
            self.p1.toActive()
            self.p2.toActive()
            if(len(self.p1.pdeck)==0):
                self.p1.resetDeck()
            if(len(self.p2.pdeck)==0):
                self.p2.resetDeck()

    def compare(self):
        card1=self.p1.checkActive()
        card2=self.p2.checkActive()
        c1=self.p1.active[len(self.p1.active)-1].getValue()
        c2=self.p2.active[len(self.p2.active)-1].getValue()
        if(c1==1 & c2>10): #A vs royal
            self.p1.activeToDiscard()
            self.p2Atop1D()
            print(f"{self.p1.name} wins this round")
        elif(c2==1 & c1>10): #royal vs A
            self.p2.activeToDiscard()
            self.p1Atop2D()
            print(f"{self.p2.name} wins this round")
        elif(c1>c2):
            self.p1.activeToDiscard()
            self.p2Atop1D()
            print(f"{self.p1.name} wins this round")
        elif(c2>c1):
            self.p2.activeToDiscard()
            self.p1Atop2D()
            print(f"{self.p2.name} wins this round")

    def p2Atop1D(self):
        while(len(self.p2.active)>0):
            temp = self.p2.active.pop()
            self.p1.discard.append(temp)

    def p1Atop2D(self):
        while(len(self.p1.active)>0):
            temp = self.p1.active.pop()
            self.p2.discard.append(temp)

    def playGame(self):
        self.turncount=1
        while self.turncount<52:
            if(len(self.p1.pdeck)==0 & len(self.p1.discard)==0):
                #if p1 runs out of cards
                break
            if(len(self.p2.pdeck)==0 & len(self.p2.discard)==0):
                #if p2 runs out of cards
                break
            print(f"Round: {self.turncount}")
            self.playRound()
        if(len(self.p1.pdeck)+len(self.p1.discard) == len(self.p2.pdeck) + len(self.p2.discard)):
            print("Tie Game")
            self.winner="Tie"
        elif(len(self.p1.pdeck)+len(self.p1.discard) > len(self.p2.pdeck) + len(self.p2.discard)):
            print(f"{self.p1.name} wins")
            self.winner=self.p1.name
        elif(len(self.p1.pdeck)+len(self.p1.discard) < len(self.p2.pdeck) + len(self.p2.discard)):
            print(f"{self.p2.name} wins")
            self.winner=self.p2.name

#Zorc
class Map:
    def __init__(self,fullMap,curMap):
        self.fullmap = fullMap
        self.curMap = curMap

    def resetMap(self):
        self.curMap=[["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["?","?","?","?","?","?"],
          ["╩","?","?","?","?","?"]]

    def genFmap(self):
        for row in range(5):
            mapRow=""
            for col in range(6):
                mapRow=mapRow+self.fullmap[row][col]
            print(mapRow)
        #add code to change color of exit to red and entrance to green
        #and everything else to black

class Room:
    def __init__(self,rowNum,colNum):
        self.rowNum = rowNum #row number
        self.colNum = colNum #column number
        self.tile = fullMap[rowNum][colNum]
        self.doors = self.populateDoors()
        #self.occupied = occupier #0 for none, 1 for player, 2 for zork
        #self.special = special #if room has a function like map expansion add in later

    def populateDoors(self):
        doorList=[]
        if(self.tile=="╬"):
            doorList=["U","L","R","D"]
        elif(self.tile=="╠"):
            doorList=["U","R","D"]
        elif(self.tile=="╣"):
            doorList=["U","L","D"]
        elif(self.tile=="╦"):
            doorList=["L","R","D"]
        elif(self.tile=="╩"):
            doorList=["U","L","R"]
        elif(self.tile=="║"):
            doorList=["U","D"]
        elif(self.tile=="═"):
            doorList=["L","R"]
        elif(self.tile=="╝"):
            doorList=["U","L"]
        elif(self.tile=="╚"):
            doorList=["U","R"]
        elif(self.tile=="╗"):
            doorList=["L","D"]
        elif(self.tile=="╔"):
            doorList=["R","D"]
        elif(self.tile=="╨"):
            doorList=["U"]
        elif(self.tile=="╥"):
            doorList=["D"]
        elif(self.tile=="╡"):
            doorList=["L"]
        elif(self.tile=="╞"):
            doorList=["R"]
        return doorList

class PlayerZ:
    def __init__(self,rowNum,colNum):
        self.rowNum = rowNum
        self.colNum = colNum
        self.pRow = rowNum #previous occupied row
        self.pCol = colNum #previous occupied col
        
class Zorc:
    def __init__(self,rowNum,colNum):
        self.rowNum = rowNum
        self.colNum = colNum
        self.pRow = rowNum #previous occupied row
        self.pCol = colNum #previous occupied col

class ZorcGame:
    def __init__(self,playerR,playerC,zorcR,zorcC):
        self.player = PlayerZ(playerR,playerC) #starting space
        self.zorc = Zorc(zorcR,zorcC) #zorc start space
        self.map = Map(fullMap,curMap) #adds fullmap and curmap
        self.pRoom = Room(playerR,playerC)
        self.zRoom = Room(zorcR,zorcC)
        self.gameState = '0'

    def getGameState(self):
        return self.gameState

    def updateProom(self):
        self.pRoom = Room(self.player.rowNum,self.player.colNum)

    def updateZroom(self):
        self.zRoom = Room(self.zorc.rowNum,self.zorc.colNum)

    def checkPdoors(self):
        doorlist="Your moves are: "
        for item in range(len(self.pRoom.doors)):
            doorlist=doorlist+self.pRoom.doors[item]
            if(item<len(self.pRoom.doors)-1):
                doorlist=doorlist+", "
        print(doorlist)

    def movePlayer(self):
        pMoves = self.pRoom.doors
        self.checkPdoors() #tells player available moves
        validMove = False
        while(validMove!=True):
            pDir = str(input("Enter a valid direction: "))
            for item in range(len(pMoves)):
                if(str(pMoves[item])==pDir):
                    validMove=True
                    break
        self.player.pRow=self.player.rowNum
        self.player.pCol=self.player.colNum
        if(pDir=="U"):
            self.player.rowNum=self.player.rowNum-1
        elif(pDir=="D"):
            self.player.rowNum=self.player.rowNum+1
        elif(pDir=="L"):
            self.player.colNum=self.player.colNum-1
        elif(pDir=="R"):
            self.player.colNum=self.player.colNum+1
        if(self.player.colNum<0): #for the fullMap
            if(self.player.rowNum!=4):
                print("Error: walked off map through a wall!")
            else:
                print("You exited via the start space.")
                self.gameState='-1'
                #fix error of looping over the map here
        if(self.player.colNum>5):
            print("Error: walked off map through a wall!")
        if(self.player.rowNum<0):
            if(self.player.colNum!=5):
                print("Error: walked off map through a wall!")
            else:
                print("You exited via the exit space. You Win!")
                self.gameState='1'
        if(self.player.rowNum>4):
            print("Error: walked off map through a wall!")

    def playerDirection(self): #reference for the moveZorc() function
        if(self.player.rowNum - self.player.pRow == -1):
            return "U"
        if(self.player.rowNum - self.player.pRow == 1):
            return "D"
        if(self.player.colNum - self.player.pCol == -1):
            return "L"
        if(self.player.colNum - self.player.pCol == 1):
            return "R"

    def moveZorc(self):
        zMoves = self.zRoom.doors
        validMove = False
        if(len(zMoves)>1):
            while(validMove!=True):
                tempMove=random.choice(zMoves)
                if(tempMove!=self.playerDirection()):
                    zDir=tempMove
                    validMove=True
        else:
            zDir=zMoves[0]
        self.zorc.pRow=self.zorc.rowNum
        self.zorc.pCol=self.zorc.colNum
        if(zDir=="U"):
            self.zorc.rowNum=self.zorc.rowNum-1
        elif(zDir=="D"):
            self.zorc.rowNum=self.zorc.rowNum+1
        elif(zDir=="L"):
            self.zorc.colNum=self.zorc.colNum-1
        elif(zDir=="R"):
            self.zorc.colNum=self.zorc.colNum+1
        
    def encounter(self):
        if(int(self.player.rowNum)==int(self.zorc.rowNum) and int(self.player.colNum)==int(self.zorc.colNum)):
            self.gameState='2'
            print("You encountered Zorc! Game over!") #you and Zorc enter the same space
        elif(int(self.player.rowNum)==int(self.zorc.pRow) and int(self.player.colNum)==int(self.zorc.pCol)
           and int(self.player.pRow)==int(self.zorc.rowNum) and int(self.player.pCol)==int(self.zorc.colNum)):
            self.gameState='2'
            print("You ran into Zorc! Game over!") #you swapped spaces with Zorc
        else:
            self.gameState='0' #unchanged

    def genCmap(self):
        for row in range(5):
            mapRow=""
            for col in range(6):
                mapRow=mapRow+self.map.curMap[row][col]
                #if(self.player.rowNum==row and self.player.colNum == col):
                    #change color of that space
            print(mapRow)
        plocation = "Your location is row " + str(self.player.rowNum) + " col " + str(self.player.colNum)
        zlocation = "Zorc is at row " + str(self.zorc.rowNum) + " col " + str(self.zorc.colNum)
        print(plocation)
        print(zlocation)
        #add code so that the entrance space when unoccupied is green
        #add code so that the exit space when unoccpied is red
        #add code so that the occupied space is blue
        #add code so that the space Zorc is on is purple
        #add code so that any remaining spaces are black

    def updateMap(self): #updates curmap when a player enters a new room
        if(self.map.curMap[self.player.rowNum][self.player.colNum]=="?"):
            self.map.curMap[self.player.rowNum][self.player.colNum]=self.map.fullmap[self.player.rowNum][self.player.colNum]

    def playGame(self):
        #self.map.genFmap()
        self.map.resetMap()
        while(self.gameState=='0'):
            self.genCmap()
            self.checkPdoors()
            self.movePlayer()
            if(self.gameState!='0'):
                break
            if(self.player.colNum<0):
                self.gameState='-1'
                break
            self.updateProom()
            self.updateMap()
            self.moveZorc()
            self.updateZroom()
            self.encounter()
        if(self.gameState=='1'):
            print("You Escaped!!!")
            #switch to next game code!!!
        elif(self.gameState=='2'):
            print("Zorc caught you! Game Over!")
            #ask if player wants to try again
            #if yes, reset the game
        elif(self.gameState=='-1'):
            #print("You took the cowards way out through the entrance. Resetting.")
            print("In the distance you hear Zorc grunt as if mocking you.")
            self.map.curMap=baseMap
            #reset the game

#Hyperclass
class HyperClass:
    def __init__(self):
        self.chat=InteractionV1("A")
        self.minotaur=ZorcGame(4,0,2,4)
        self.cardWar=WarGame("Temp","Computer")
        self.run=True

    def updateCWname(self):
        if(self.chat.playerName!="Temp"):
            self.cardWar.p1.setName(self.chat.getPlayerName())

    def CardToChatTransition(self):
        if(self.cardWar.winner=="Tie"):
            self.chat.setDia("T")
            self.chat.interT()
            self.chat.setNextGame("Chat")
            self.chat.interactions()
            self.cardWar=WarGame(self.chat.getPlayerName(),"Computer")
            self.cardWar.playGame()
        elif(self.cardWar.winner=="Computer"):
            self.chat.setDia("B")
            self.chat.interT()
            self.chat.setNextGame("Chat")
            self.chat.interactions()
        elif(self.cardWar.winner==self.chat.getPlayerName() or self.cardWar.winner=="Temp"):
            self.chat.setDia("C")
            self.chat.interT()
            self.chat.setNextGame("Chat")
            self.chat.interactions()
        
    def ZorcToChatTranition(self):
        if(self.minotaur.getGameState()=='-1'):
            self.chat.setDia("R")
            self.chat.interT()
            self.chat.setNextGame("Chat")
            self.chat.interactions()
        elif(self.minotaur.getGameState()=='2'):
            self.chat.setDia("Z")
            self.chat.interT()
            self.chat.setNextGame("Chat")
            self.chat.interactions()
        elif(self.minotaur.getGameState()=='1'):
            self.chat.setDia("S")
            self.chat.interT()
            self.chat.setNextGame("None")
            self.chat.interactions()
            self.run=False

    def ChatToOthers(self):
        if(self.chat.interacting==False):
            if(self.chat.getNextGame()=="CardWar"):
                #code to reset aspects of cardwar
                self.cardWar.playGame()
                self.CardToChatTransition()
            elif(self.chat.getNextGame()=="Zorc"):
                self.minotaur=ZorcGame(4,0,2,4)
                self.minotaur.map.resetMap()
                self.minotaur.playGame()
                self.ZorcToChatTranition()
            elif(self.chat.getNextGame()=="None"):
                self.run=False
                print("End of Game.")
            elif(self.chat.getNextGame()=="Chat"):
                print("Error?")
                
    def Process(self):
        while(self.run==True):
            self.chat.interactions() #while self.chat.interacting=True
            self.updateCWname() #if a name other than temp is used from RoomA, the card war will be updated
            self.ChatToOthers() #if self.chat.interacting=False

if __name__ == "__main__":
    hyper = HyperClass()
    hyper.Process()

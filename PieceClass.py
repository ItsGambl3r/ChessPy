class Piece:
    def __init__(self, color, type, xCordinate, yCordinate):
        self.color = color
        self.type = type
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
    
    def getPostion(self):
        return self.xCordinate, self.yCordinate

    def setPostion(self, xCordinate, yCordinate):
        self.xCordinate = xCordinate
        self.yordinate = yCordinate
        Board[xCordinate][yCordinate] = self

class Pawn(Piece):
    def __init__self(desiredX, desiredY):
        pass

    def __str__(self):
        return "%s pawn at (%d, %d)" % (self.color,
         self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self


class Knight(Piece):
    def __init__self(self, color, xCordinate, yCordinate):
        pass

    def __str__(self):
        return "%s Knight at (%d, %d)" % (self.color,
         self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self

class Bishop(Piece):
    def __init__self(self, color, xCordinate, yCordinate):
        pass

    def __str__(self):
        return "%s Bishop at (%d, %d)" % (self.color,
         self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self

class Rook(Piece):
    def __init__self(self, color, xCordinate, yCordinate):
        pass

    def __str__(self):
        return "%s Rook at (%d, %d)" % (self.color,
         self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self

class Queen(Piece):
    def __init__self(self, color, xCordinate, yCordinate):
        self.color = color
        self.type = type
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate

    def __str__(self):
        return "%s Queen at (%d, %d)" % (self.color,
        self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self 

class King(Piece):
    def __init__self(self, color, xCordinate, yCordinate):
        pass

    def __str__(self):
        return "%s King at (%d, %d)" % (self.color,
         self.xCordinate, self.yCordinate)
    
    def __repr__(self) -> str:
        return self.type

    def checkAvaibleMoves():
        pass

    def move(self, desiredX, desiredY):
        self.xCordinate = desiredX
        self.yCordinate = desiredY
        Board[self.xCordinate][self.yCordinate] = self

Board = []

def createBoard():
    for row in range(8):
        Board.append([])
        for column in range(8):
            Board[row].append("o") ## "o" stands for avaible

def setPieces():
    black_pawns = [] ## List of black pawns
    white_pawns = [] ## List of white pawns
    black_rooks = [] ## List of black rooks
    white_rooks = [] ## List of white rooks
    black_knights = [] ## List of black knights
    white_knights = [] ## List of white knights
    black_bishops = [] ## List of black bishops 
    white_bishops = [] ## List of white bishops
    black_queen = [] ## List of black queen
    white_queen = [] ## List of white queen
    black_king = [] ## List of black king
    white_king = [] ## List of white king

    #Wow wtf is this Im so freakin bad at this

    # Set pawns
    for i in range(8):
        Board[1][i] = Pawn("Black", "Pawn", 1, i)
        black_pawns.append(Pawn)
      
    for i in range(8):
        Board[6][i] = Pawn("White", "Pawn", 6, i)
        white_pawns.append(Pawn)

    # Set rooks
    Board[0][0] = Rook("White", "Rook", 0, 0)
    white_rooks.append(Rook)
    Board[0][7] = Rook("White", "Rook", 0, 7)
    white_rooks.append(Rook)

    Board[7][0] = Rook("Black", "Rook", 7, 0)
    black_rooks.append(Rook)
    Board[7][7] = Rook("Black", "Rook", 7, 7)
    black_rooks.append(Rook)

    # Set knights
    Board[0][1] = Knight("White", "Knight", 0, 1)
    white_knights.append(Knight)
    Board[0][6] = Knight("White", "Knight", 0, 6)
    white_knights.append(Knight)

    Board[7][1] = Knight("Black", "Knight", 7, 1)
    black_knights.append(Knight)
    Board[7][6] = Knight("Black", "Knight", 7, 6)
    black_knights.append(Knight)

    # Set bishops
    Board[0][2] = Bishop("White", "Bishop", 0, 2)
    white_bishops.append(Bishop)
    Board[0][5] = Bishop("White", "Bishop", 0, 5)
    white_bishops.append(Bishop)
    Board[7][2] = Bishop("Black", "Bishop", 7, 2)
    black_bishops.append(Bishop)
    Board[7][5] = Bishop("Black", "Bishop", 7, 5)
    black_bishops.append(Bishop)

    # Set queens
    Board[0][3] = Queen("White", "Queen", 0, 3)
    white_queen.append(Queen)
    Board[7][3] = Queen("Black", "Queen", 7, 3)
    black_queen.append(Queen)

    # Set kings
    Board[0][4] = King("White", "King", 0, 4)
    white_king.append(King)
    Board[7][4] = King("Black", "King", 7, 4)
    black_king.append(King)

def printBoard():
    for row in Board:
        print(row)
    
def surrender():
    gameIsActive = False 

def replacePreviousPosition(xCordinate,yCordinate):
    Board[xCordinate][yCordinate] = "o" 

def updateBoard():
    currentX = int(input("CurrentX: "))
    currentY = int(input("CurrentY: "))

    newX = int(input("\nnewX: "))
    newY = int(input("newY: "))

    Board[currentX][currentY].move(newX, newY)
    replacePreviousPosition(currentX,currentY)
    printBoard()

createBoard()
setPieces()

gameIsActive = True 

while gameIsActive:
    updateBoard()
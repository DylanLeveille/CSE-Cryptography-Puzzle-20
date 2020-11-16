class HexCube:
    """Class to create a HexCube (i.e. a rubik cube where each square has a label)"""
    
    num_squares = 54 #the number of squares a rubix cube should have
    valid_moves = ["F", "F2", "F'", "R", "R2", "R'", "U", "U2", "U'", "B", "B2", "B'", "L", "L2", "L'", "D", "D2", "D'"] #valid moves on the cube
    valid_colours = ["O", "G", "Y", "W", "R", "B"] #valid colours for each square
     
    """
    Constructor to create the HexCube.
    
    Args:
         specs: list of 54 tuples. The item at the first index of each tuple is a colour represented as a string ("O", "G", "Y", "W", "R", "B"), the second index contains the label for that square (can be of any type). Default value is a regular rubik cube with blank labels.
    
    """ 
    def __init__(self, specs = [("O", 1),("O", 2),("O", 3),("O", 4),("O", 5),("O", 6),("O", 7),("O", 8),("O", 9),("G", 10),("G", 11),("G", 12),("G", 13),("G", 14),("G", 15),("G", 16),("G", 17),("G", 18),("Y", 19),("Y", 20),("Y", 21),("Y", 22),("Y", 23),("Y", 24),("Y", 25),("Y", 26),("Y", 27),("W", 28),("W", 29),("W", 30),("W", 31),("W", 32),("W", 33),("W", 34),("W", 35),("W", 36),("R", 37),("R", 38),("R", 39),("R", 40),("R", 41),("R", 42),("R", 43),("R", 44),("R", 45),("B", 46),("B", 47),("B", 48),("B", 49),("B", 50),("B", 51),("B", 52),("B", 53),("B", 54)]):
        if len(specs) != HexCube.num_squares:
            raise ValueError('HexCube must have exactly ' + str(HexCube.num_squares) +' squares. You have ' + str(len(specs)) + " squares.")
        
        #create sides of HexCube
        self.TopSide = [[], [], []]
        self.LeftSide = [[], [], []]
        self.CenterSide = [[], [], []]
        self.RightSide = [[], [], []]
        self.BottomSide = [[], [], []]
        self.TailEndSide = [[], [], []]       
        
        for i in range(HexCube.num_squares):
            #check validity of type (must be tuple for each item in specs)
            if type(specs[i]) is not tuple:
                raise ValueError('item at index ' + str(i) + " must be a tuple.")
            
            #check validity of entered square (must be a valid colour)
            if specs[i][0] not in HexCube.valid_colours:
                raise ValueError('item at index ' + str(i) + " is not a valid colour or is not uppercased")                  
            
            #create the sides of the HexCube based on the provided specs (colours and labels)
            if i in range(0, 9):
                self.TopSide[i // 3].append(specs[i])
                
            elif i in range(9, 18):
                self.LeftSide[i // 3 - 3].append(specs[i]) 
                
            elif i in range(18, 27):
                self.CenterSide[i // 3 - 6].append(specs[i])            
                
            elif i in range(27, 36):
                self.RightSide[i // 3 - 9].append(specs[i])
                
            elif i in range(36, 45):
                self.BottomSide[i // 3 - 12].append(specs[i])         
        
            else:
                self.TailEndSide[i // 3 - 15].append(specs[i])
           
      
    """
    Print cube based on either the colour or labels. Will print in '2D cube' format
    
    Args:
         val: an integer of either 0 or 1. 0 will print the cube's colours, 1 will print the labels.
    
    """         
    def printCubeValues(self, val):
        if val not in range(0, 2):
            raise ValueError("parameter for printed value must be 0 or 1.")
        
        result = ''
        numRows = 12
        for i in range(numRows): #rubik cube has 12 rows when printed flat, therefore, iterate through 12 rows
            if i in range(0, 3):
                result += " " * 11
                result += (str(self.TopSide[i % 3][0][val]) + " " + str(self.TopSide[i % 3][1][val]) + " " + str(self.TopSide[i % 3][2][val]))
                result += "\n"
                
            elif i in range(3, 6): #in rows 3 to 5, three sides of the cube are present
                result += (str(self.LeftSide[i % 3][0][val]) + " " + str(self.LeftSide[i % 3][1][val]) + " " + str(self.LeftSide[i % 3][2][val]))
                result += " " * 3
                result += (str(self.CenterSide[i % 3][0][val]) + " " + str(self.CenterSide[i % 3][1][val]) + " " + str(self.CenterSide[i % 3][2][val]))
                result += " " * 3
                result += (str(self.RightSide[i % 3][0][val]) + " " + str(self.RightSide[i % 3][1][val]) + " " + str(self.RightSide[i % 3][2][val]))
                result += "\n"                
                
            elif i in range(6, 9):
                result += " " * 11
                result += (str(self.BottomSide[i % 3][0][val]) + " " + str(self.BottomSide[i % 3][1][val]) + " " + str(self.BottomSide[i % 3][2][val]))
                result += "\n"                    
        
            else:
                result += " " * 11
                result += (str(self.TailEndSide[i % 3][0][val]) + " " + str(self.TailEndSide[i % 3][1][val]) + " " + str(self.TailEndSide[i % 3][2][val]))
                result += "\n" 
                
        print(result)
     
    """
    Print cube based on the colour.
    
    Args:
         NONE
    
    """     
    def printCube(self):
        self.printCubeValues(0)     
        
    """
    Print cube based on the labels.
    
    Args:
         NONE
    
    """            
    def printCubeLabels(self):
        self.printCubeValues(1)
    
    """
    Make an F move. 
    
    Args:
         units: number of F-moves made
    
    """           
    def moveF(self, units):
        while(units > 0):
            temp = self.TopSide[2]
            temp2 = self.BottomSide[0]
            
            self.TopSide[2] = [self.LeftSide[2][2], self.LeftSide[1][2], self.LeftSide[0][2]]
            
            self.BottomSide[0] = [self.RightSide[2][0], self.RightSide[1][0], self.RightSide[0][0]]           
                   
            self.RightSide[0][0] = temp[0]
            self.RightSide[1][0] = temp[1]
            self.RightSide[2][0] = temp[2]
            
            self.LeftSide[0][2] = temp2[0]
            self.LeftSide[1][2] = temp2[1]
            self.LeftSide[2][2] = temp2[2]      
            
            self.rotateSide(self.CenterSide)
             
            units -= 1
        
    def moveR(self, units):
        while(units > 0):
            temp = self.CenterSide[2]
            temp2 = self.TailEndSide[0]
            
            self.CenterSide[2] = self.LeftSide[2]
            
            self.TailEndSide[0] = self.RightSide[2][::-1]       
                   
            self.RightSide[2] = temp
         
            self.LeftSide[2] = temp2[::-1]        
            
            self.rotateSide(self.BottomSide)
             
            units -= 1  
            
    def moveU(self, units):
        while(units > 0):
            temp = [self.TopSide[0][2], self.TopSide[1][2], self.TopSide[2][2]]
            temp2 = [self.BottomSide[0][2], self.BottomSide[1][2], self.BottomSide[2][2]]
            
            self.TopSide[0][2] = self.CenterSide[0][2]
            self.TopSide[1][2] = self.CenterSide[1][2]
            self.TopSide[2][2] = self.CenterSide[2][2]
            
            self.BottomSide[0][2] = self.TailEndSide[0][2]  
            self.BottomSide[1][2] = self.TailEndSide[1][2]   
            self.BottomSide[2][2] = self.TailEndSide[2][2]   
            
            self.TailEndSide[0][2] = temp[0]
            self.TailEndSide[1][2] = temp[1]
            self.TailEndSide[2][2] = temp[2]             
                   
            self.CenterSide[0][2] = temp2[0]
            self.CenterSide[1][2] = temp2[1]
            self.CenterSide[2][2] = temp2[2]        
            
            self.rotateSide(self.RightSide)
             
            units -= 1    
            
    def moveB(self, units):
        while(units > 0):
            temp = self.TopSide[0]
            temp2 = self.BottomSide[2]
            
            self.TopSide[0] = [self.RightSide[0][2], self.RightSide[1][2], self.RightSide[2][2]]
            
            self.BottomSide[2] = [self.LeftSide[0][0], self.LeftSide[1][0], self.LeftSide[2][0]]  
            
            self.LeftSide[0][0] = temp[2]
            self.LeftSide[1][0] = temp[1]
            self.LeftSide[2][0] = temp[0]             
                   
            self.RightSide[0][2] = temp2[2]
            self.RightSide[1][2] = temp2[1]
            self.RightSide[2][2] = temp2[0]    
            
            self.rotateSide(self.TailEndSide)
             
            units -= 1    
            
    def moveL(self, units):
        while(units > 0):
            temp = self.LeftSide[0]
            temp2 = self.RightSide[0]
            
            self.LeftSide[0] = self.CenterSide[0]
            
            self.RightSide[0] = self.TailEndSide[2][::-1]
            
            self.TailEndSide[2] = temp[::-1]  
            
            self.CenterSide[0] = temp2    
            
            self.rotateSide(self.TopSide)
             
            units -= 1    
            
    def moveD(self, units):
        while(units > 0):
            temp = [self.CenterSide[0][0], self.CenterSide[1][0], self.CenterSide[2][0]]
            temp2 = [self.TailEndSide[0][0], self.TailEndSide[1][0], self.TailEndSide[2][0]]
            
            self.CenterSide[0][0] = self.TopSide[0][0]
            self.CenterSide[1][0] = self.TopSide[1][0]
            self.CenterSide[2][0] = self.TopSide[2][0]
            
            self.TailEndSide[0][0] = self.BottomSide[0][0]
            self.TailEndSide[1][0] = self.BottomSide[1][0]
            self.TailEndSide[2][0] = self.BottomSide[2][0]    
            
            self.BottomSide[0][0] = temp[0]
            self.BottomSide[1][0] = temp[1]
            self.BottomSide[2][0] = temp[2]            
            
            self.TopSide[0][0] = temp2[0]
            self.TopSide[1][0] = temp2[1]
            self.TopSide[2][0] = temp2[2]
            
            self.rotateSide(self.LeftSide)
             
            units -= 1    
    
    def rotateSide(self, side):
        temp = [side[0][2], side[1][2], side[2][2]]
        side[2][2] = side[0][2]
        side[1][2] = side[0][1]
        side[0][2] = side[0][0]       
        
        side[0][1] = side[1][0]
        side[0][0] = side[2][0]
        side[1][0] = side[2][1]
        
        side[2][1] = temp[1]
        side[2][0] = temp[2]
        
            
    def makeMove(self, move):
        if move not in HexCube.valid_moves: #check if move is valid
            raise ValueError("move : " + str(move) + " is not a valid move.")
     
        if move.startswith("F"):           
            self.moveF((HexCube.valid_moves.index(move) % 3) + 1)
        elif move.startswith("R"):
            self.moveR((HexCube.valid_moves.index(move) % 3) + 1)
        elif move.startswith("U"):
            self.moveU((HexCube.valid_moves.index(move) % 3) + 1) 
        elif move.startswith("B"):
            self.moveB((HexCube.valid_moves.index(move) % 3) + 1) 
        elif move.startswith("L"):
            self.moveL((HexCube.valid_moves.index(move) % 3) + 1)     
        else:
            self.moveD((HexCube.valid_moves.index(move) % 3) + 1) 
       
if __name__ == "__main__":
    givenSpecs = [("O", "22"),("R", "5b"),("G", "61"),("O", "50"),("O", "76"),("B", "6d"),("B", "77"),("G", "2a"),("O", "63"),
("G", "2a"),("B", "6d"),("R", "74"),("W", "48"),("Y", "6d"),("G", "6f"),("Y", "7c"),("W", "7a"),("W", "3a"),
("Y", "70"),("W", "7c"),("W", "72"),("Y", "34"),("G", "77"),("O", "7a"),("B", "78"),("B", "78"),("R", "7e"),
("B", "76"),("Y", "76"),("R", "3f"),("Y", "6a"),("W", "78"),("R", "7e"),("Y", "6f"),("O", "6a"),("W", "3a"),
("R", "77"),("R", "61"),("G", "2b"),("B", "75"),("R", "77"),("G", "58"),("B", "6a"),("W", "76"),("O", "79"),
("O", "6a"),("O", "50"),("G", "66"),("R", "3f"),("B", "75"),("G", "68"),("Y", "6b"),("Y", "75"),("W", "73")]
    myHexCube = HexCube(givenSpecs)
    
    myHexCube.printCube()
    myHexCube.printCubeLabels()
    
    #20 moves for solution
    solution = ["R2", "U", "F'", "U", "B2", "R", "F'", "U'", "D2", "R'", "U", "L2", "U2", "D'", "B2", "R2", "U'", "R2", "F2", "R2"]
    
    for move in solution:
        myHexCube.makeMove(move)
        
    myHexCube.printCube()
    myHexCube.printCubeLabels()    
   
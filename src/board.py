from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0 for i in range(COLS)] for j in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col]= Square(row,col);

    def _add_pieces(self,color):
        row_pawn, row_other = (6,7) if color=='white' else (1,0)

        # All pawns 
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col, Pawn(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other,0,Rook(color))
        self.squares[row_other][7] = Square(row_other,7,Rook(color))

        # Knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other,6,Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))

        # Queen
        self.squares[row_other][3] = Square(row_other,3,Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other,4,King(color))
        self.squares[4][4] = Square(4,4,King('white'))
    
    def calc_moves(self, piece, row, col):
        '''calculate all the possible / valid moves of a specific piece on a specific place'''

        def straightLineMoves(incrs):
            for inc in incrs:
                row_inc, col_inc = inc
                row_curr, col_curr = row, col
                while True:
                    row_curr = row_curr+row_inc
                    col_curr = col_curr+col_inc
                    if(row_curr<8 and row_curr>=0 and col_curr<8 and col_curr>=0):
                        if(self.squares[row_curr][col_curr].isEmpty()):
                            initial = Square(row,col)
                            final = Square(row_curr,col_curr)
                            move = Move(initial, final)
                            piece.add_move(move)
                        elif(self.squares[row_curr][col_curr].hasRivalPiece(piece.color)):
                            initial = Square(row,col)
                            final = Square(row_curr,col_curr)
                            move = Move(initial, final)
                            piece.add_move(move)
                            break
                        else:
                            break
                    else:
                        break

        if isinstance(piece, Pawn):
            # cases for pawn move
            # 1 - it can go straight for 1 or 2 (depending on its first or second move) moves until there is some other piece of same color or different
            # 2 - if there is any piece of opposite color to its diagonally leftup and rightup then its possible to go there.
            steps = 1 if piece.moved else 2

            #vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1+steps))
            for move_row in range(start, end, piece.dir):
                if(move_row>=0 and move_row<8):
                    if(self.squares[move_row][col].isEmpty()):
                        initial = Square(row,col)
                        final = Square(move_row,col)
                        move = Move(initial,final)
                        piece.add_move(move)
                    else:
                        break
                else:
                    break
            
            #diagonal moves
            possibleMoves = [(row+piece.dir*1,col+1),(row+piece.dir*1,col-1)]
            for i in range(2):
                if(possibleMoves[i][0]<8 and possibleMoves[i][0]>=0 and possibleMoves[i][1]<8 and possibleMoves[i][1]>=0):
                    if(self.squares[possibleMoves[i][0]][possibleMoves[i][1]].hasRivalPiece(piece.color)):
                        initial = Square(row,col)
                        final = Square(possibleMoves[i][0],possibleMoves[i][1])
                        move = Move(initial,final)
                        piece.add_move(move)
            
        elif isinstance(piece, Knight):
            possibleMoves = [(row+2,col-1),(row+2,col+1),(row-2,col-1),(row-2,col+1),(row-1,col-2),(row+1,col-2),(row-1,col+2),(row+1,col+2)]
            for i in range(8):
                if(possibleMoves[i][0]<8 and possibleMoves[i][0]>=0 and possibleMoves[i][1]<8 and possibleMoves[i][1]>=0):
                    if self.squares[possibleMoves[i][0]][possibleMoves[i][1]].isEmptyOrRival(piece.color):
                        initial = Square(row,col)
                        final = Square(possibleMoves[i][0], possibleMoves[i][1])
                        #create new move
                        move = Move(initial, final)
                        #append new valid move
                        piece.add_move(move)

                    
        elif isinstance(piece, Bishop):
            straightLineMoves([(-1,1),(-1,-1),(1,1),(1,-1)])

        elif isinstance(piece, Rook):
            straightLineMoves([(-1,0),(0,1),(1,0),(0,-1)])

        elif isinstance(piece, King):
            possibleMoves = [(-1,1),(-1,-1),(1,1),(1,-1),(-1,0),(0,1),(1,0),(0,-1)]
            for possibleMove in possibleMoves:
                rowNew = row+possibleMove[0]
                colNew = col+possibleMove[1]
                if(rowNew<8 and row>=0 and colNew<8 and colNew>=0):
                    if(self.squares[rowNew][colNew].isEmptyOrRival(piece.color)):
                        initial = Square(row,col)
                        final = Square(rowNew,colNew)
                        move = Move(initial, final)
                        piece.add_move(move)

        elif isinstance(piece, Queen):
            straightLineMoves([(-1,1),(-1,-1),(1,1),(1,-1),(-1,0),(0,1),(1,0),(0,-1)])

# board = Board()
# board._create()
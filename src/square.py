class Square:

    def __init__(self,row,col,piece=None):
        self.row = row
        self.col = col
        self.piece = piece
    
    def has_piece(self):
        return self.piece!=None
    
    def isEmpty(self):
        return not self.has_piece()

    def isEmptyOrRival(self, color):
        return self.isEmpty() or self.piece.color != color

    def hasTeamPiece(self,color):
        return self.has_piece() and self.piece.color == color

    def hasRivalPiece(self, color):
        return self.has_piece() and self.piece.color != color

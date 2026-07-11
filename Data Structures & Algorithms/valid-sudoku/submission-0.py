from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #a hashmap for checking duplicates in the boxes,
        #key = tuple(coordinates) and value = set()
        box = defaultdict(set)

        for i in range(len(board)):
            row_set = set()
            col_set = set()
            for j in range(len(board)):
                #check for duplicate in the row
                if(board[i][j] in row_set and board[i][j] != "."):
                    return False
                row_set.add(board[i][j])
                
                #check for duplicates in the col
                if(board[j][i] in col_set and board[j][i] != "."):
                    return False
                col_set.add(board[j][i])

                #check if there are duplicates in the boxes
                #by converting the 9x9 box into 3x3 box
                coordinate = (i//3, j//3)
                #check for duplicates
                if(board[i][j] != "." and board[i][j] in box[coordinate]):
                    return False
                box[coordinate].add(board[i][j])

        return True
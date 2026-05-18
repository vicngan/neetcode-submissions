class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) 

        for r in range(9):
            for c in range(9): 
                if board[r][c] == ".":
                    continue 
                
                digit = board[r][c]
                if (digit in rows[r] or 
                    digit in cols[c] or 
                    digit in squares[(r//3, c//3)]):
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                squares[(r//3, c//3)].add(digit)

        return True 
                


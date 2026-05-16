'''
Solve by using a hashset to detect duplicates in rows, cols, and squares 

A brute force solution O(n^2) would be just to iterate through rows, cols, and squares one by one; skipping '.'; and add each digit to a seen set and if seen, return falls and if not, add in seen
A Onepass/ Hashset solution validate the entire board in one pass; check the digit if it alr appeared in the same row, same cols, or same 3x3 boxes 

1: create 3 hashmaps of sets using defaultdict(assign any empty value a key)
    - rows[r]
    - cols[c]
    - squares[r//3. c//3] ; track digits in each 3x3 boxes 
2: loop through every cell in the board; skip if it contains "." (empty) 
3: let val be the digit in the cell
4: if val already in row[r] or cols[c] or squares[r//3, c//3]; then return false 
5: if passed all conditions; add digit to all 3 sets 
6: if whole board wo duplicates, return True 

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]:
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True 

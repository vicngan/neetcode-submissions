class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) , len(matrix[0])

        '''
        each row in the matrix are sorted from L-> R increasing
        with each new row, the first element > last element of the last row and increase 
        (top row <= bottom row)

        1: divide the matrix in half (binary search), start from middle row
        2: if the target > last element of this row, top move down (row+1)
        3: if the target < first element of this row, bottom move up (row-1)
        4: otherwise, the target is in this row; break into 2nd binary search within the row 

        2nd binary search 
        1: divide the row into halves (left, right)
        2: if target is in the larget half left, switch ptr to the right 
        3: if target is in the lower half right, switch ptr to the left 
        4: otherwise, the target is the current ptr 

        '''

        #binary search through the matrix to find the row 
        top, bottom = 0, rows - 1
        while top <= bottom: 
            row = (top + bottom) // 2 
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row -1
            else:
                break 

        #binary search within the row 

        if not(top<=bottom):
            return False
        row = (top+bottom) // 2
        left, right = 0, cols -1 
        while left <= right:
            m = (left + right) //2 
            if target > matrix[row][m]:
                left = m + 1 
            elif target < matrix[row][m]:
                right = m -1 
            else: 
                return True
        return False

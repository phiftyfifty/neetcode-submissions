class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # think of each tile as a set 
        # think of each row, column as their own independent sets
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # iterate over each r,c
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == ".":
                    continue
                if board[x][y] in cols[y] or board[x][y] in rows[x] or board[x][y] in squares[(x//3,y//3)]:
                    return False
                cols[y].add(board[x][y])
                rows[x].add(board[x][y])
                squares[(x//3,y//3)].add(board[x][y])
        return True


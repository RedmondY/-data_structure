class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[] for _ in range(9)]
        block = [[] for _ in range(9)]

        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False

                    if board[i][j] not in col[j]:
                        col[j].append(board[i][j])
                    else:
                        return False

                    if board[i][j] not in block[i // 3 * 3 + j // 3]:
                        block[i // 3 * 3 + j // 3].append(board[i][j])
                    else:
                        return False
        return True

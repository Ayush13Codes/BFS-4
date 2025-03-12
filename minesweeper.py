class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # T: O(m * n), S: O(m * n)
        m, n = len(board), len(board[0])
        row, col = click

        # If we click on a mine
        if board[row][col] == "M":
            board[row][col] = "X"
            return board

        # Define the 8 adjacent directions
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # Helper function for DFS
        def dfs(r, c):
            # If out of bounds or not an unrevealed blank cell, stop
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "E":
                return

            # Count adjacent mines
            mine_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in ["M", "X"]:
                    mine_count += 1

            # If there are adjacent mines, mark with count
            if mine_count > 0:
                board[r][c] = str(mine_count)
            # If no adjacent mines, mark as 'B' and recursively check adjacent cells
            else:
                board[r][c] = "B"
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        # Start DFS from the click position
        dfs(row, col)
        return board

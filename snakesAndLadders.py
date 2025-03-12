class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # T: O(n ** 2), S: O(n ** 2)
        n = len(board)

        # Convert 2D board to 1D array
        cells = [0] * (n * n + 1)  # 1-indexed
        label = 1
        columns = list(range(0, n))

        # We need to handle the zig-zag pattern of the board
        for row in range(n - 1, -1, -1):
            # For even-indexed rows (from bottom), we move left to right
            if (n - 1 - row) % 2 == 0:
                for col in columns:
                    cells[label] = board[row][col]
                    label += 1
            # For odd-indexed rows (from bottom), we move right to left
            else:
                for col in reversed(columns):
                    cells[label] = board[row][col]
                    label += 1

        # BFS to find shortest path
        queue = deque([(1, 0)])  # (position, moves)
        visited = {1}

        while queue:
            position, moves = queue.popleft()

            # Check if we've reached the destination
            if position == n * n:
                return moves

            # Try all six possible dice rolls
            for next_pos in range(position + 1, min(position + 6, n * n) + 1):
                # If there's a snake or ladder, we follow it
                destination = next_pos if cells[next_pos] == -1 else cells[next_pos]

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

        # If we can't reach the destination
        return -1

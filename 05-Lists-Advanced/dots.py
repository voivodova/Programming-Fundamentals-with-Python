def dfs(board, row, col, visited):

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return 0


    if visited[row][col] or board[row][col] != '.':
        return 0

    visited[row][col] = True

    count = 1
    count += dfs(board, row-1, col, visited)
    count += dfs(board, row+1, col, visited)
    count += dfs(board, row, col-1, visited)
    count += dfs(board, row, col+1, visited)

    return count

def find_largest_count(board):

    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    largest_count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not visited[row][col] and board[row][col] == '.':
                count = dfs(board, row, col, visited)
                largest_count = max(largest_count, count)

    return largest_count


n = int(input())
board = []
for _ in range(n):
    row = input().split()
    board.append(row)

largest_count = find_largest_count(board)
print(largest_count)

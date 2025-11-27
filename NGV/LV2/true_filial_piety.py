import sys
input = sys.stdin.readline

def solve_min_farming_cost():
    board = [list(map(int, input().split())) for _ in range(3)]
        
    min_cost = float('inf')
    target_heights = [1, 2, 3]

    for r in range(3):
        for target in target_heights:
            current_cost = 0

            for c in range(3):
                current_cost += abs(board[r][c] - target)
            
            min_cost = min(min_cost, current_cost)
            
    for c in range(3):
        for target in target_heights:
            current_cost = 0
            
            for r in range(3):
                current_cost += abs(board[r][c] - target)
                
            min_cost = min(min_cost, current_cost)
            
    print(min_cost)

if __name__ == '__main__':
    solve_min_farming_cost()
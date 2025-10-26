def solution(board, moves):
    answer = 0
    bucket = []
    N = len(board)
    
    for col_idx in moves:
        col = col_idx - 1
        doll = 0
        
        for row_idx in range(N):
            if board[row_idx][col] != 0:
                doll = board[row_idx][col]
                board[row_idx][col] = 0
                break
  
        if doll != 0:
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)
                
    return answer
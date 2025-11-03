# 전위순회
def DFS_PRE(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS_PRE(v * 2)
        DFS_PRE(v * 2 + 1)

# 중위순회
def DFS_IN(v):
    if v > 7:
        return
    else:
        DFS_IN(v * 2)
        print(v, end=' ')
        DFS_IN(v * 2 + 1)

# 후위순회
def DFS_POST(v):
    if v > 7:
        return
    else:
        DFS_POST(v * 2)
        DFS_POST(v * 2 + 1)
        print(v, end=' ')

if __name__ == '__main__':
    DFS_PRE(1)
    DFS_IN(1)
    DFS_POST(1)
def solution(n):
    answer = [[0] * n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y, x = 0, 0
    num = 1
    direction = 0
    
    while num<=n*n:
        answer[y][x]=num
        num+=1
        ny=y+dy[direction]
        nx=x+dx[direction]
        if nx>n-1 or ny>n-1 or nx<0 or ny<0 or answer[ny][nx]!=0: #범위를 초과하거나 이미 값을 작성한경우는 방향전환
            direction=(direction+1)%4
            ny=y+dy[direction]
            nx=x+dx[direction]
        y=ny
        x=nx
    

    return answer

import sys

mapList = [[0 for i in range(0, 101)] for i in range(0, 101)]
visit = [[False for i in range(0, 101)] for i in range(0, 101)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = 0
M = 0


def bfs():
    queue = [(0, 0)]
    visit[0][0] = True
    for t in range(1, 2147483647):
        size = len(queue)
        if size == 0:
            return -1

        while size > 0:
            size = size - 1
            x = queue[0][0]
            y = queue[0][1]
            del queue[0]

            if x == N - 1 and y == M - 1:
                return t

            for d in range(0, 4):
                nx = x + direct[d][0]
                ny = y + direct[d][1]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if mapList[nx][ny] == 0 or visit[nx][ny]:
                    continue
                queue.append((nx, ny))
                visit[nx][ny] = True


def func():
    print(bfs())


def input():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    for i in range(0, N):
        mapList[i] = list(map(int, sys.stdin.readline().strip()))


if __name__ == '__main__':
    input()
    func()

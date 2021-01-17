#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> location_t;
char maze[1000][1001];

bool canMove(int i, int j, int R, int C) {
    return (0 <= i && i < R && 0 <= j && j < C && maze[i][j] == '.');
}

int main(void) {
    int R, C;
    scanf("%d %d", &R, &C);

    bool visited[1000][1000] = { false };
    queue<location_t> jihoons;
    queue<location_t> fires;
    
    for(int i = 0; i < R; i++) {
        scanf("%s", maze[i]);

        for(int j = 0; j < C; j++) {
            if(maze[i][j] == 'J') {
                jihoons.push(make_pair(i, j));
                visited[i][j] = true;
                maze[i][j] = '.';
            }
            
            if(maze[i][j] == 'F') {
                fires.push(make_pair(i, j));
            }
        }
    }

    // 처음부터 가장자리에 위치한 경우
    int i = jihoons.front().first;
    int j = jihoons.front().second;
    if(i == 0 || i == R-1 || j == 0 || j == C-1) {
        printf("1\n");
        return 0;
    }

    // 1번 이상을 움직여야 가장자리에 위치하는 경우
    int answer = -1;
    int move = 0;
    int move_i[] = { -1, 0, 1,  0 },
        move_j[] = {  0, 1, 0, -1 };
    while(answer == -1 && !jihoons.empty()) {
        move++;

        // 불 이동
        int fires_size = fires.size();
        for(int k = 0; k < fires_size; k++) {
            location_t fire = fires.front(); fires.pop();
            
            for(int l = 0; l < 4; l++) {
                int next_i = fire.first + move_i[l];
                int next_j = fire.second + move_j[l];
                if(canMove(next_i, next_j, R, C)) {
                    fires.push(make_pair(next_i, next_j));
                    maze[next_i][next_j] = 'F';
                }
            }
        }

        // 지훈이 이동
        int jihoons_size = jihoons.size();
        for(int k = 0; answer == -1 && k < jihoons_size; k++) {
            location_t jihoon = jihoons.front(); jihoons.pop();

            for(int l = 0; l < 4; l++) {
                int next_i = jihoon.first + move_i[l];
                int next_j = jihoon.second + move_j[l];
                
                if(canMove(next_i, next_j, R, C) && !visited[next_i][next_j]) {
                    // 이동한 위치가 가장자리이면 종료
                    if(next_i == 0 || next_i == R-1 || next_j == 0 || next_j == C-1) {
                        answer = move + 1;
                        break;
                    }

                    jihoons.push(make_pair(next_i, next_j));
                    visited[next_i][next_j] = true;
                }
            }
        }
    }

    if(answer == -1) printf("IMPOSSIBLE\n");
    else printf("%d\n", answer);
    return 0;
}

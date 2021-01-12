#include <stdio.h>
#include <queue>
#include <utility>
using namespace std;

/*
 * isRange - (x, y)가 범위 내에 있는지 판단한다.
 * 
 * @param   N       공간의 크기
 * @param   x, y    현재 위치
 * @return  0   범위를 벗어난 경우
 *          1   범위 내에 있는 경우
 */
int isRange(int N, int x, int y) {
    return (0 <= x && x < N && 0 <= y && y < N);
}

/*
 * isEatenFirst - (x, y)의 물고기가 ret에 저장된 물고기보다 먼저 먹히는지 판단한다.
 * 
 * @param   dist, x, y  살펴볼 물고기와의 거리와 위치
 * @param   ret, fish   현재까지 먹을 수 있는 물고기 중 가장 가까운 물고기
 * @return  0   ret 내의 물고기가 먼저 먹힐 경우
 *          1   (x, y)의 물고기가 먼저 먹힐 경우
 */
int isEatenFirst(int dist, int x, int y, int ret, pair<int, int> fish) {
    return ((dist < ret) ||
            (dist == ret && (x < fish.first || (x == fish.first && y < fish.second))));
}

/*
 * nextPos - 상어의 다음 위치와 이동 거리를 결정한다.
 * 
 * @param   map         공간의 상태
 * @param   N           공간의 크기
 * @param   fish        상어의 위치
 * @param   fish_size   현재 상어의 크기
 * @return  500     상어가 이동 못 할 경우
 *          ret     상어의 다음 위치까지 거리
 */
int nextPos(int map[][20], int N, pair<int, int> &fish, pair<int, int> fish_size) {
    int next_x, next_y, next_dist;
    int ret = 500;
    int move_x[] = {-1, 1, 0, 0},
        move_y[] = {0, 0, -1, 1};  // 상하좌우
    int chk[20][20] = { 0, };
    pair<int, pair<int, int> > p;
    queue<pair<int, pair<int, int> > > que;

    que.push(make_pair(0, fish));
    chk[fish.first][fish.second] = 1;
    while(que.size() != 0) {
        p = que.front(); que.pop();
        
        next_dist = p.first + 1;
        for(int i = 0; i < 4; i++) {
            next_x = p.second.first + move_x[i];
            next_y = p.second.second + move_y[i];

            if(!isRange(N, next_x, next_y) || chk[next_x][next_y] == 1 || map[next_x][next_y] > fish_size.first) continue;

            if(map[next_x][next_y] != 0 && map[next_x][next_y] < fish_size.first && isEatenFirst(next_dist, next_x, next_y, ret, fish)) {
                ret = next_dist;
                fish = make_pair(next_x, next_y);
            } else {
                que.push(make_pair(next_dist, make_pair(next_x, next_y)));
            }
            chk[next_x][next_y] = 1;
        }
    }
    return ret;
}

/*
 * updateFishSize - 상어가 물고기 1마리 먹은 후의 크기로 업데이트한다.
 * 
 * @param   fish_size   물고기의 크기, 현재 크기에서 먹은 물고기의 수
 */
void updateFishSize(pair<int, int> &fish_size) {
    fish_size.second += 1;
    if(fish_size.first == fish_size.second) {
        fish_size.first += 1;
        fish_size.second = 0;
    }
}

int main(void) {
    int N, move_cnt;
    int ret = 0;
    int map[20][20];
    pair<int, int> fish, fish_size;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%d", &map[i][j]);
            if(map[i][j] == 9) {
                fish = make_pair(i, j);
                map[i][j] = 0;
            }
        }
    }

    fish_size = make_pair(2, 0);
    while(1) {
        move_cnt = nextPos(map, N, fish, fish_size);
        
        if(move_cnt == 500) break;
        
        ret += move_cnt;
        map[fish.first][fish.second] = 0;
        updateFishSize(fish_size);
    }
    printf("%d\n", ret);

    return 0;
}
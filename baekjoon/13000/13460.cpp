#include <stdio.h>
#include <queue>
using namespace std;

char map[10][11];
queue<int> que;
int chk[10][10][10][10];

void myEnque(int *pos) {
    if(chk[pos[0]][pos[1]][pos[2]][pos[3]] == 1) return ;
    for(int i = 0; i < 5; i++) {
        que.push(pos[i]);
    }
    chk[pos[0]][pos[1]][pos[2]][pos[3]] = 1;
}

void myDeque(int *pos) {
    for(int i = 0; i < 5; i++) {
        pos[i] = que.front(); que.pop();
    }
}

/*
 * findNextPosition - 구슬의 다음 위치를 구한다.
 * 
 * 구슬을 벽 또는 구멍을 만날 때까지 이동시킨다.
 * @return 0 - 구슬이 구멍에 빠진 경우
 *         1 - 구슬이 벽을 만난 경우
 */
int findNextPosition(int *x, int *y, int move_x, int move_y) {
    int next_x = *x;
    int next_y = *y;
    while(1) {
        next_x += move_x;
        next_y += move_y;

        if(map[next_x][next_y] == 'O') {
            return 0;
        }
        if(map[next_x][next_y] == '#') {
            *x = next_x - move_x;
            *y = next_y - move_y;
            return 1;
        }
    }
}

/*
 * run - 판을 뒤집으며 구슬을 이동시킨다.
 * 
 * 판을 상하좌우 순으로 뒤집고 이에 따른 구슬의 위치와 이동 횟수를 next_pos에 저장한다.
 * @return 1 - 빨간 구슬만 구멍에 빠질 경우(문제 해결)
 *         0 - 두 구슬 모두 구멍에 빠지거나 이동 횟수가 10회를 넘을 경우
 */
int run() {
    int R, B;
    int pos[5]; myDeque(pos);
    int next_pos[5];
    int comp_left[4] = {pos[0], pos[2], pos[1], pos[3]},
        comp_right[4] = {pos[2], pos[0], pos[3], pos[1]},
        move_x[4] = {-1, 1, 0, 0},
        move_y[4] = {0, 0, -1, 1};  // 상하좌우

    for(int i = 0; i < 4; i++) {
        for(int idx = 0; idx < 5; idx++) {
            next_pos[idx] = pos[idx];
        }

        if(comp_left[i] < comp_right[i]) {  // 빨간 구슬 먼저 이동
            R = findNextPosition(&next_pos[0], &next_pos[1], move_x[i], move_y[i]);
            if((B = findNextPosition(&next_pos[2], &next_pos[3], move_x[i], move_y[i])) == 0) continue;

            // 빨간 구슬과 파란 구슬의 위치가 같으면 파란 구슬을 한 칸 이동 전으로 되돌리기
            if(next_pos[0] == next_pos[2] && next_pos[1] == next_pos[3]) {
                next_pos[2] -= move_x[i];
                next_pos[3] -= move_y[i];
            }
        } else {  // 파란 구슬 먼저 이동
            if((B = findNextPosition(&next_pos[2], &next_pos[3], move_x[i], move_y[i])) == 0) continue;
            R = findNextPosition(&next_pos[0], &next_pos[1], move_x[i], move_y[i]);
            
            // 빨간 구슬과 파란 구슬의 위치가 같으면 빨간 구슬을 한 칸 이동 전으로 되돌리기
            if(next_pos[0] == next_pos[2] && next_pos[1] == next_pos[3]) {
                next_pos[0] -= move_x[i];
                next_pos[1] -= move_y[i];
            }
        }
        next_pos[4] += 1;

        if(R == 0 && B == 1) {
            printf("%d\n", next_pos[4]);
            return 1;
        } else if(R == 1 && B == 1 && next_pos[4] < 10) {
            myEnque(next_pos);
        }
    }
    return 0;
}

void init(int N, int M) {
    int pos[5];

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(map[i][j] == 'R') {
                pos[0] = i; pos[1] = j;
            } else if(map[i][j] == 'B')  {
                pos[2] = i; pos[3] = j;
            }
        }
    }
    pos[4] = 0;
    myEnque(pos);
}

int main(void) {
    int N, M;

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        scanf("%s", map[i]);
    }

    init(N, M);
    while(que.size() != 0) {
        if(run() == 1) return 0;
    }
    printf("-1\n");
    return 0;
}
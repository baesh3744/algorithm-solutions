#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

#define BOARD_SIZE 101

int N, M;
int ladder[15][2], snake[15][2], board[BOARD_SIZE];
queue<int> que;

int lors(int cur, int endi, int type[][2]) {
    for(int i = 0; i < endi; i++) {
        if(cur == type[i][0]) return type[i][1];
    }
    return 0;
}

void checkAndPush(int cur) {
    if(board[cur] == 0) {
        int next;

        if((next = lors(cur, N, ladder)) == 0 && (next = lors(cur, M, snake)) == 0) next = cur;

        if(board[next] == 0) {
            que.push(next);
            board[next] = 1;
        }
    }
}

int main(void) {
    int ans = 0;

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) { scanf("%d %d", &ladder[i][0], &ladder[i][1]); }
    for(int i = 0; i < M; i++) { scanf("%d %d", &snake[i][0], &snake[i][1]); }
    memset(board, 0, sizeof(int) * BOARD_SIZE);

    que.push(1);
    board[1] = 1;
    while(que.size() != 0) {
        int size = que.size();
        
        while((size--) > 0) {
            int cur = que.front(); que.pop();
            
            if(cur == 100) { printf("%d\n", ans); return 0; }

            for(int i = 1; i <= 6; i++) {
                checkAndPush(cur + i);
            }
        }
        
        ans++;
    }
}
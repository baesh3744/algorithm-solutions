#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

#define CHECK_SIZE 513

int check[CHECK_SIZE];
queue<int> que;
int next_idx[][5] = {
    {0, 1, 3, -1, -1},  {0, 1, 2, 4, -1},   {1, 2, 5, -1, -1},
    {0, 3, 4, 6, -1},   {1, 3, 4, 5, 7},    {2, 4, 5, 8, -1},
    {3, 6, 7, -1, -1},  {4, 6, 7, 8, -1},   {5, 7, 8, -1, -1}
};

int paintBoard(int cur, int idx) {
    int nidx, item;
    int ret = cur;

    for(int i = 0; i < 5; i++) {
        if(next_idx[idx][i] != -1) {
            nidx = next_idx[idx][i];
            item = 1 << nidx;

            if((ret & item) > 0) ret &= ~item;
            else ret |= item;
        }
    }

    return ret;    
}

void bfs(int cur) {
    for(int i = 0; i < 9; i++) {
        int new_cur = paintBoard(cur, i);
        if(check[new_cur] == 0) {
            que.push(new_cur);
            check[new_cur] = 1;
        }
    }
}

int main(void) {
    int P, init, cur, ans, go, size;
    char board[4];

    scanf("%d", &P);

    for(int i = 0; i < P; i++) {
        init = ans = 0;
        go = 1;
        memset(check, 0, sizeof(int) * CHECK_SIZE);
        while(que.size() != 0) { que.pop(); }

        for(int j = 0; j < 3; j++) {
            scanf("%s", board);

            for(int k = 0; k < 3; k++) {
                init <<= 1;
                if(board[k] == '*') init += 1;
            }
        }

        que.push(0);
        while(go == 1 && que.size() != 0) {
            size = que.size();
            while(go == 1 && (size--) > 0) {
                cur = que.front(); que.pop();
                if(cur == init) {
                    printf("%d\n", ans);
                    go = 0;
                } else {
                    bfs(cur);
                }
            }
            ans++;
        }
    }

    return 0;
}
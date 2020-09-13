#include <stdio.h>
#include <string.h>

#define SIZE 50

int M, N;
int cabbage[SIZE][SIZE];
int move_y[] = {0, 1, 0, -1};
int move_x[] = {1, 0, -1, 0};

int isRange(int y, int x) {
    if(0 <= y && y <= N - 1 && 0 <= x && x <= M - 1) return 1;
    return 0;
}

void eraseCabbage(int y, int x) {
    cabbage[y][x] = 0;
    for(int i = 0; i < 4; i++) {
        int next_y = y + move_y[i];
        int next_x = x + move_x[i];
        if(isRange(next_y, next_x) == 1 && cabbage[next_y][next_x] == 1) eraseCabbage(next_y, next_x);
    }
}

int main(void) {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int K, X, Y;
        int ans = 0;

        memset(cabbage, 0, sizeof(int) * SIZE * SIZE);
        scanf("%d %d %d", &M, &N, &K);
        for(int j = 0; j < K; j++) {
            scanf("%d %d", &X, &Y);
            cabbage[Y][X] = 1;
        }

        for(int y = 0; y < N; y++) {
            for(int x = 0; x < M; x++) {
                if(cabbage[y][x] == 1) {
                    eraseCabbage(y, x);
                    ans++;
                }
            }
        }
        printf("%d\n", ans);
    }

    return 0;
}
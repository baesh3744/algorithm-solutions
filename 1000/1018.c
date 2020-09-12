#include <stdio.h>

#define MAX 50
#define min(a, b) (a < b ? a : b)
char board[MAX][MAX];

char answer_board[2][8][8] = {
    {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    },
    {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    }
};

int paintBoard(int y, int x, int color) {
    int ret = 0;

    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(board[y + i][x + j] != answer_board[color][i][j]) {
                ret++;
            }
        }
    }

    return ret;
}

int main(void) {
    int N, M;
    int ans = 100;

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        scanf("%s", board[i]);
    }

    for(int i = 0; i <= N - 8; i++) {
        for(int j = 0; j <= M - 8; j++) {
            ans = min(ans, paintBoard(i, j, 0));
            ans = min(ans, paintBoard(i, j, 1));
        }
    }
    printf("%d", ans);

    return 0;
}
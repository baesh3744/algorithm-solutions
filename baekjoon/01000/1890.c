#include <stdio.h>

#define MAX_N 100

int N;
int board[MAX_N][MAX_N];
long long cache[MAX_N][MAX_N];

int isRange(int idx) {
    return ((0 <= idx) && (idx < N));
}

long long dp(int i, int j) {
    if((i == N-1) && (j == N-1)) return 1;
    if(cache[i][j] != 0) return cache[i][j];
    if(board[i][j] == 0) return 0;

    long long ret = 0;
    int next_i = i + board[i][j];
    int next_j = j + board[i][j];
    if(isRange(next_i)) ret += dp(next_i, j);
    if(isRange(next_j)) ret += dp(i, next_j);
    return (cache[i][j] = ret);
}

int main(void) {
    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%d", &board[i][j]);
        }
    }

    printf("%lld\n", dp(0, 0));
    return 0;
}

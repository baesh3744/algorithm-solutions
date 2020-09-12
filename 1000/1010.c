#include <stdio.h>

int dp[30][30] = {0};

int combination(int n, int r) {
    if(dp[n][r] != 0) {
        return dp[n][r];
    }

    if(n == r || r == 0) {
        return 1;
    }

    return (dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r));
}

int main(void) {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N, M;

        scanf("%d %d", &N, &M);

        printf("%d\n", combination(M, N));
    }

    return 0;
}
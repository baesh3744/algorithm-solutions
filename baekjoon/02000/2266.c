#include <stdio.h>

int cache[501][501];

int dp(int n, int k) {
    if(n == 0) return 0;
    if(k == 1) return n;
    if(cache[n][k]) return cache[n][k];

    int ret = 1000;
    for(int i = 0; i < n; i++) {
        int broken = dp(i, k-1), not_broken = dp(n-i-1, k);
        int cur = broken > not_broken ? broken : not_broken;
        ret = ret < cur ? ret : cur;
    }
    return (cache[n][k] = ret + 1);
}

int main(void) {
    int N, K;
    scanf("%d %d", &N, &K);

    printf("%d\n", dp(N, K));
    return 0;
}

// 10 2
// 1층에서 낙하 - 깨지면, (0, 1) 안깨지면, (9, 2) --> 깨질 때와 안 깨질 때 중 큰 값(최악인 경우)
// 2층에서 낙하 - 깨지면, (1, 1) 안깨지면, (8, 2)
// 3층에서 낙하 - 깨지면, (2, 1) 안깨지면, (7, 2)
// 4층에서 낙하 - 깨지면, (3, 1) 안깨지면, (6, 2)
// 5층에서 낙하 - 깨지면, (4, 1) 안깨지면, (5, 2)
// 6층에서 낙하 - 깨지면, (5, 1) 안깨지면, (4, 2)
// 7층에서 낙하 - 깨지면, (6, 1) 안깨지면, (3, 2)
// 8층에서 낙하 - 깨지면, (7, 1) 안깨지면, (2, 2)
// 9층에서 낙하 - 깨지면, (8, 1) 안깨지면, (1, 2)
// 10층에서 낙하 - 깨지면, (9, 1) 안깨지면, (0, 2)
// --> 각 층에서 낙하한 값들 중 최소값

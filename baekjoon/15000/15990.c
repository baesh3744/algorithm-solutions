#include <stdio.h>

#define MOD 1000000009

int cache[100001][3];

int dp(int num, int first) {
    if(num < 0) return 0;
    if(num == 0) return 1;
    if(cache[num][first-1] != 0) return cache[num][first-1];

    int *ptr = &cache[num][first-1];
    for(int i = 1; i <= 3; i++) {
        if(i == first) continue;
        *ptr += dp(num - i, i);
        *ptr %= MOD;
    }
    return *ptr;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int num;
        scanf("%d", &num);

        int ans = 0;
        for(int j = 1; j <= 3; j++) {
            ans += dp(num - j, j);
            ans %= MOD;
        }
        printf("%d\n", ans);
    }
    return 0;
}

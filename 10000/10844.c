#include <stdio.h>

int cache[10][101];

/*
 * findStairsByN - 첫 자리 숫자가 cur이고 길이가 n인 수의 개수를 구한다.
 */
int findStairsByN(int cur, int n) {
    if(n == 1) return 1;
    if(cache[cur][n] != 0) return cache[cur][n];

    int ret = 0;
    if(cur-1 >= 0) ret += (cache[cur-1][n-1] = findStairsByN(cur-1, n-1));
    if(cur+1 <= 9) ret += (cache[cur+1][n-1] = findStairsByN(cur+1, n-1));
    return (cache[cur][n] = ret % 1000000000);
}

int main(void) {
    int N;
    scanf("%d", &N);

    int ans = 0;
    for(int i = 1; i < 10; i++) {
        ans += findStairsByN(i, N);
        ans %= 1000000000;
    }
    printf("%d\n", ans);
    return 0;
}

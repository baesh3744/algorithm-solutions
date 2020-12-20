#include <stdio.h>
#include <string.h>

#define maxN 1001
#define overflow 2000

int N;
int A[maxN];
int cache[maxN];

/*
 * dp - cur에서 오른쪽 끝 칸으로 갈 때, 해야할 점프의 최소 횟수를 구한다.
 * @return  점프의 최소 횟수
 *          overflow    오른쪽 끝 칸으로 갈 수 없을 때
 */
int dp(int cur) {
    if(cur > N) return overflow;
    if(cur == N) return 0;
    if(cache[cur] != -1) return cache[cur];

    int ret = overflow;
    for(int i = 1; i <= A[cur]; i++) {
        int cmp = 1 + dp(cur + i);
        ret = (ret < cmp ? ret : cmp);
    }
    return (cache[cur] = ret);
}

int main(void) {
    scanf("%d", &N);

    for(int i = 1; i <= N; i++) {
        scanf("%d", &A[i]);
    }

    memset(cache, -1, sizeof(int)*maxN);

    int ans;
    if((ans =  dp(1)) < overflow) printf("%d\n", ans);
    else printf("-1\n");
    return 0;
}

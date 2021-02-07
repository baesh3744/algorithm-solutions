#include <stdio.h>

#define min(a,b) (a < b ? a : b)
#define max(a,b) (a < b ? b : a)

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);

        int dough[1000][2];
        for(int j = 0; j < N; j++) {
            scanf("%d %d", &dough[j][0], &dough[j][1]);
        }

        int cache[2][100001];
        for(int k = 0; k <= 100000; k++) {
            if(k < dough[0][0]) cache[0][k] = dough[0][1];
            else cache[0][k] = 0;
        }

        for(int j = 1; j < N; j++) {
            for(int k = 0; k <= 100000; k++) {
                int cur = j % 2;
                int pre = (j - 1) % 2;
                
                if(k < dough[j][0]) {
                    cache[cur][k] = cache[pre][k] + dough[j][1];
                } else {
                    cache[cur][k] = min(cache[pre][k - dough[j][0]], cache[pre][k] + dough[j][1]);
                }
            }
        }

        int idx = (N - 1) % 2;
        int ans = 300000;
        for(int j = 0; j <= 100000; j++) {
            ans = min(ans, max(j, cache[idx][j]));
        }
        printf("%d\n", ans);
    }
    return 0;
}

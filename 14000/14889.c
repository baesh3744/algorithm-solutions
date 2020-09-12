#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define min(a, b) (a < b ? a : b)
#define MAX_N 21

int N, ans;
int S[MAX_N][MAX_N], check[MAX_N];

void dfs(int cur, int cnt) {
    if(cnt == N/2) {
        int check_sum = 0;
        int no_check_sum = 0;

        for(int i = 1; i <= N; i++) {
            for(int j = i+1; j <= N; j++) {
                if(check[i] == 1 && check[j] == 1) {
                    check_sum += S[i][j];
                    check_sum += S[j][i];
                } else if(check[i] == 0 && check[j] == 0) {
                    no_check_sum += S[i][j];
                    no_check_sum += S[j][i];
                }
            }
        }

        ans = min(ans, abs(check_sum - no_check_sum));
        return ;
    }

    for(int i = cur + 1; i <= N; i++) {
        if(check[i] == 0) {
            check[i] = 1;
            dfs(i, cnt + 1);
            check[i] = 0;
        }
    }
}

int main(void) {
    ans = 2147483647;
    memset(check, 0, sizeof(int) * MAX_N);
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            scanf("%d", &S[i][j]);
        }
    }

    dfs(0, 0);
    printf("%d\n", ans);

    return 0;
}
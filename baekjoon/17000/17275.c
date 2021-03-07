#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solve() {
    int N, M;
    scanf("%d %d", &N, &M);

    int* alliance = (int*)malloc(sizeof(int) * (N + 1));
    memset(alliance, 0, sizeof(int) * (N + 1));
    for(int i = 0; i < M; i++) {
        int x, y;
        scanf("%d %d", &x, &y);

        alliance[x]++; alliance[y]++;
    }

    long long pair_total = 1LL * N * (N - 1) * (N - 2) / 6;
    long long pair_nothing = 0;
    for(int i = 1; i <= N; i++) {
        pair_nothing += 1LL * alliance[i] * (N - 1 - alliance[i]);
    }
    printf("%lld\n", pair_total - pair_nothing / 2);

    free(alliance);
    return;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) solve();
    return 0;
}

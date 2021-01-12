#include <stdio.h>

int main(void) {
    int L, P, V, cnt, extra;
    int idx = 1;

    while(1) {
        scanf("%d %d %d", &L, &P, &V);

        if(L == 0 && P == 0 && V == 0) break;

        cnt = V / P;
        extra = V % P < L ? V % P : L;
        printf("Case %d: %d\n", idx++, L * cnt + extra);
    }

    return 0;
}
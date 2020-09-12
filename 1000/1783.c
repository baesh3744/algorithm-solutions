#include <stdio.h>

int main(void) {
    int N, M, ans;

    scanf("%d %d", &N, &M);

    if(N == 1) ans = 1;
    else if(N == 2) ans = (M - 1) / 2 + 1 < 4 ? (M - 1) / 2 + 1 : 4;
    else if(M < 7) ans = M < 4 ? M : 4;
    else ans = M - 2 > 4 ? M - 2 : 4;
    printf("%d\n", ans);

    return 0;
}
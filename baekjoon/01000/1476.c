#include <stdio.h>

int main(void) {
    int E, S, M, ans;
    int go = 1;

    scanf("%d %d %d", &E, &S, &M);

    ans = S;
    while(go == 1) {
        if((ans - E) % 15 == 0 && (ans - M) % 19 == 0) {
            printf("%d\n", ans);
            go = 0;
        }
        ans += 28;
    }

    return 0;
}
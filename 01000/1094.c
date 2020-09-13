#include <stdio.h>

int main(void) {
    int X;
    int ans = 0;

    scanf("%d", &X);

    while(X > 0) {
        if(X % 2 == 1) ans++;
        X /= 2;
    }
    printf("%d\n", ans);

    return 0;
}
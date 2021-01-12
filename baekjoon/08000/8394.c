#include <stdio.h>

int cache[10000001];

int main(void) {
    int n;

    scanf("%d", &n);

    cache[1] = 1;
    cache[2] = 2;
    for(int i = 3; i <= n; i++) {
        cache[i] = (cache[i-1] + cache[i-2]) % 10;
    }

    printf("%d\n", cache[n]);

    return 0;
}
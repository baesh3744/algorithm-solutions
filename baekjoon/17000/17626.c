#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX_N 50001
#define min(a, b) (a < b ? a : b)

int main(void) {
    int n, cache[MAX_N];

    scanf("%d", &n);
    memset(cache, 50000, sizeof(int) * MAX_N);
    cache[0] = 0;

    for(int i = 1; i <= n; i++) {
        for(int j = (int)sqrt((double)i); j > 0; j--) {
            cache[i] = min(cache[i], cache[i - j * j] + 1);
        }
    }
    printf("%d\n", cache[n]);

    return 0;
}
#include <stdio.h>

#define MAX_TIME 250 * 250
#define max(a, b) (a < b ? b : a)
#define min(a, b) (a < b ? a : b)

int main(void) {
    int n;
    scanf("%d", &n);

    int a[250], b[250];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a[i], &b[i]);
    }

    int cache[2][MAX_TIME];
    // 첫 번째 작업
    for (int t = 0; t < MAX_TIME; t++) {
        if (t < a[0])
            cache[0][t] = b[0];
        else
            cache[0][t] = 0;
    }

    // 첫 번째 이후 작업
    for (int i = 1; i < n; i++) {
        int cur = i % 2;
        int past = (i - 1) % 2;

        for (int t = 0; t < MAX_TIME; t++) {
            if (t < a[i])
                cache[cur][t] = cache[past][t] + b[i];
            else
                cache[cur][t] = min(cache[past][t - a[i]], cache[past][t] + b[i]);
        }
    }

    int ans = MAX_TIME;
    int idx = (n - 1) % 2;
    for (int t = 0; t < MAX_TIME; t++) {
        ans = min(ans, max(t, cache[idx][t]));
    }
    printf("%d\n", ans);
    return 0;
}

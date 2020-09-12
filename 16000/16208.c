#include <stdio.h>

int main(void) {
    int n;
    int total = 0;
    long long bar_length[500000];
    long long cost = 0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%lld", &bar_length[i]);
        total += bar_length[i];
    }

    for(int i = 0; i < n; i++) {
        total -= bar_length[i];
        cost += bar_length[i] * total;
    }
    printf("%lld\n", cost);

    return 0;
}
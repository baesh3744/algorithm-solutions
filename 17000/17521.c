#include <stdio.h>

int main(void) {
    int n, min;
    int find_min = 1;
    int s[15];
    long long W, coin;

    scanf("%d %lld", &n, &W);
    for(int i = 0; i < n; i++) {
        scanf("%d", &s[i]);

        if(i == 0) continue;
        if(find_min == 1 && (s[i-1] < s[i])) {
            min = s[i-1];
            coin = W / min;
            find_min = 0;
        } else if(find_min == 0 && (s[i-1] > s[i])) {
            W += coin * (s[i-1] - min);
            find_min = 1;
        }

        if(find_min == 0 && i == n-1) {
            W += coin * (s[i] - min);
        }
    }
    printf("%lld\n", W);

    return 0;
}
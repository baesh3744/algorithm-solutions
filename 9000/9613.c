#include <stdio.h>

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main(void) {
    int t;
    
    scanf("%d", &t);

    for(int i = 0; i < t; i++) {
        int n;
        long long sum;

        scanf("%d", &n);

        int num[n];

        for(int j = 0; j < n; j++) {
            scanf("%d", &num[j]);
        }

        sum = 0;
        for(int j = 0; j < n; j++) {
            for(int k = j + 1; k < n; k++) {
                sum += gcd(num[j], num[k]);
            }
        }

        printf("%lld\n", sum);
    }

    return 0;
}
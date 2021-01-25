#include <stdio.h>

long long sum(long long n) {
    if(n <= 0) return 0;

    long long pow = 1;
    long long sum = 0;
    long long after = 0;
    while(n > 0) {
        long long before = n / 10;
        long long point = n % 10;
    
        for(int i = 1; i < 10; i++) {
            if(i < point) {
                sum += (before + 1) * pow * i;
            } else if(i == point) {
                if(before > 0) sum += before * pow * i;
                sum += (after + 1) * i;
            } else {
                sum += before * pow * i;
            }
        }

        after += point * pow;
        n /= 10;
        pow *= 10;
    }
    return sum;
}

int main(void) {
    int L, U;
    scanf("%d %d", &L, &U);

    printf("%lld\n", sum(U) - sum(L-1));
    return 0;
}

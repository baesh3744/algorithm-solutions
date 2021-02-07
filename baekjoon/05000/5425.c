#include <stdio.h>

long long sum(long long num) {
    if(num <= 0) return 0;

    long long sum = 0;
    long long after = 0;
    long long pow = 1;
    while(num > 0) {
        long long before = num / 10;
        int point = num % 10;

        // 1 ~ point-1
        int subsum = point * (point - 1) / 2;
        sum += (before + 1) * pow * subsum;

        // point
        subsum = point;
        sum += before * pow * subsum;
        sum += 1 * (after + 1) * subsum;

        // point+1 ~ 9
        subsum = (point + 10) * (9 - point) / 2;
        sum += before * pow * subsum;

        after += point * pow;
        num /= 10;
        pow *= 10;
    }
    return sum;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);

        printf("%lld\n", sum(b) - sum(a-1));
    }
    return 0;
}

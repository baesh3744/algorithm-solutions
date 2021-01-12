#include <stdio.h>

int main(void) {
    long long k;
    int cnt = 0;

    scanf("%lld", &k);

    k -= 1;
    while(k > 0) {
        cnt += k & 1;
        k >>= 1;
    }

    printf("%d\n", cnt % 2);
    
    return 0;
}
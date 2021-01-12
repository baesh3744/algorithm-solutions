#include <stdio.h>
#include <string.h>

#define MAX_SIZE 81
long long cache[MAX_SIZE];

long long fibo(int n) {
    if(n == 0 || n == 1 || cache[n] != 0) return cache[n];
    return cache[n] = fibo(n - 1) + fibo(n - 2);
}

int main(void) {
    int N;

    scanf("%d", &N);
    memset(cache, 0, sizeof(long long) * MAX_SIZE);
    cache[1] = 1;

    fibo(N);
    printf("%lld\n", 4 * cache[N] + 2 * cache[N - 1]);

    return 0;
}
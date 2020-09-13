#include <stdio.h>
#include <string.h>

#define MAX_SIZE 91
long long cache[MAX_SIZE];

long long fibo(int n) {
    if(n == 0 || n == 1 || cache[n] != 0) return cache[n];
    return cache[n] = fibo(n - 1) + fibo(n - 2);
}

int main(void) {
    int n;

    scanf("%d", &n);
    memset(cache, 0, sizeof(long long) * MAX_SIZE);
    cache[1] = 1;

    printf("%lld\n", fibo(n));

    return 0;
}
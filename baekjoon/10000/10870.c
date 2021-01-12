#include <stdio.h>
#include <string.h>

#define MAX_SIZE 25
int cache[MAX_SIZE];

int fibo(int n) {
    if(n == 0) return 0;
    if(n == 1) return 1;

    if(cache[n] == -1) return cache[n] = fibo(n - 1) + fibo(n - 2);
    else return cache[n];
}

int main(void) {
    int n;
    
    memset(cache, -1, sizeof(int) * MAX_SIZE);
    scanf("%d", &n);

    printf("%d\n", fibo(n));

    return 0;
}
#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100001
int cache[MAX_SIZE];

int countCoins(int n) {
    if(n < 0) return -1;
    if(n == 0) return 0;

    if(cache[n] != 0) return cache[n];
    if((countCoins(n - 5) == -1) && (countCoins(n - 2) == -1)) return cache[n] = -1;
    else if(countCoins(n - 2) == -1) return cache[n] = cache[n - 5] + 1;
    else if(countCoins(n - 5) == -1) return cache[n] = cache[n - 2] + 1;
    else return cache[n] = cache[n - 5] < cache[n - 2] ? cache[n - 5] + 1 : cache[n - 2] + 1;
}

int main(void) {
    int n;

    scanf("%d", &n);
    memset(cache, 0, sizeof(int) * MAX_SIZE);

    printf("%d\n", countCoins(n));

    return 0;
}
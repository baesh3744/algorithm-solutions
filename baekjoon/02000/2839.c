#include <stdio.h>
#include <string.h>

#define MAX_SIZE 5005
int cache[MAX_SIZE];

int alctBag(int n) {
    if(n < 0 || cache[n] == -1) return -1;
    if(n == 0) return 1;
    
    if(cache[n] == 0) {
        if(((alctBag(n - 3) == -1) && (alctBag(n - 5) == -1))) cache[n] = -1;
        else if(alctBag(n - 5) == -1) cache[n] = cache[n - 3] + 1;
        else if(alctBag(n - 3) == -1) cache[n] = cache[n - 5] + 1;
        else cache[n] = (cache[n - 3] < cache[n - 5] ? cache[n - 3] + 1 : cache[n - 5] + 1);
    }
    return cache[n];
}

int main(void) {
    int N;

    memset(cache, 0, sizeof(int) * MAX_SIZE);
    scanf("%d", &N);

    printf("%d\n", alctBag(N));

    return 0;
}
#include <stdio.h>
#include <string.h>

#define MAX_SIZE 305
int cache[MAX_SIZE];
int A, B, C;

int allocateRoom(int n) {
    if(n == 0) return 1;
    if(n < 0) return 0;

    if(cache[n] != -1) return cache[n];
    else return cache[n] = allocateRoom(n - A) | allocateRoom(n - B) | allocateRoom(n - C);
}

int main(void) {
    int N;

    memset(cache, -1, sizeof(int) * MAX_SIZE);
    scanf("%d %d %d %d", &A, &B, &C, &N);

    printf("%d\n", allocateRoom(N));

    return 0;
}
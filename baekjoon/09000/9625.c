#include <stdio.h>
#include <string.h>

#define MAX_SIZE 46
int cache[MAX_SIZE][2];
int countA(int k);
int countB(int k);

int countA(int k) {
    if(k == 0) return 1;

    if(cache[k][0] == 0) cache[k][0] = countB(k - 1);
    return cache[k][0];
}

int countB(int k) {
    if(k == 0) return 0;

    if(cache[k][1] == 0) cache[k][1] = countA(k - 1) + countB(k - 1);
    return cache[k][1];
}

int main(void) {
    int K;

    memset(cache, 0, sizeof(int) * MAX_SIZE * 2);
    scanf("%d", &K);

    printf("%d %d\n", countA(K), countB(K));

    return 0;
}
#include <stdio.h>
#include <string.h>

#define MAX 31
int cache[MAX][MAX];

int pascalTri(int n, int k) {
    if(cache[n][k] != 0) return cache[n][k];
    if(k == 1 || n == k) return cache[n][k] = 1;

    return cache[n][k] = pascalTri(n - 1, k - 1) + pascalTri(n - 1, k);
}

int main(void) {
    int n, k;

    scanf("%d %d", &n, &k);
    memset(cache, 0, sizeof(int) * MAX * MAX);

    printf("%d\n", pascalTri(n, k));

    return 0;
}
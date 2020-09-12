#include <stdio.h>

int main(void) {
    int N, M, dist;
    int max_dist = 0;
    int x[100001];

    scanf("%d %d", &N, &M);
    for(int i = 1; i <= M; i++) {
        scanf("%d", &x[i]);
    }
    x[0] = 0;
    x[M+1] = N;

    for(int i = 1; i <= M+1; i++) {
        if(i == 1 || i == M+1) dist = x[i] - x[i-1];
        else if((dist = (x[i] - x[i-1])) % 2 == 1) dist = dist / 2 + 1;
        else dist /= 2;

        if(dist > max_dist) max_dist = dist;
    }
    printf("%d\n", max_dist);

    return 0;
}
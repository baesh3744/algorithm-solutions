#include <stdio.h>
#include <stdlib.h>

int comp(const void* left, const void* right) {
    if(((int*)left)[0] < ((int*)right)[0]) return -1;
    if(((int*)left)[0] > ((int*)right)[0]) return 1;
    if(((int*)left)[1] < ((int*)right)[1]) return -1;
    if(((int*)left)[1] > ((int*)right)[1]) return 1;
}

int main(void) {
    int N;
    int xy[100000][2];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) { scanf("%d %d", &xy[i][0], &xy[i][1]); }

    qsort(xy, N, sizeof(xy[0]), comp);
    for(int i = 0; i < N; i++) { printf("%d %d\n", xy[i][0], xy[i][1]); }

    return 0;
}
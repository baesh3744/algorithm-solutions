#include <stdio.h>
#include <stdlib.h>

double F[100000];

int comp(const void* left, const void* right) {
    if(*(double*)left < *(double*)right) return -1;
    if(*(double*)left > *(double*)right) return 1;
    return 0;
}

int binarySearch(double num, int left, int right) {
    if(left > right) return 0;

    int mid = (left + right) / 2;
    if(F[mid] < num) return binarySearch(num, mid+1, right);
    else return right - mid + 1 + binarySearch(num, left, mid-1);
}

int main(void) {
    int N;
    int cnt = 0;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%lf", &F[i]);
    }
    qsort(F, N, sizeof(double), comp);
    for(int i = 1; i < N; i++) {
        cnt += binarySearch(F[i]*9/10, 0, i-1);
    }
    printf("%d\n", cnt);

    return 0;
}
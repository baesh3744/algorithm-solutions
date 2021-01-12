#include <stdio.h>
#include <stdlib.h>

int comp(const void* left, const void* right) {
    if(*(int*)left > *(int*)right) return 1;
    if(*(int*)left < *(int*)right) return -1;
    return 0;
}

int main(void) {
    int N;
    int arr[1000];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) { scanf("%d", &arr[i]); }

    qsort(arr, N, sizeof(int), comp);
    for(int i = 0; i < N; i++) { printf("%d\n", arr[i]); }

    return 0;
}
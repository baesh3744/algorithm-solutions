#include <stdio.h>
#include <stdlib.h>

int comp(const void* left, const void* right) {
    if(*(int*)left > *(int*)right) return -1;
    if(*(int*)left < *(int*)right) return 1;
    return 0;
}

int main(void) {
    int N;
    int idx = 0;
    int arr[10];

    scanf("%d", &N);
    while(N > 0) {
        arr[idx++] = N % 10;
        N /= 10;
    }

    qsort(arr, idx, sizeof(int), comp);
    for(int i = 0; i < idx; i++) { printf("%d", arr[i]); }

    return 0;
}
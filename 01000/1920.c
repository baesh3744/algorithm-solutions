#include <stdio.h>

int A[100000];

void insertionSort(int N) {
    int i, j, key;
    for(i = 1; i < N; i++) {
        key = A[i];

        for(j = i-1; j >= 0 && A[j] > key; j--) {
            A[j+1] = A[j];
        }
        A[j+1] = key;
    }
}

int binarySearch(int num, int left, int right) {
    if(left > right) return 0;

    int mid = (left + right) / 2;
    if(A[mid] < num) {
        return binarySearch(num, mid+1, right);
    } else if(A[mid] > num) {
        return binarySearch(num, left, mid-1);
    } else {
        return 1;
    }
}

int main(void) {
    int N, M, num;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    insertionSort(N);
    
    scanf("%d", &M);
    for(int i = 0; i < M; i++) {
        scanf("%d", &num);
        printf("%d\n", binarySearch(num, 0, N-1));
    }

    return 0;
}
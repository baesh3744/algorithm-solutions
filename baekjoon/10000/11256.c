#include <stdio.h>

#define swap(a, b, tmp) ( (tmp)=(a), (a)=(b), (b)=(tmp) )

int partition(int arr[], int left, int right) {
    int tmp;
    int low = left + 1;
    int high = right;
    int pivot = arr[left];

    while(low <= high) {
        while(low <= high && arr[low] <= pivot) { low++; }
        while(low <= high && arr[high] >= pivot) { high--; }
        if(low < high) { swap(arr[low], arr[high], tmp); }
    }
    swap(arr[left], arr[high], tmp);

    return high;
}

void quickSort(int arr[], int left, int right) {
    if(left < right) {
        int pivot = partition(arr, left, right);
        quickSort(arr, left, pivot-1);
        quickSort(arr, pivot+1, right);
    }
}

int main(void) {
    int T, J, N, R, C, cnt;
    int box_size[1000];

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        cnt = 0;

        scanf("%d %d", &J, &N);
        for(int j = 0; j < N; j++) {
            scanf("%d %d", &R, &C);
            box_size[j] = R * C;
        }

        quickSort(box_size, 0, N-1);

        while(J > 0) {
            J -= box_size[N-1];
            N--; cnt++;
        }
        printf("%d\n", cnt);
    }

    return 0;
}
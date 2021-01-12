#include <stdio.h>

void merge(int arr[], int start, int mid, int end) {
    int idx = start;
    int first = start;
    int second = mid + 1;
    int tmp[14];
    
    while(first <= mid && second <= end) {
        if(arr[first] <= arr[second]) tmp[idx++] = arr[first++];
        else tmp[idx++] = arr[second++];
    }
    while(first <= mid) tmp[idx++] = arr[first++];
    while(second <= end) tmp[idx++] = arr[second++];
    for(int i = start; i <= end; i++) {
        arr[i] = tmp[i];
    }
}

void mergeSort(int arr[], int start, int end) {
    if(start < end) {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

void elimZero(int arr[], int N) {
    for(int j = 0; j < 2; j++) {
        if(arr[j] == 0) {
            for(int i = 1; i < N; i++) {
                if(arr[i] != 0) {
                    arr[j] = arr[i];
                    arr[i] = 0;
                    break;
                }
            }
        }
    }
}

int minSum(int arr[], int N) {
    int idx;
    int ret = 0;
    
    if(N % 2 == 1) {
        ret += arr[0];
        idx = 1;
    } else {
        ret += arr[0] + arr[1];
        idx = 2;
    }
    for( ; idx < N; idx += 2) {
        ret *= 10;
        ret += arr[idx] + arr[idx + 1];
    }

    return ret;
}

int main(void) {
    int N, ans;
    int arr[14];

    while(1) {
        scanf("%d", &N);
        
        if(N == 0) break;

        for(int i = 0; i < N; i++) {
            scanf("%d", &arr[i]);
        }

        mergeSort(arr, 0, N - 1);
        elimZero(arr, N);
        ans = minSum(arr, N);
        printf("%d\n", ans);
    }

    return 0;
}
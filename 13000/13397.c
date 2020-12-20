#include <stdio.h>

/*
 * solve - arr 배열을 각 구간 내 최대값과 최소값의 차이가 mid를 넘지 않도록 구간을 설정하였을 때,
 *         구간의 개수를 리턴한다.
 */
int solve(const int *arr, int N, int mid) {
    int min = 10001, max = 0, ret = 0;

    for(int i = 0; i < N; i++) {
        if(arr[i] < min) min = arr[i];
        if(max < arr[i]) max = arr[i];

        if(mid <= max-min) {
            min = arr[i]; max = arr[i];
            ret++;
        }
    }
    return ret + 1;
}

int main(void) {
    int N, M;
    int min = 10001, max = 0;
    int arr[5000];

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);

        if(arr[i] < min) min = arr[i];
        if(max < arr[i]) max = arr[i];
    }

    int left = 0;
    int right = max - min;
    while(left <= right) {
        int mid = (left + right) / 2;
        
        if(M < solve(arr, N, mid)) left = mid + 1;
        else right = mid - 1;
    }
    printf("%d\n", right);

    return 0;
}

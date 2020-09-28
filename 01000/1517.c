#include <stdio.h>

void merge(int *A, int left, int mid, int right, long long *ans) {
    int tmp[500001];
    int cnt = 0,
        idx = left, l_idx = left, r_idx = mid+1;
    
    while(l_idx <= mid || r_idx <= right) {
        if(mid < l_idx) {
            tmp[idx++] = A[r_idx++];
            cnt++;
        } else if(right < r_idx) {
            tmp[idx++] = A[l_idx++];
            *ans += (long long) cnt;
        } else if(A[l_idx] <= A[r_idx]) {
            tmp[idx++] = A[l_idx++];
            *ans += (long long) cnt;
        } else {
            tmp[idx++] = A[r_idx++];
            cnt++;
        }
    }
    for(int i = left; i <= right; i++) A[i] = tmp[i];
    return ;
}

void mergeSort(int *A, int left, int right, long long *ans) {
    if(left < right) {
        int mid = (left + right) / 2;
        mergeSort(A, left, mid, ans);
        mergeSort(A, mid+1, right, ans);
        merge(A, left, mid, right, ans);
    }
}

int main(void) {
    int N;
    long long ans = 0;
    int A[500001];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) scanf("%d", &A[i]);

    mergeSort(A, 0, N-1, &ans);

    printf("%lld\n", ans);

    return 0;
}

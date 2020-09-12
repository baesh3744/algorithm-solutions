#include <stdio.h>

void swap(int cit[], int idx1, int idx2) {
    int tmp = cit[idx1];
    cit[idx1] = cit[idx2];
    cit[idx2] = tmp;
}

int partition(int cit[], int start, int end) {
    int pivot = cit[start];
    int left = start + 1;
    int right = end;

    while(left <= right) {
        while(left <= right && cit[left] <= pivot) left++;
        while(left <= right && pivot < cit[right]) right--;
        if(left < right) swap(cit, left, right);
    }
    swap(cit, start, right);

    return right;
}

void qSort(int cit[], int start, int end) {
    if(start < end) {
        int pivot_idx = partition(cit, start, end);

        qSort(cit, start, pivot_idx - 1);
        qSort(cit, pivot_idx + 1, end);
    }
}

int main(void) {
    int n;
    int cit[1000];
    int ans = 0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &cit[i]);
    }

    qSort(cit, 0, n - 1);
    for(int i = n; 0 <= i; i--) {
        if(i <= cit[n - i]) {
            ans = i;
            break;
        }
    }
    printf("%d\n", ans);

    return 0;
}
#include <stdio.h>

void bubbleSort(int arr[], int L) {
    for(int i = 0; i <= L; i++) {
        for(int j = 0; j < L-i; j++) {
            if(arr[j] > arr[j+1]) {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
}

int main(void) {
    int L, N;
    int ls[50];
    int ans = 0;

    scanf("%d", &L);
    for(int i = 1; i <= L; i++) scanf("%d", &ls[i]);
    ls[0] = 0;
    scanf("%d", &N);

    bubbleSort(ls, L);
    for(int i = 0; ans == 0 && i <= L; i++) {
        if((i < L) && ls[i] < N && ls[i+1] > N) {
            int left = 0;
            int right = 0;

            for(int j = ls[i] + 1; j < N; j++) left++;
            for(int j = N + 1; j < ls[i+1]; j++) right++;

            ans = left * right + left + right;
        }
    }
    printf("%d\n", ans);

    return 0;
}
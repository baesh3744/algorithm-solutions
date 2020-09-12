#include <stdio.h>

char handle[100][21];
int idx_handle[100];

int compare(int idx1, int idx2) {
    int i;

    for(i = 0; handle[idx1][i] != '\0' && handle[idx2][i] != '\0'; i++) {
        if(handle[idx1][i] == handle[idx2][i]) continue;
        else if(handle[idx1][i] < handle[idx2][i]) return -1;
        else return 1;
    }
    if(handle[idx1][i] == '\0') return -1;
    if(handle[idx2][i] == '\0') return 1;
}

void iSortID(int N) {
    int j;

    for(int i = 1; i < N; i++) {
        int key = idx_handle[i];

        for(j = i - 1; 0 <= j; j--) {
            if(compare(idx_handle[j], key) == 1) idx_handle[j + 1] = idx_handle[j];
            else break;
        }
        idx_handle[j + 1] = key;
    }
}

int main(void) {
    int N, I;

    scanf("%d %d", &N, &I);
    for(int i = 0; i < N; i++) {
        scanf("%s", handle[i]);
        idx_handle[i] = i;
    }

    iSortID(N);

    printf("%s\n", handle[idx_handle[I - 1]]);

    return 0;
}
#include <stdio.h>

int pile[900][3];

void selectionSort(int N, int left, int right) {
    for(int i = 0; i < 3 * N; i++) {
        int idx = i;

        for(int j = i + 1; j < 3 * N; j++) {
            if(pile[j][0] < pile[idx][0]) idx = j;
            else if(pile[j][0] == pile[idx][0] && pile[j][1] < pile[idx][1]) idx = j;
        }

        for(int k = 0; k < 3; k++) {
            int tmp = pile[idx][k];
            pile[idx][k] = pile[i][k];
            pile[i][k] = tmp;
        }
    }
}

int main(void) {
    int N;

    scanf("%d", &N);
    for(int i = 0; i < 3 * N; i++) {
        scanf("%d %d", &pile[i][0], &pile[i][1]);
        pile[i][2] = i + 1;
    }

    selectionSort(N, 0, 3 * N - 1);

    for(int i = 0; i < 3 * N; i += 3) {
        printf("%d %d %d\n", pile[i][2], pile[i + 1][2], pile[i + 2][2]);
    }

    return 0;
}
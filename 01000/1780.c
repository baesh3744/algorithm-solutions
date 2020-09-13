#include <stdio.h>

#define MAX_N 2200
int arr[MAX_N][MAX_N], ans[3];

void paperCnt(int y, int x, int size) {
    int head = arr[y][x];

    for(int i = y; i < y + size; i++) {
        for(int j = x; j < x + size; j++) {
            if(arr[i][j] != head) {
                int next_size = size / 3;
                for(int k = 0; k < 3; k++) {
                    for(int l = 0; l < 3; l++) {
                        paperCnt(y + k * next_size, x + l * next_size, next_size);
                    }
                }
                return ;
            }
        }
    }

    if(head == -1) ans[0]++;
    else if(head == 0) ans[1]++;
    else ans[2]++;
    return ;
}

int main(void) {
    int N;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    paperCnt(0, 0, N);
    printf("%d\n%d\n%d\n", ans[0], ans[1], ans[2]);

    return 0;
}
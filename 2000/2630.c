#include <stdio.h>

#define MAX_N 128
int arr[MAX_N][MAX_N];
int white_cnt = 0;
int blue_cnt = 0;

void paperCnt(int y, int x, int size) {
    int head = arr[y][x];

    for(int i = y; i < y + size; i++) {
        for(int j = x; j < x + size; j++) {
            if(arr[i][j] != head) {
                int next_size = size / 2;
                int next_x = x + next_size;
                int next_y = y + next_size;
                
                paperCnt(y, x, next_size);
                paperCnt(y, next_x, next_size);
                paperCnt(next_y, x, next_size);
                paperCnt(next_y, next_x, next_size);
                return ;
            }
        }
    }

    if(head == 0) white_cnt++;
    else blue_cnt++;
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
    printf("%d\n%d\n", white_cnt, blue_cnt);
    
    return 0;
}
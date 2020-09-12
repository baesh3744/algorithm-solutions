#include <stdio.h>

#define SIZE 500

int main(void) {
    int R, C;
    int ans = 1;
    int mv_x[] = {1, 0, -1, 0};
    int mv_y[] = {0, -1, 0, 1};
    char board[SIZE][SIZE];

    scanf("%d %d", &R, &C);
    for(int i = 0; i < R; i++) {
        scanf("%s", board[i]);
    }

    for(int i = 0; ans == 1 && i < R; i++) {
        for(int j = 0; ans == 1 && j < C; j++) {
            if(board[i][j] == 'S') {
                for(int k = 0; ans == 1 && k < 4; k++) {
                    int new_i = i + mv_x[k];
                    int new_j = j + mv_y[k];

                    if(new_i < 0 || new_i >= R || new_j < 0 || new_j >= C) continue;
                    
                    if(board[new_i][new_j] == 'W') ans = 0;
                    else if(board[new_i][new_j] == '.') board[new_i][new_j] = 'D';
                }
            }
        }
    }

    printf("%d\n", ans);
    if(ans == 1) {
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                printf("%c", board[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
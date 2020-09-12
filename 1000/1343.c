#include <stdio.h>
#include <string.h>

int main(void) {
    int idx, len;
    int can = 1;
    char board[501], poli[501];

    scanf("%s", board);

    len = strlen(board);
    for(idx = 0; (can == 1) && (idx < len); idx++) {
        if(board[idx] == 'X') {
            if(idx + 1 < len && board[idx + 1] == 'X') {
                if((idx + 2 < len && board[idx + 2] == 'X') && (idx + 3 < len && board[idx + 3] == 'X')) {
                    poli[idx] = 'A';
                    poli[idx + 1] = 'A';
                    poli[idx + 2] = 'A';
                    poli[idx + 3] = 'A';
                    idx += 3;
                } else {
                    poli[idx] = 'B';
                    poli[idx + 1] = 'B';
                    idx += 1;
                }
            } else {
                can = -1;
            }
        } else {
            poli[idx] = '.';
        }
    }

    poli[idx] = '\0';
    if(can == 1) printf("%s\n", poli);
    else printf("-1\n");

    return 0;
}
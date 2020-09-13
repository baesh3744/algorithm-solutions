#include <stdio.h>
#include <string.h>

char king[3], stone[3], tmp_king[3], tmp_stone[3];
int move_int_x[] = {1, -1, 0, 0, 1, -1, 1, -1};
int move_int_y[] = {0, 0, -1, 1, 1, 1, -1, -1};

int checkRange(char *pos) {
    if('A' <= pos[0] && pos[0] <= 'H' && '1' <= pos[1] && pos[1] <= '8') return 1;
    return -1;
}

void moveKing(int j) {
    strcpy(tmp_king, king);
    strcpy(tmp_stone, stone);

    tmp_king[0] += move_int_x[j];
    tmp_king[1] += move_int_y[j];
    if(checkRange(tmp_king) == -1) return ;

    if(strcmp(tmp_king, tmp_stone) != 0) {
        strcpy(king, tmp_king);
        return ;
    }
    
    tmp_stone[0] += move_int_x[j];
    tmp_stone[1] += move_int_y[j];
    if(checkRange(tmp_stone) == -1) return ;
    
    strcpy(king, tmp_king);
    strcpy(stone, tmp_stone);
    return ;
}

int main(void) {
    char move[50][3];
    char info[][3] = {"R", "L", "B", "T", "RT", "LT", "RB", "LB"};
    int N;

    scanf("%s %s", king, stone);
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%s", move[i]);
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < 8; j++) {
            if(strcmp(info[j], move[i]) == 0) {
                moveKing(j);
                break;
            }
        }
    }
    printf("%s\n%s\n", king, stone);

    return 0;
}
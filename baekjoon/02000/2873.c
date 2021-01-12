#include <stdio.h>

/*
 * findMinIdx - R과 C가 모두 짝수일 때, 제외될 수 있는 칸 중 가장 작은 값의 인덱스를 구한다.
 */
void findMinIdx(int happy[][1000], int R, int C, int *min_i, int *min_j) {
    int min_happy = 10000;
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(((i+j) % 2 == 1) && (happy[i][j] < min_happy)) {
                min_happy = happy[i][j];
                *min_i = i;
                *min_j = j;
            }
        }
    }
}

/*
 * scanSquare - start부터 end까지 type에 따라 좌우 또는 상하로 이동하며 출력한다.
 * 
 * @param   type    'R' 좌우로 이동하며 출력하고, 한 칸 아래로 이동한다.
 *                  'D' 상하로 이동하며 출력하고, 한 칸 오른쪽으로 이동한다.
 * @param   move    1   오른쪽 또는 아래로 이동한다.
 *                  0   왼쪽 또는 위로 이동한다.
 * @return  1   출력을 한 경우
 *          0   출력을 하지 않은 경우
 */
int scanSquare(char type, int start, int end, int length, int move) {
    char ch, one, zero, next;
    int ret = 0;

    if(type == 'R') {
        one = 'R'; zero = 'L'; next = 'D';
    } else if(type == 'D') {
        one = 'D'; zero = 'U'; next = 'R';
    }

    for(int i = start; i < end; i++) {
        ret = 1;
        ch = (move == 1 ? one : zero);
        for(int j = 1; j < length; j++) printf("%c", ch);
        if(i != end-1) printf("%c", next);
        move = (move == 1 ? 0 : 1);
    }
    return ret;
}

/*
 * R-홀         오 -> 아1 -> 왼 -> 아1 -> 오
 * R-짝 C-홀    아 -> 오1 -> 위 -> 오1 -> 아
 * R-짝 C-짝    i+j가 홀수인 곳 중 한 곳을 갈 수 없다.
 *              min_i가 짝수    min_i번째 줄 왼쪽 위 -> 오른쪽 아래
 *              min_i가 홀수    min_i가 마지막 줄이 아닐 때     min_i번째 줄 오른쪽 위 -> 왼쪽 아래
 *                              min_i가 마지막 줄일 때          min_i번째 줄 왼쪽 위 -> 오른쪽 아래
 */
int main(void) {
    int R, C, min_i, min_j;
    int happy[1000][1000];

    scanf("%d %d", &R, &C);
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            scanf("%d", &happy[i][j]);
        }
    }

    if(R % 2 == 1) {
        scanSquare('R', 0, R, C, 1);
    } else if(C % 2 == 1) {
        scanSquare('D', 0, C, R, 1);
    } else {
        findMinIdx(happy, R, C, &min_i, &min_j);
        
        if(min_i % 2 == 0) {
            if(scanSquare('R', 0, min_i, C, 1) == 1) printf("D");

            printf("DR");
            int j = 1;
            while(j < C-1) {
                if(j < min_j) printf("URDR");
                else printf("RURD");
                j += 2;
            }
            
            if(min_i+2 < R-1) {
                printf("D");
                scanSquare('R', min_i+2, R, C, 0);
            }
        } else if(min_i != R-1) {
            if(scanSquare('R', 0, min_i, C, 1) == 1) printf("D");
            
            printf("DL");
            int j = C-2;
            while(j > 0) {
                if(j > min_j) printf("ULDL");
                else printf("LULD");
                j -= 2;
            }

            if(min_i+2 < R) {
                printf("D");
                scanSquare('R', min_i+2, R, C, 1);
            }
        } else {
            if(scanSquare('D', 0, min_j, R, 1) == 1) printf("R");
            printf("RD");

            int i = 1;
            while(i < R-1) {
                printf("LDRD");
                i += 2;
            }

            if(min_j+2 < C-1) {
                printf("R");
                scanSquare('D', min_j+2, C, R, 0);
            }
        }
    }
    printf("\n");
    return 0;
}

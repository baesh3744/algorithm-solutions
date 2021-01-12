#include <stdio.h>

/*
 * printStars - stars 배열을 출력한다.
 */
void printStars(char (*stars)[2188], int N) {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            printf("%c", stars[i][j]);
        }
        printf("\n");
    }
}

/*
 * makePatterns - stars 배열을 규칙에 따라 빈 칸을 뚫어준다.
 */
void makePatterns(char (*stars)[2188], int N, int i, int j) {
    if(N == 3) {
        stars[i+1][j+1] = ' ';
        return ;
    }

    int next_N = N / 3;
    for(int k = 0; k < 3; k++) {
        for(int l = 0; l < 3; l++) {
            if(k == 1 && l == 1) {
                for(int m = 0; m < next_N; m++) {
                    for(int n = 0; n < next_N; n++) {
                        stars[i+next_N+m][j+next_N+n] = ' ';
                    }
                }
            } else {
                makePatterns(stars, next_N, i+next_N*k, j+next_N*l);
            }
        }
    }
    return ;
}

/*
 * initStars - stars 배열을 *로 채운다.
 */
void initStars(char (*stars)[2188], int N) {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            stars[i][j] = '*';
        }
    }
}

int main(void) {
    int N;
    char stars[2188][2188];

    scanf("%d", &N);

    initStars(stars, N);

    makePatterns(stars, N, 1, 1);
    
    printStars(stars, N);
    return 0;
}

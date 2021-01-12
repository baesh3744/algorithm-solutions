#include <stdio.h>
#include <string.h>

#define HEIGHT 3100
#define SIZE 193

/*
 * isStar - stars 배열의 (i, j)의 k번째 비트가 별인지를 판단한다.
 */
int isStar(int (*stars)[SIZE], int i, int j, int k) {
    return (stars[i][j] >> (32 - k)) & 1;
}

/*
 * printStars - 별을 출력한다.
 */
void printStars(int (*stars)[SIZE], int N) {
    int base = 2 * N - 1;
    for(int i = 1; i <= N; i++) {
        // 32bit가 모두 사용되는 int 출력
        for(int j = 0; j < base/32; j++) {
            for(int k = 1; k <= 32; k++) {
                if(isStar(stars, i, j, k) == 1) printf("*");
                else printf(" ");
            }
        }

        // 32bit 중 일부만 사용되는 int 출력
        for(int k = 1; k <= base%32; k++) {
            if(isStar(stars, i, base/32, k) == 1) printf("*");
            else printf(" ");
        }
        printf("\n");
    }
}

/*
 * makePatterns - 규칙에 맞게 별을 표시한다. 이때 별은 한 비트에 1로 표시한다.
 */
void makePatterns(int (*stars)[SIZE], int N, int i, int j) {
    // 높이 3의 기본 삼각형
    if(N == 3) {
        int set[][2] = {{i, j},
                        {i+1, j-1}, {i+1, j+1},
                        {i+2, j-2}, {i+2, j-1}, {i+2, j}, {i+2, j+1}, {i+2, j+2}};
        for(int k = 0; k < 8; k++) {
            int stars_i = set[k][0];
            int stars_j = set[k][1] / 32;
            int bit_move = 31 - set[k][1] % 32;
            stars[stars_i][stars_j] |= (1 << bit_move);
        }
        return ;
    }

    int next_N = N / 2;
    makePatterns(stars, next_N, i, j);
    makePatterns(stars, next_N, i+next_N, j-next_N);
    makePatterns(stars, next_N, i+next_N, j+next_N);
}

int main(void) {
    int N;
    int stars[HEIGHT][SIZE];

    scanf("%d", &N);
    memset(stars, 0, sizeof(int) * HEIGHT * SIZE);

    makePatterns(stars, N, 1, N-1);

    printStars(stars, N);

    return 0;
}

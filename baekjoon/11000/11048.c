#include <stdio.h>
#include <string.h>

#define max_maze 1001

int N, M;
int cache[max_maze][max_maze];
int maze[max_maze][max_maze];

/*
 * isRange - (n, m)이 미로 안에 위치하는지 확인한다.
 * @return  1   미로 안에 위치한다.
 *          0   미로의 범위를 벗어난다.
 */
int isRange(int n, int m) {
    return (0 < n && n <= N && 0 < m && m <= M);
}

/*
 * dp - (1, 1)에서 (n, m)으로 이동하면서 가져올 수 있는 사탕 개수의 최댓값을 구한다.
 * @return  사탕 개수의 최댓값
 */
int dp(int n, int m) {
    if(!isRange(n, m)) return 0;
    if(n == 1 && m == 1) return maze[n][m];
    if(cache[n][m] != -1) return cache[n][m];

    int ret = 0;
    int move_n[3] = {-1, 0, -1};
    int move_m[3] = {0, -1, -1};
    for(int i = 0; i < 3; i++) {
        int new = maze[n][m] + dp(n+move_n[i], m+move_m[i]);
        ret = (ret > new ? ret : new);
    }
    return (cache[n][m] = ret);
}

int main(void) {
    scanf("%d %d", &N, &M);

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            scanf("%d", &maze[i][j]);
        }
    }

    memset(cache, -1, sizeof(int)*max_maze*max_maze);
    printf("%d\n", dp(N, M));
    return 0;
}

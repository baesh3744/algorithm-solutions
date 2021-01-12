#include <stdio.h>

#define OVER_VAL 20000000
#define min(a, b) (a < b ? a : b)

int cache[66000][16];

/*
 * tsp - 외판원의 순회에 필요한 최소 비용을 구한다.
 * 
 * @param   W       이동하는데 드는 비용 행렬
 * @param   N       도시의 개수
 * @param   visited 도시의 방문여부를 비트마스크로 표현(1 - 방문o, 0 - 방문x)
 * @param   cur     현재 도시의 인덱스
 * @return  최소 비용
 */
int tsp(int W[][16], int N, int visited, int cur) {
    int next_bit;
    int ret = OVER_VAL;;

    // 기저 사례: 모든 도시를 방문한 경우, 최초의 도시(0번째)로 이동
    if(visited == (1<<N)-1) return (W[cur][0] == 0 ? OVER_VAL : W[cur][0]);
    if(cache[visited][cur] != 0) return cache[visited][cur];
    
    // 방문하지 않은 도시를 순회
    for(int next = 1; next < N; next++) {
        next_bit = 1<<next;
        if(W[cur][next] != 0 && ((visited & next_bit) == 0)) {
            ret = min(ret, W[cur][next] + tsp(W, N, visited | next_bit, next));
        }
    }
    return (cache[visited][cur] = ret);
}

int main(void) {
    int N;
    int chk[16] = { 0, };
    int W[16][16];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%d", &W[i][j]);
        }
    }

    printf("%d\n", tsp(W, N, 1, 0));
    
    return 0;
}
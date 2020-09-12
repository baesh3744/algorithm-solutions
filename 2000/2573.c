#include <stdio.h>

int N, M;
int map[300][300], chk[300][300], minus[300][300];
int move_i[] = {0, 1, 0, -1};
int move_j[] = {1, 0, -1, 0};

int isRange(int i, int j) {
    return (0 <= i && i < N && 0 <= j && j < M);
}

int afterOneYear(int cnt) {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            minus[i][j] = 0;

            if(map[i][j] != 0) {
                for(int idx = 0; idx < 4; idx++) {
                    int next_i = i + move_i[idx];
                    int next_j = j + move_j[idx];

                    if(isRange(next_i, next_j) == 1 && map[next_i][next_j] == 0) {
                        minus[i][j]++;
                    }
                }
            }
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(minus[i][j] != 0) {
                map[i][j] -= minus[i][j];
                if(map[i][j] < 0) map[i][j] = 0;
                if(map[i][j] == 0) cnt--;
            }
        }
    }

    return cnt;
}

int dfs(int i, int j, int year) {
    chk[i][j] = year;
    
    int ret = 1;
    for(int idx = 0; idx < 4; idx++) {
        int next_i = i + move_i[idx];
        int next_j = j + move_j[idx];

        if(isRange(next_i, next_j) == 1 && map[next_i][next_j] > 0 && chk[next_i][next_j] != year) {
            ret += dfs(next_i, next_j, year);
        }
    }
    return ret;
}

int countLump(int year, int cnt) {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(map[i][j] > 0) {
                if(dfs(i, j, year) != cnt) return 2;
                else return 1;
            }
        }
    }
}

int main(void) {
    int cnt = 0;
    int year = 0;
    int found = 1;

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            scanf("%d", &map[i][j]);
            if(map[i][j] != 0) cnt++;
        }
    }
    
    while(found == 1) {
        if((cnt = afterOneYear(cnt)) == 0) break;
        
        if(countLump(++year, cnt) == 2) {
            printf("%d\n", year);
            found = 0;
        }
    }
    if(found == 1) printf("0\n");

    return 0;
}
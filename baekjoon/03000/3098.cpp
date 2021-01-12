#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

#define SIZE 51

int main(void) {
    int N, M, A, B;
    int map[SIZE][SIZE];
    int day = 1;
    int cnt = 0;
    vector<int> ans;

    memset(map, 0, sizeof(int) * SIZE * SIZE);
    scanf("%d %d", &N, &M);
    for(int i = 0; i < M; i++) {
        scanf("%d %d", &A, &B);
        map[A][B] = day;
        map[B][A] = day;
        cnt += 1;
    }

    while(1) {
        int one_day_cnt = 0;
        day += 1;

        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                if(i != j && 0 < map[i][j] && map[i][j] < day) {
                    for(int k = 1; k <= N; k++) {
                        if(i != k && 0 < map[j][k] && map[j][k] < day && map[i][k] == 0) {
                            map[i][k] = day;
                            map[k][i] = day;
                            one_day_cnt += 1;
                        }
                    }
                }
            }
        }

        ans.push_back(one_day_cnt);
        cnt += one_day_cnt;
        
        if(cnt == N * (N-1) / 2) break;
    }
    
    printf("%d\n", day - 1);
    for(int i = 0; i < ans.size(); i++) {
        printf("%d\n", ans[i]);
    }

    return 0;
}
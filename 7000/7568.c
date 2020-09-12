#include <stdio.h>

int main(void) {
    int N, cnt;
    int rank[50], wandh[50][2];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) { scanf("%d %d", &wandh[i][0], &wandh[i][1]); }
    
    for(int i = 0; i < N; i++) {
        cnt = 0;
        
        for(int j = 0; j < N; j++) {
            if(i == j) continue;

            if(wandh[i][0] < wandh[j][0] && wandh[i][1] < wandh[j][1]) cnt++;
        }

        rank[i] = cnt + 1;
    }

    for(int i = 0; i < N; i++) { printf("%d ", rank[i]); }

    return 0;
}
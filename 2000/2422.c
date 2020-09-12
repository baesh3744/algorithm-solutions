#include <stdio.h>

#define ICE_NUM 201

int main(void) {
    int N, M, ice1, ice2;
    int cnt = 0;
    int noMatch[ICE_NUM][ICE_NUM];

    scanf("%d %d", &N, &M);
    for(int i = 0; i < M; i++) {
        scanf("%d %d", &ice1, &ice2);
        noMatch[ice1][ice2] = -1;
        noMatch[ice2][ice1] = -1;
    }

    for(int i = 1; i <= N-2; i++) {
        for(int j = i+1; j <= N-1; j++) {
            if(noMatch[i][j] == -1) continue;
            for(int k = j+1; k <= N; k++) {
                if(noMatch[j][k] == -1 || noMatch[i][k] == -1) continue;
                cnt++;
            }
        }
    }
    printf("%d\n", cnt);

    return 0;
}
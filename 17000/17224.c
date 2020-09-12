#include <stdio.h>

int main(void) {
    int N, L, K;
    int sub[100][2];
    int max_score = 0;

    scanf("%d %d %d", &N, &L, &K);
    for(int i = 0; i < N; i++) {
        scanf("%d %d", &sub[i][0], &sub[i][1]);
    }

    for(int i = 0; K > 0 && i < N; i++) {
        if(sub[i][0] <= L && sub[i][1] <= L) {
            max_score += 140;
            K--;
            sub[i][0] = L + 1;
        }
    }
    for(int i = 0; K > 0 && i < N; i++) {
        if(sub[i][0] <= L) {
            max_score += 100;
            K--;
        }
    }
    printf("%d\n", max_score);

    return 0;
}
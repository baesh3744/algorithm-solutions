#include <stdio.h>

int score[10][2];

void sortScore() {
    int idx;

    for(int type = 0; type < 2; type++) {
        for(int i = 0; i < 9; i++) {
            idx = i;
            for(int j = idx + 1; j < 10; j++) {
                if(score[idx][type] < score[j][type]) idx = j;
            }
            if(idx != i) {
                int tmp = score[idx][type];
                score[idx][type] = score[i][type];
                score[i][type] = tmp;
            }
        }
    }
}

int main(void) {
    int ans;

    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 10; j++) {
            scanf("%d", &score[j][i]);
        }
    }

    sortScore();

    for(int i = 0; i < 2; i++) {
        ans = 0;
        for(int j = 0; j < 3; j++) {
            ans += score[j][i];
        }
        printf("%d ", ans);
    }
    
    return 0;
}
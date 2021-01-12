#include <stdio.h>

int N;
char frnd_map[50][51];

int count2Friends(int idx) {
    int ret = 0;
    int check[50] = { 0, };

    for(int j = 0; j < N; j++) {
        if(frnd_map[idx][j] == 'Y') {
            check[j] = 1;
            for(int k = 0; k < N; k++) {
                if(idx != k && frnd_map[j][k] == 'Y') {
                    check[k] = 1;
                }
            }
        }
    }
    
    for(int j = 0; j < N; j++) {
        if(check[j] == 1) ret++;
    }
    return ret;
}

int main(void) {
    int cnt;
    int ans = 0;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%s", frnd_map[i]);
    }
    
    for(int i = 0; i < N; i++) {
        if((cnt = count2Friends(i)) > ans) ans = cnt;
    }
    printf("%d\n", ans);

    return 0;
}
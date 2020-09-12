#include <stdio.h>
#include <string.h>

int main(void) {
    int N, a, cnt;
    char num[1001];

    memset(num, 1, sizeof(num));
    num[1] = 0;
    for(int i = 2; i < 1001; i++) {
        if(num[i] == 0) continue;
        for(int j = i + 1; j < 1001; j++) {
            if(j % i == 0) num[j] = 0;
        }
    }

    scanf("%d", &N);

    cnt = 0;
    for(int i = 0; i < N; i++) {
        scanf("%d", &a);
        if(num[a] == 1) cnt++;
    }

    printf("%d", cnt);

    return 0;
}
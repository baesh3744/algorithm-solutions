#include <stdio.h>

int main(void) {
    int N, tmp;
    int cnt = 0;
    int num = 0;

    scanf("%d", &N);

    while(1) {
        num++;
        tmp = N - num * (num + 1) / 2;
        
        if(tmp < 0) break;
        if(tmp % num == 0) cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}
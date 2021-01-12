#include <stdio.h>

int main(void) {
    int N, tmp;
    int ans = 665, cnt = 0;

    scanf("%d", &N);

    while(cnt != N) {
        ans++;
        tmp = ans;

        while(tmp > 0) {
            if(tmp % 1000 == 666) {
                cnt++;
                break;
            }
            tmp /= 10;
        }
    }
    printf("%d\n", ans);

    return 0;
}
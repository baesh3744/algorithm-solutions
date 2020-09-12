#include <stdio.h>

int makeList(int left, int right, int type) {
    int tmp;
    int ret = 2;

    if(type == 1) printf("%d %d ", left, right);
    while((tmp = left - right) >= 0) {
        left = right;
        right = tmp;
        ret++;
        if(type == 1) printf("%d ", right);
    }

    return ret;
}

int main(void) {
    int num, ans, cnt;
    int max = 0;

    scanf("%d", &num);
    for(int cur = num/2; cur <= num; cur++) {
        if((cnt = makeList(num, cur, 0)) > max) {
            max = cnt;
            ans = cur;
        }
    }
    printf("%d\n", max);
    makeList(num, ans, 1);

    return 0;
}
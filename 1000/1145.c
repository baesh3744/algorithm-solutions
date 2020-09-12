#include <stdio.h>

#define min(a, b) (a < b ? a : b)

int mostMultiples(int num1, int num2, int num3) {
    int ret = num1;

    while(1) {
        if((ret % num2 == 0) && (ret % num3 == 0)) break;
        ret += num1;
    }

    return ret;
}

int main(void) {
    int num[5];
    int ans = 1000000;

    for(int i = 0; i < 5; i++) {
        scanf("%d", &num[i]);
    }

    for(int i = 0; i < 3; i++) {
        for(int j = i + 1; j < 4; j++) {
            for(int k = j + 1; k < 5; k++) {
                ans = min(ans, mostMultiples(num[i], num[j], num[k]));
            }
        }
    }
    printf("%d", ans);

    return 0;
}
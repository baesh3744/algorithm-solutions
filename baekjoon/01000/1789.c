#include <stdio.h>

int main(void) {
    unsigned int num, current;
    int ans = 0;

    scanf("%u", &num);

    current = num;
    while(1) {
        ans++;
        num -= ans;
        if(num > current) break;
        current = num;
    }

    printf("%d\n", ans - 1);

    return 0;
}
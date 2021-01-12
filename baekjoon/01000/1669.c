#include <stdio.h>
#include <math.h>

int main(void) {
    int X, Y;
    scanf("%d %d", &X, &Y);

    int diff = Y - X;
    int num = (int)ceil(sqrt((double)diff));

    int ans;
    if(diff == 0) {
        ans = 0;
    } else if(diff <= num*(num-1)) {
        ans = 2 * num - 2;
    } else {
        ans = 2 * num - 1;
    }
    printf("%d\n", ans);
    return 0;
}

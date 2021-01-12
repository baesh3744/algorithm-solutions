#include <stdio.h>
#include <math.h>

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int x, y;
        scanf("%d %d", &x, &y);

        int dist = y - x;
        int num = (int)ceil(sqrt(dist));
        int move = 2 * num - 1;
        if(dist <= num*(num-1)) printf("%d\n", move-1);
        else printf("%d\n", move);
    }
    return 0;
}

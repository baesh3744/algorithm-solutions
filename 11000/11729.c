#include <stdio.h>

/*
 * printMove - 원판의 이동을 출력한다.
 */
void printMove(int num, int from, int to) {
    if(num == 1) {
        printf("%d %d\n", from, to);
        return ;
    }

    int last = 6 - from - to;

    printMove(num-1, from, last);
    printf("%d %d\n", from, to);
    printMove(num-1, last, to);
    return ;
}

int main(void) {
    int N, K;

    scanf("%d", &N);

    K = (1 << N) - 1;
    printf("%d\n", K);
    printMove(N, 1, 3);
    return 0;
}
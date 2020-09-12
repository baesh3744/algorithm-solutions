#include <stdio.h>

int main(void) {
    int A, B, N;

    scanf("%d %d %d", &A, &B, &N);

    A %= B;
    while(N > 0) {
        A *= 10;
        N -= 1;
        if(N == 0) printf("%d\n", A / B);
        else A %= B;
    }

    return 0;
}
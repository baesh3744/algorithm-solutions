#include <stdio.h>

int main(void) {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int A, B, GCD;

        scanf("%d %d", &A, &B);

        GCD = A < B ? A : B;

        while(1) {
            if((A % GCD == 0) && (B % GCD == 0)) break;
            GCD--;
        }

        printf("%d\n", A * B / GCD);
    }

    return 0;
}
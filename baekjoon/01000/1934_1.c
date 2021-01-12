#include <stdio.h>

int gcd(int A, int B) {
    return B ? gcd(B, A % B) : A;
}

int main(void) {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int A, B;

        scanf("%d %d", &A, &B);

        printf("%d\n", A * B / gcd(A, B));
    }

    return 0;
}
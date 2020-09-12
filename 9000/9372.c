#include <stdio.h>

int main(void) {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N, M, plane1, plane2;

        scanf("%d %d", &N, &M);
        for(int j = 0; j < M; j++) {
            scanf("%d %d", &plane1, &plane2);
        }

        printf("%d\n", N - 1);
    }

    return 0;
}
#include <stdio.h>

int main(void) {
    int N, M, K, last, start_print;
    int end_print = 1;

    scanf("%d %d %d", &N, &M, &K);

    if((M + K - 1 > N) || (M * K < N)) {
        printf("-1\n");
    } else {
        last = N;
        
        while((0 < last) && (last - (K-1) >= M)) {
            start_print = end_print + (K-1);
            for(int i = start_print; end_print <= i; i--) {
                printf("%d ", i);
            }
            end_print = start_print + 1;
            last -= K;
            M -= 1;
        }

        start_print = end_print + (last - M);
        for(int i = start_print; end_print <= i; i--) {
            if(i <= N) printf("%d ", i);
        }
        end_print = start_print + 1;

        for(int i = end_print; i <= N; i++) {
            printf("%d ", i);
        }

        printf("\n");
    }
    return 0;
}

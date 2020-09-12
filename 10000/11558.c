#include <stdio.h>
#include <string.h>

#define SIZE 10001

int main(void) {
    int T, N, K, cur;
    int A[SIZE], check[SIZE];

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        scanf("%d", &N);
        for(int j = 0; j < N; j++) {
            scanf("%d", &A[j+1]);
        }

        K = 0;
        cur = 1;
        memset(check, 0, sizeof(int) * SIZE);
        while(1) {
            if(cur == N) break;

            int next_cur = A[cur];
            
            if(check[next_cur] == 1) {
                K = 0;
                break;
            }

            K += 1;
            check[next_cur] = 1;
            cur = next_cur;
        }

        printf("%d\n", K);
    }

    return 0;
}
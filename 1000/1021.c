#include <stdio.h>

int main(void) {
    int N, M, lcnt, rcnt, go;
    int circular_queue[50], pick[50];
    int idx = 1;
    int ans = 0;

    scanf("%d %d", &N, &M);
    for(int i = 0; i < M; i++) {
        scanf("%d", &pick[i]);
    }
    for(int i = 1; i <= N; i++) {
        circular_queue[i] = i;
    }

    for(int i = 0; i < M; i++) {
        go = 1;
        lcnt = 0;

        for(int j = 0; go == 1 && j < N; j++) {
            if(idx > N) idx = 1;

            if(circular_queue[idx] == pick[i]) {
                rcnt = N - i - lcnt;
                go = 0;
                circular_queue[idx] = 0;

                if(rcnt < lcnt) ans += rcnt;
                else ans += lcnt;
            } else if(circular_queue[idx] != 0) {
                lcnt++;
            }
            idx += 1;
        }
    }
    printf("%d\n", ans);

    return 0;
}
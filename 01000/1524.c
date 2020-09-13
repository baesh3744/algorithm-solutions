#include <stdio.h>



int main(void) {
    int T, N, M, sj, sb, max_sj, max_sb;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        max_sj = 0;
        max_sb = 0;

        scanf("%d %d", &N, &M);
        for(int j = 0; j < N; j++) {
            scanf("%d", &sj);
            if(sj > max_sj) max_sj = sj;
        }
        for(int j = 0; j < M; j++) {
            scanf("%d", &sb);
            if(sb > max_sb) max_sb = sb;
        }

        if(max_sb > max_sj) printf("B\n");
        else printf("S\n");
    }

    return 0;
}
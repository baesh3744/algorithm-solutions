#include <stdio.h>

int main(void) {
    int N, M, max;
    int idx = 0, sum_hd = 0;
    int cnt[4];
    char dna[1005][55], ans[55];
    char acgt[4] = {'A', 'C', 'G', 'T'};

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        scanf("%s", dna[i]);
    }

    for( ; idx < M; idx++) {
        max = 0;
        for(int i = 0; i < 4; i++) {
            cnt[i] = 0;
        }

        for(int i = 0; i < N; i++) {
            if(dna[i][idx] == 'A') cnt[0]++;
            else if(dna[i][idx] == 'C') cnt[1]++;
            else if(dna[i][idx] == 'G') cnt[2]++;
            else cnt[3]++;
        }

        for(int i = 0; i < 4; i++) {
            max = max > cnt[i] ? max : cnt[i];
        }

        for(int i = 0; i < 4; i++) {
            if(max == cnt[i]) {
                ans[idx] = acgt[i];
                sum_hd += N - max;
                break;
            }
        }
    }
    ans[idx] = '\0';
    printf("%s\n%d\n", ans, sum_hd);

    return 0;
}
#include <stdio.h>
#include <string.h>

int cache[51][1001];

int dp(int b, int m) {
    if(m == 0) return 0;
    if(m == 1) return 1;
    if(b == 1) return m;
    if(cache[b][m]) return cache[b][m];

    int* ret = &cache[b][m];
    *ret = 1000;
    for(int drop_m = 0; drop_m < m; drop_m++) {
        int broken_case = dp(b-1, drop_m) + 1;
        int not_broken_case = dp(b, m - drop_m - 1) + 1;
        int worst_case = broken_case > not_broken_case ? broken_case : not_broken_case;
        
        *ret = *ret > worst_case ? worst_case : *ret;
    }
    return *ret;
}

int main(void) {
    int P;
    scanf("%d", &P);

    for(int i = 0; i < P; i++) {
        int B, M;
        scanf("%d %d", &B, &M);

        memset(cache, 0, sizeof(int) * 51 * 1001);
        printf("%d\n", dp(B, M));
    }
    return 0;
}

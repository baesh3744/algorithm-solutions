#include <stdio.h>
#include <string.h>

int main(void) {
    char dec[1000001];

    memset(dec, 1, sizeof(dec));
    dec[1] = 0;
    for(int i = 2; i <= 500000; i++) {
        if(dec[i] == 0) continue;
        for(int j = 2 * i; j <= 1000001; j += i) {
            dec[j] = 0;
        }
    }

    while(1) {
        int n, found;

        scanf("%d", &n);

        if(n == 0) break;

        found = 0;
        for(int i = 3; i <= n / 2; i += 2) {
            if((dec[i] == 1) && (dec[n - i] == 1)) {
                printf("%d = %d + %d\n", n, i, n - i);
                found = 1;
                break;
            }
        }
        if(!found) printf("Goldbach's conjecture is wrong.\n");
    }

    return 0;
}
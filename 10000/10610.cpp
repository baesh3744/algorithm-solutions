#include <stdio.h>
#include <algorithm>
using namespace std;

bool compare(int a, int b) {
    return a > b;
}

int main(void) {
    int idx;
    int have_zero = 0, sum = 0;
    int N[100000];
    char in[100001];

    scanf("%s", in);
    
    for(idx = 0; in[idx] != '\0'; idx++) {
        N[idx] = in[idx] - '0';

        sum += N[idx];
        if(N[idx] == 0) have_zero = 1;
    }

    if((have_zero == 0) || (sum % 3 != 0)) {
        printf("-1\n");
    } else {
        sort(N, N+idx, compare);
        for(int i = 0; i < idx; i++) {
            printf("%d", N[i]);
        }
        printf("\n");
    }
    return 0;
}
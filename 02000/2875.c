#include <stdio.h>

int main(void) {
    int N, M, K, team;
    int last = 0;

    scanf("%d %d %d", &N, &M, &K);

    team = N/2 < M ? N/2 : M;
    K -= (N - 2*team) + (M - team);
    
    if(K < 0) K = 0;
    else if(K % 3 == 0) K = K /3;
    else K = K / 3 + 1;
    
    printf("%d\n", team - K);
    return 0;
}
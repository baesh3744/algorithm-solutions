#include <stdio.h>

/*
 * solve - len배열을 합이 mid가 넘지 않도록 그룹을 만들었을 때, 그룹의 개수를 리턴한다.
 */
int solve(const int *len, int N, int mid) {
    int sum = 0, ret = 0;

    for(int i = 0; i < N; i++) {
        sum += len[i];
        if(sum > mid) {
            sum = len[i];
            ret++;
        }
    }
    return ret + 1;
}

int main(void) {
    int N, M;
    int left = 0, right = 0;
    int len[100000];

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++) {
        scanf("%d", &len[i]);
        
        right += len[i];
        if(left < len[i]) left = len[i];
    }

    while(left <= right) {
        int mid = (left + right) / 2;
        
        if(M < solve(len, N, mid)) left = mid + 1;
        else right = mid - 1;
    }
    printf("%d\n", left);
    return 0;
}

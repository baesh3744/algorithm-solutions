#include <cstdio>
#include <algorithm>
using namespace std;

int gcd(int small, int big) {
    if(small > big) swap(small, big);

    if(small == 0) return big;
    
    while(big % small != 0) {
        int tmp = big % small;
        big = small;
        small = tmp;
    }
    return small;
}

bool compare(int left, int right) {
    return left < right;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);

        int arr[2000];
        for(int j = 0; j < N; j++) {
            scanf("%d", &arr[j]);
        }

        sort(arr, arr+N, compare);

        if(N == 1) printf("%d\n", arr[0]);
        else if(arr[0] == arr[N-1]) printf("INFINITY\n");
        else {
            int diff[2000];
            for(int j = 0; j < N-1; j++) {
                diff[j] = arr[j+1] - arr[j];
            }

            int ans = diff[0];
            for(int j = 1; j < N-1; j++) {
                ans = gcd(ans, diff[j]);
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}

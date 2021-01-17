#include <cstdio>
#include <algorithm>
using namespace std;

#define OVER_DIFF 10000000

bool compare(int left, int right) {
    return left < right;
}

int main(void) {
    int n;
    scanf("%d", &n);

    int arr[1000];
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    sort(arr, arr+n, compare);

    int min_diff = OVER_DIFF;
    for(int i = 0; i < n-1; i++) {
        int diff = arr[i+1] - arr[i];
        
        if(diff == 0) continue;

        if(diff < min_diff) min_diff = diff;
    }
    if(min_diff == OVER_DIFF) min_diff = arr[0];
    
    int D = arr[0];
    for(int dividing = 1; dividing <= min_diff; dividing++) {
        if(min_diff % dividing != 0) continue;

        D = min_diff / dividing;
        int remainder = arr[0] % D;
        if(remainder < 0) remainder += D;
        
        int foundAnswer = 1;
        for(int i = 1; i < n; i++) {
            int remainder_i = arr[i] % D;
            if(remainder_i < 0) remainder_i += D;

            if(remainder_i != remainder) {
                foundAnswer = 0;
                break;
            }
        }
        
        if(foundAnswer) break;
    }

    printf("%d\n", D);
    return 0;
}

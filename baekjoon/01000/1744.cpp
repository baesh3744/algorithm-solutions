#include <stdio.h>
#include <algorithm>
using namespace std;

bool compare(int a, int b) {
    return a < b;
}

int main(void) {
    int N;
    int ngtv = 0, one = 0, pstv = 0, ret = 0;
    int arr[10000];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
        if(arr[i] <= 0) ngtv++;
        else if(arr[i] == 1) one++;
        else pstv++;
    }

    sort(arr, arr+N, compare);

    for(int i = 0; i < ngtv/2; i++) { ret += arr[2*i] * arr[2*i+1]; }
    for(int i = 0; i < pstv/2; i++) { ret += arr[N-2*i-1] * arr[N-2*i-2]; }
    if(ngtv % 2 == 1) ret += arr[ngtv-1];
    if(pstv % 2 == 1) ret += arr[ngtv+one];
    ret += one;
    printf("%d\n", ret);
    return 0;
}
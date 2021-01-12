#include <stdio.h>
#include <string.h>

#define SIZE 10000
double arr[SIZE], cache[SIZE];

double multiply(int idx, int N) {
    if(cache[idx] != 0) return cache[idx];
    
    double ret = 1;
    for(int i = idx; i < N; i++) {
        ret *= arr[i];
        if(cache[idx] < ret) cache[idx] = ret;
    }
    return cache[idx];
}

int main(void) {
    int N;
    double ans = 0;

    memset(cache, 0, sizeof(double) * SIZE);
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%lf", &arr[i]);
    }

    for(int i = 0; i < N; i++) {
        double mult = multiply(i, N);
        if(mult > ans) ans = mult;
    }
    printf("%.3f\n", ans);

    return 0;
}
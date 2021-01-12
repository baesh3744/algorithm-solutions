#include <stdio.h>

/*
 * mysqrt - max의 제곱근을 리턴한다.
 * 
 * @param   max
 * @return  max의 제곱근
 */
int mysqrt(long long max) {
    long long ret = 1;
    while(ret*ret <= max) { ret++; }
    return (int)(ret - 1);
}

int main(void) {
    int sqrt_max;
    long long min, max, end_idx, start_idx;
    int cnt = 0;
    int num[1000001] = { 0, };

    scanf("%lld %lld", &min, &max);
    end_idx = max - min;

    sqrt_max = mysqrt(max);
    for(long long i = 2; i <= sqrt_max; i++) {
        if(min % (i*i) == 0) start_idx = 0;
        else start_idx = (i*i) - min % (i*i);

        for(long long idx = start_idx; idx <= end_idx; idx += (i*i)) {
            num[idx] = 1;
        }
    }

    for(int i = 0; i <= end_idx; i++) {
        if(num[i] == 0) cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}
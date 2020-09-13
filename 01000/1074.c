#include <stdio.h>

int mypow(int N) {
    int ret = 1;
    for(int i = 0; i < N; i++) ret *= 2;
    return ret;
}

int zBoard(int N, int r, int c) {
    if(N == 1) {
        if(r == 0 && c == 0) return 0;
        if(r == 0 && c == 1) return 1;
        if(r == 1 && c == 0) return 2;
        if(r == 1 && c == 1) return 3;
    }

    int qboard_size = mypow(N - 1);
    int base = qboard_size * qboard_size;
    int base_mlt = 0;
    int next_r = r;
    int next_c = c;

    if(r >= qboard_size) {
        base_mlt += 2;
        next_r = r - qboard_size;
    }
    if(c >= qboard_size) {
        base_mlt += 1;
        next_c = c - qboard_size;
    }

    return base * base_mlt + zBoard(N - 1, next_r, next_c);
}

int main(void) {
    int N, r, c;

    scanf("%d %d %d", &N, &r, &c);

    printf("%d\n", zBoard(N, r, c));

    return 0;
}
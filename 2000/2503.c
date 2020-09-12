#include <stdio.h>

#define SIZE 1000

int cnt = 0;
int ans[SIZE];

int findCandidate(int num, int strike, int ball) {
    int s, b, cand;
    int first = num / 100;
    int second = (num / 10) % 10;
    int third = num % 10;

    for(int i = 1; i < 10; i++) {
        for(int j = 1; j < 10; j++) {
            for(int k = 1; k < 10; k++) {
                cand = i*100 + j*10 + k;
                if(ans[cand] == -1 || i == j || j == k || k == i) continue;

                s = b = 0;

                if(i == first) s++;
                else if(i == second || i == third) b++;

                if(j == second) s++;
                else if(j == first || j == third) b++;

                if(k == third) s++;
                else if(k == first || k == second) b++;

                if(s != strike || b != ball) {
                    ans[cand] = -1;
                    cnt++;
                }
            }
        }
    }
}

int main(void) {
    int N, num, strike, ball;

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d %d %d", &num, &strike, &ball);
        findCandidate(num, strike, ball);
    }
    printf("%d\n", 504 - cnt);

    return 0;
}
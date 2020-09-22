#include <stdio.h>

void printChars(char ch, int cnt) {
    for(int i = 0; i < cnt; i++) printf("%c", ch);
    return ;
}

int main(void) {
    int N, K, cnt_A, cnt_B, move_cnt;
    int have_S = 0;

    scanf("%d %d", &N, &K);
    
    for(int i = 0; i <= N/2; i++) {
        if(i * (N-i) >= K) {
            cnt_A = N - i;
            cnt_B = i;
            have_S = 1;
            break;
        }
    }

    if(have_S == 0) printf("-1\n");
    else {
        move_cnt = cnt_A * cnt_B - K;
        
        while(move_cnt >= cnt_A) {
            printf("B"); cnt_B--;
            move_cnt -= cnt_A;
        }
        printChars('A', cnt_A-move_cnt);
        if(cnt_B > 0) { printf("B"); cnt_B--; }
        printChars('A', move_cnt);
        printChars('B', cnt_B);
        printf("\n");
    }
    return 0;
}
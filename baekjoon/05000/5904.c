#include <stdio.h>

int sk[100];

char mooArrWord(int k, int N) {
    if(k == 0) {
        sk[0] = 3;
        if(N == 1) return 'm';
        else if(N == 2 || N == 3) return 'o';
    } else {
        sk[k] = 2 * sk[k - 1] + k + 3;
    }

    if(N > sk[k]) return mooArrWord(k + 1, N);
    else if(N <= sk[k - 1]) return mooArrWord(k - 1, N);
    else if(N > (sk[k - 1] + k + 3)) return mooArrWord(k - 1, N - (sk[k - 1] + k + 3));
    else if((N - sk[k - 1]) == 1) return 'm';
    else if((N - sk[k - 1]) <= k + 3) return 'o';
}

int main(void) {
    int N;

    scanf("%d", &N);

    printf("%c\n", mooArrWord(0, N));
    
    return 0;
}
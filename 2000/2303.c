#include <stdio.h>

int main(void) {
    int N;
    int card[1000][5];
    int choose[10][3] = {
        {0, 1, 2}, {0, 1, 3}, {0, 1, 4}, {0, 2, 3}, {0, 2, 4}, {0, 3, 4},
        {1, 2, 3}, {1, 2, 4}, {1, 3, 4},
        {2, 3, 4}
    };
    int max = 0;
    int person = 0;
    
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < 5; j++) {
            scanf("%d", &card[i][j]);
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < 10; j++) {
            int sum = (card[i][choose[j][0]] + card[i][choose[j][1]] + card[i][choose[j][2]]) % 10;
            if(sum >= max) {
                person = i;
                max = sum;
            }
        }
    }

    printf("%d\n", person + 1);

    return 0;
}
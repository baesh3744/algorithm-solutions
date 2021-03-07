#include <stdio.h>

int main(void) {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);

        int tube[1000][1000];
        for(int j = 0; j < N - 1; j++) {
            for(int k = j + 1; k < N; k++) {
                scanf("%d", &tube[j][k]);
                tube[k][j] = tube[j][k];
            }
        }

        int triangle_total = N * (N - 1) * (N - 2) / 6;
        int triangle_impossible = 0;
        for(int j = 0; j < N; j++) {
            int number_of_one = 0;

            for(int k = 0; k < N; k++) {
                if(j == k) continue;

                if(tube[j][k] == 1) number_of_one++;
            }

            triangle_impossible += number_of_one * (N - 1 - number_of_one);
        }

        printf("%d\n", triangle_total - triangle_impossible / 2);
    }
    return 0;
}

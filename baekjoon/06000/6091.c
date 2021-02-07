#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1024

int main(void) {
    int N;
    scanf("%d", &N);

    int (*list)[MAX_N] = malloc(sizeof(int) * MAX_N * MAX_N);
    int (*tree)[MAX_N] = malloc(sizeof(int) * MAX_N * MAX_N);
    for(int i = 0; i < N-1; i++) {
        for(int j = i+1; j < N; j++) {
            scanf("%d", &tree[i][j]);
            tree[j][i] = tree[i][j];
        }
    }

    for(int i = 0; i < N-1; i++) {
        for(int j = i+1; j < N; j++) {
            int isShortest = 1;
            for(int k = 0; isShortest && k < N; k++) {
                if(k == i || k == j) continue;

                if(tree[i][k] + tree[k][j] <= tree[i][j]) isShortest = 0;
            }

            if(isShortest) {
                int index = ++list[i][0];
                list[i][index] = j + 1;

                index = ++list[j][0];
                list[j][index] = i + 1;
            }
        }
    }

    for(int i = 0; i < N; i++) {
        int count = list[i][0];
        printf("%d ", count);
        for(int j = 1; j <= count; j++) {
            printf("%d ", list[i][j]);
        }
        printf("\n");
    }
    free(list); free(tree);
    return 0;
}

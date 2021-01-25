#include <stdio.h>

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b; 
    *b = tmp;
}

int main(void) {
    while(1) {
        int a, b;
        scanf("%d %d", &a, &b);

        if(a == 0 && b == 0) return 0;

        int isHyeog = 1;
        while(a != 0 && b != 0) {
            if(a < b) swap(&a, &b);

            if(a % b == 0 || a / b >= 2) break;
            else if(a / b < 2) a -= b;

            isHyeog = isHyeog == 1 ? 0 : 1;
        }

        isHyeog == 1 ? printf("A wins\n") : printf("B wins\n");
    }
}

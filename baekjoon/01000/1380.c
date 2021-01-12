#include <stdio.h>
#include <string.h>

#define SIZE 101

int main(void) {
    int n, idx;
    int check[SIZE];
    char ch;
    char name[SIZE][62];
    int cnt = 1;
    
    while(1) {
        scanf("%d", &n);

        if(n == 0) return 0;

        memset(check, 0, sizeof(int) * SIZE);
        getchar();
        for(int i = 0; i < n; i++) fgets(name[i], 62, stdin);
        for(int i = 1; i < 2*n; i++) {
            scanf("%d %c", &idx, &ch);
            
            if(check[idx] == 0) check[idx]++;
            else if(check[idx] == 1) check[idx]--;
        }

        for(int i = 1; i <= n; i++) {
            if(check[i] == 1) {
                printf("%d %s", cnt++, name[i-1]);
                break;
            }
        }
    }
}
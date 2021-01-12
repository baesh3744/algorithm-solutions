#include <stdio.h>

int main(void) {
    char number[1000001];
    int check[9] = { 0, };
    int ans = 0;

    scanf("%s", number);

    for(int i = 0; number[i] != '\0'; i++) {
        if(number[i] == '9') check[6]++;
        else check[number[i] - '0']++;
    }

    if(check[6] % 2 == 0) check[6] /= 2;
    else check[6] = check[6] / 2 + 1;

    for(int i = 0; i < 9; i++) {
        if(check[i] > ans) ans = check[i];
    }
    printf("%d\n", ans);

    return 0;
}
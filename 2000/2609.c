#include <stdio.h>

int main(void) {
    int num1, num2, gcd;

    scanf("%d %d", &num1, &num2);

    gcd = num1 < num2 ? num1 : num2;

    while(1) {
        if((num1 % gcd == 0) && (num2 % gcd == 0)) {
            break;
        }
        gcd--;
    }

    printf("%d\n%d\n", gcd, num1 * num2 / gcd);

    return 0;
}
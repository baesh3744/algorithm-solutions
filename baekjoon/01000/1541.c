#include <stdio.h>

/*
 * execOp - 식의 마지막 또는 -, +를 만났을 때, 이전에 읽은 수에 대한 연산을 진행한다.
 *          식의 첫 번째 수를 제외하고는 빼는 것이 결과가 최소가 된다.
 */
void execOp(int *ret, int *num, int *is_first) {
    if(*is_first == 1) {
        *ret += *num;
    } else {
        *ret -= *num;
    }
    *num = 0;
}

int main(void) {
    int num = 0, ret = 0, is_first = 1;
    char exp[51];

    scanf("%s", exp);

    for(int i = 0; exp[i] != '\0'; i++) {
        if(('0' <= exp[i]) && (exp[i] <= '9')) {
            num = num*10 + exp[i]-'0';
            continue;
        }
        
        execOp(&ret, &num, &is_first);
        if(exp[i] == '-') is_first = 0;
    }
    execOp(&ret, &num, &is_first);
    printf("%d\n", ret);
    return 0;
}
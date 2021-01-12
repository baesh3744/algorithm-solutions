#include <stdio.h>

#define FAIL 9
const int dfa[10][2] = {
    {5, 1},         // 0
    {2, FAIL},      // 1
    {3, FAIL},      // 2
    {3, 4},         // 3
    {5, 7},         // 4
    {FAIL, 6},      // 5
    {5, 1},         // 6
    {8, 7},         // 7
    {3, 6},         // 8
    {FAIL, FAIL},   // 9
};

int isPattern(char *str) {
    int state = 0;
    for(int i = 0; state != FAIL && str[i] != '\0'; i++) {
        char next = str[i] - '0';
        state = dfa[state][next];
    }
    return state == 4 || state == 6 || state == 7;
}

int main(void) {
    char str[151];
    scanf("%s", str);

    printf(isPattern(str) ? "SUBMARINE\n" : "NOISE\n");
    return 0;
}

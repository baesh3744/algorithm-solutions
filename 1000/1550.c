#include <stdio.h>
#include <string.h>

int hexToDec(char h) {
    if('0' <= h && h <= '9') {
        return h - 48;
    }
    if('A' <= h && h <= 'F') {
        return h - 55;
    }
}

int main(void) {
    char hex[10];
    int dec, len;

    scanf("%s", hex);

    dec = 0;
    len = strlen(hex);
    for(int i = 0; i < len; i++) {
        int plus;

        plus = hexToDec(hex[i]);
        for(int j = 0; j < len - i - 1; j++) {
            plus *= 16;
        }
        dec += plus;
    }

    printf("%d\n", dec);

    return 0;
}
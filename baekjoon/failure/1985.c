#include <stdio.h>
#include <string.h>

#define SIZE 10
int num1[SIZE], num2[SIZE];

int checkZero(char *data) {
    if(data[0] == '0') return -1;
    return 1;
}

void makeNumberArray(char *data, int num[]) {
    memset(num, 0, sizeof(int) * SIZE);
    
    for(int i = 0; data[i] != '\0'; i++) {
        int idx = data[i] - '0';
        if(num[idx] == 0) num[idx]++;
    }
}

int isFriends(char *data1, char *data2) {
    if(checkZero(data1) == -1 || checkZero(data2) == -1) return -1;

    makeNumberArray(data1, num1);
    makeNumberArray(data2, num2);

    for(int i = 0; i < SIZE; i++) {
        if(num1[i] != num2[i]) return -1;
    }
    return 1;
}

int changeNumbers(char *data1, char *data2) {
    int len = strlen(data1);

    if(len == 1) {
        if(data1[0] != 9) {
            data1[0]++;
            if(isFriends(data1, data2) == 1) return 1;
            data1[0]--;
        }
        if(data1[0] != 0) {
            data1[0]--;
            if(isFriends(data1, data2) == 1) return 1;
            data1[0]++;
        }
    } else {
        for(int i = 0; i < len - 1; i++) {
            if(data1[i] != 9 && data1[i + 1] != 0) {
                data1[i]++; data1[i + 1]--;
                if(isFriends(data1, data2) == 1) return 1;
                data1[i]--; data1[i + 1]++;
            }
            if(data1[i] != 0 && data1[i + 1] != 9) {
                data1[i]--; data1[i + 1]++;
                if(isFriends(data1, data2) == 1) return 1;
                data1[i]++; data1[i + 1]--;
            }
        }
    }
    return -1;
}

int main(void) {
    char a[102], b[102];

    for(int i = 0; i < 3; i++) {
        scanf("%s", a);
        scanf("%s", b);

        if(isFriends(a, b) == 1) printf("friends\n");
        else if(changeNumbers(a, b) == 1 || changeNumbers(b, a) == 1) printf("almost friends\n");
        else printf("nothing\n");
    }
    
    return 0;
}
#include <stdio.h>
#include <string.h>

#define MAX 55
char copy[MAX];

char *compareWord(char *word1, char *word2) {
    int len = strlen(word1);
    for(int i = 0; i < len; i++) {
        if(word1[i] < word2[i]) return word1;
        if(word1[i] > word2[i]) return word2;
    }
    return word1;
}

void swapWord(int idx1, int idx2) {
    char tmp = copy[idx1];
    copy[idx1] = copy[idx2];
    copy[idx2] = tmp;
}

void reverseWord(int first, int second) {
    int third = strlen(copy) - 1;
    for(int i = 0; i < ((first + 1) / 2); i++) {
        swapWord(i, first - i);
    }
    for(int i = 0; i < ((second - first + 1) / 2); i++) {
        swapWord(first + 1 + i, second - i);
    }
    for(int i = 0; i < ((third - second + 1) / 2); i++) {
        swapWord(second + 1 + i, third - i);
    }
}

int main(void) {
    char origin_word[MAX], answer[MAX];

    scanf("%s", origin_word);

    for(int i = 0; i < MAX; i++) {
        answer[i] = 'z';
    }
    answer[MAX] = '\0';
    for(int i = 0; i < strlen(origin_word) - 2; i++) {
        for(int j = i + 1; j < strlen(origin_word) - 1; j++) {
            strcpy(copy, origin_word);
            reverseWord(i, j);
            strcpy(answer, compareWord(answer, copy));
        }
    }
    printf("%s\n", answer);

    return 0;
}
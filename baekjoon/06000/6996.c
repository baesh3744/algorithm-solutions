#include <stdio.h>
#include <string.h>

int cmpWord(char *a, char *b) {
    int i;

    for(i = 0; a[i] != '\0' && b[i] != '\0'; i++) {
        if(a[i] == b[i]) continue;
        else return -1;
    }
    if(a[i] == '\0' && b[i] == '\0') return 1;
    return -1;
}

void bSortWord(char *word) {
    int len = strlen(word);

    for(int i = 0; i < len - 1; i++) {
        for(int j = 0; j < len - 1 - i; j++) {
            if(word[j] > word[j + 1]) {
                char tmp = word[j];
                word[j] = word[j + 1];
                word[j + 1] = tmp;
            }
        }
    }
}

int main(void) {
    int t;
    char a[101], b[101], a_tmp[101], b_tmp[101];

    scanf("%d", &t);

    for(int i = 0; i < t; i++) {
        scanf("%s %s", a, b);

        strcpy(a_tmp, a);
        strcpy(b_tmp, b);
        bSortWord(a_tmp);
        bSortWord(b_tmp);
        
        if(cmpWord(a_tmp, b_tmp) == 1) printf("%s & %s are anagrams.\n", a, b);
        else printf("%s & %s are NOT anagrams.\n", a, b);
    }

    return 0;
}
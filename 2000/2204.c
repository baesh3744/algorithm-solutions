#include <stdio.h>
#include <string.h>

int mysize(char *str) {
    for(int len = 0; ; len++) {
        if(str[len] == '\0') return len;
    }
}

int mystrcmp(char *first, char *second) {
    int f_size = mysize(first);
    int s_size = mysize(second);
    char f_char, s_char;

    f_size = f_size < s_size ? f_size : s_size;
    for(int i = 0; i < f_size; i++) {
        if((f_char = first[i]) < 97) f_char += 32;
        if((s_char = second[i]) < 97) s_char += 32;

        if(f_char == s_char) continue;
        else if(f_char < s_char) return -1;
        else if(f_char > s_char) return 1;
    }
    return f_size == s_size ? 1 : -1;
}

int main(void) {
    int n;
    char fast[21], input[21];
    
    while(1) {
        scanf("%d", &n);

        if(n == 0) return 0;

        for(int i = 0; i < n; i++) {
            scanf("%s", input);

            if(i == 0) strcpy(fast, input);
            else if(mystrcmp(fast, input) > 0) strcpy(fast, input);
        }

        printf("%s\n", fast);
    }
}
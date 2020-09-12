#include <stdio.h>

int main(void) {
    int ans = 0;
    char word[101];

    scanf("%s", word);

    for(int i = 0; word[i] != '\0'; i++) {
        if(word[i+1] != '\0') {
            if((word[i] == 'c' && (word[i+1] == '-' || word[i+1] == '='))
                || (word[i] == 'd' && word[i+1] == '-')
                || (word[i] == 'l' && word[i+1] == 'j')
                || (word[i] == 'n' && word[i+1] == 'j')
                || (word[i] == 's' && word[i+1] == '=')
                || (word[i] == 'z' && word[i+1] == '=')) {
                i += 1;
            } else if(word[i] == 'd' && word[i+2] != '\0' && word[i+1] == 'z' && word[i+2] == '=') {
                i += 2;
            }
        }
        ans++;
    }
    printf("%d\n", ans);

    return 0;
}
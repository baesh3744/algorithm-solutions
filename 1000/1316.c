#include <stdio.h>
#include <string.h>

#define SIZE 26

int main(void) {
    int N;
    int cnt = 0;
    int alpha[SIZE];
    char word[101];

    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        int go = 1;
        char current;

        scanf("%s", word);
        memset(alpha, 0, sizeof(int) * SIZE);

        current = word[0];
        alpha[current - 'a'] = 1;
        for(int j = 0; go == 1 && word[j] != '\0'; j++) {
            if(word[j] != current) {
                if(alpha[word[j] - 'a'] == 0) {
                    alpha[word[j] - 'a'] = 1;
                    current = word[j];
                } else {
                    go = 0;
                }
            }
        }
        
        if(go == 1) cnt++;
    }

    printf("%d\n", cnt);

    return 0;
}
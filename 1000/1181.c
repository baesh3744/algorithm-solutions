#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void* left, const void* right) {
    char* first = (char*)left;
    char* second = (char*)right;
    int f_size, s_size;

    for(f_size = 0; first[f_size] != '\0'; f_size++);
    for(s_size = 0; second[s_size] != '\0'; s_size++);

    if(f_size < s_size) return -1;
    if(f_size > s_size) return 1;
    return strcmp(first, second);
}

int main(void) {
    int N;
    char words[20000][51];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) { scanf("%s", words[i]); }

    qsort(words, N, sizeof(words[0]), comp);
    for(int i = 0; i < N; i++) {
        if(i == 0 || strcmp(words[i], words[i-1]) != 0) printf("%s\n", words[i]);
    }

    return 0;
}
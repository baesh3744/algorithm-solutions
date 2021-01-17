#include <stdio.h>

int isSlump(char *str, int idx) {
    if(str[idx] != 'D' && str[idx] != 'E') return -1;

    while(str[++idx] == 'F');

    if(str[idx] == 'G') return idx + 1;
    return isSlump(str, idx);
}

int isSlimp(char *str, int idx) {
    if(str[idx] != 'A') return -1;

    int end_slimp, end_slump;
    if(str[idx+1] == 'H') return idx + 2;
    else if(str[idx+1] == 'B' && (end_slimp = isSlimp(str, idx+2)) != -1 && str[end_slimp] == 'C') return end_slimp + 1;
    else if((end_slump = isSlump(str, idx+1)) != -1 && str[end_slump] == 'C') return end_slump + 1;

    return -1;
}

int main(void) {
    int N;
    scanf("%d", &N);

    printf("SLURPYS OUTPUT\n");
    for(int i = 0; i < N; i++) {
        char str[61];
        scanf("%s", str);

        int start_slump, end_slump;
        if((start_slump = isSlimp(str, 0)) != -1 && (end_slump = isSlump(str, start_slump)) != -1 && str[end_slump] == '\0') printf("YES\n");
        else printf("NO\n");
    }
    printf("END OF OUTPUT\n");
    return 0;
}

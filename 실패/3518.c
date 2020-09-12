#include <stdio.h>
#include <string.h>

int main(void) {
    int idx, len, i;
    int sntc = 0;
    int word_cnt[1000], max_cnt[181];
    char contents[1000][182];

    memset(max_cnt, 0, sizeof(int) * 181);
    memset(word_cnt, 0, sizeof(int) * 1000);

    while(fgets(contents[sntc], 182, stdin) != NULL) {
        for(i = 0, idx = 0, len = 0; contents[sntc][i] != '\n'; i++) {
            if(contents[sntc][i] == ' ' && len != 0) {
                if(len > max_cnt[idx]) max_cnt[idx] = len;
                word_cnt[sntc]++;
                len = 0;
                idx++;
            } else if(contents[sntc][i] != ' ') {
                len++;
            }
        }
        if(len != 0) {
            if(len > max_cnt[idx]) max_cnt[idx] = len;
            word_cnt[sntc]++;
        }

        contents[sntc++][i] = '\0';
    }

    for(int i = 0; i < sntc; i++) {
        int j = 0;
        int k = 0;
        
        while(contents[i][j] != '\0') {
            len = 0;
            
            while(contents[i][j] == ' ') { j++; }
            while(len < max_cnt[k]) {
                if(contents[i][j] != ' ') printf("%c", contents[i][j++]);
                else if(contents[i][j] == ' ' && k != word_cnt[i]-1) printf(" ");
                len++;
            }
            
            if((++k) == word_cnt[i]) break;
            
            printf(" ");
        }
        printf("\n");
    }

    return 0;
}
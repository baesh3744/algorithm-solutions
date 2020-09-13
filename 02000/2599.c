#include <stdio.h>

int main(void) {
    int N;
    int found = 0;
    int stud[3][2];

    scanf("%d", &N);
    for(int i = 0; i < 3; i++) {
        scanf("%d %d", &stud[i][0], &stud[i][1]);
    }

    for(int i = 1; found == 0 && i <= stud[0][0]; i++) {
        int ab = i;
        int ac = stud[0][0] - i;
        int bc = stud[2][1] - ac;
        int ba = stud[1][0] - bc;
        int cb = stud[1][1] - ab;
        int ca = stud[2][0] - cb;
        
        if(ab >= 0 && ac >= 0 && ba >= 0 && bc >= 0 && ca >= 0 && cb >= 0) {
            found = 1;
            printf("1\n");
            printf("%d %d\n", ab, ac);
            printf("%d %d\n", ba, bc);
            printf("%d %d\n", ca, cb);
        }
    }
    if(found == 0) printf("0\n");

    return 0;
}
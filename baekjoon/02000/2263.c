#include <stdio.h>

/*
 * printFreeOrder - 이진 트리의 인오더와 포스트오더 배열을 통해 트리를 프리오더 순으로 출력한다.
 */
void printFreeOrder(const int *in, const int *post, int in_start, int in_end, int post_start, int post_end) {
    if(in_end < in_start || post_end < post_start) return ;
    if(in_start == in_end) {
        printf("%d ", in[in_start]);
        return ;
    }

    int mid = post[post_end];
    int mid_idx;
    for(mid_idx = in_start; mid_idx <= in_end; mid_idx++) {
        if(in[mid_idx] == mid) break;
    }
    int left_cnt = mid_idx - in_start;

    printf("%d ", mid);
    printFreeOrder(in, post, in_start, mid_idx-1, post_start, post_start+left_cnt-1);
    printFreeOrder(in, post, mid_idx+1, in_end, post_start+left_cnt, post_end-1);
}

int main(void) {
    int n;
    int in[100000], post[100000];

    scanf("%d", &n);
    for(int i = 0; i < n; i++) scanf("%d", &in[i]);
    for(int i = 0; i < n; i++) scanf("%d", &post[i]);

    printFreeOrder(in, post, 0, n-1, 0, n-1);
    printf("\n");
    
    return 0;
}

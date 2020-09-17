#include <stdio.h>

/*
 * updatedxy - 확장 유클리드 알고리즘에서 d, x, y의 값을 업데이트한다.
 * 
 * @param   q
 * @param   arr d, x, y의 값을 저장한 배열
 */
void updatedxy(int q, int arr[]) {
    int tmp = arr[1];
    arr[1] = arr[0] - q * arr[1];
    arr[0] = tmp;
}

/*
 * xgcd - 확장 유클리드 알고리즘을 사용하여 봉지 수를 구한다.
 * 
 * @param   K   파티에 참가하는 사람의 수
 * @param   c   한 봉지에 들어있는 사탕의 수
 * @param   x   한 사람당 받게될 사탕의 수
 * @param   y   선영이가 구매해야 할 봉지의 수
 * @return  0 - 사탕봉지가 없거나 봉지 수가 10^9을 초과한 경우
 *          1 - 봉지를 찾은 경우
 */
int xgcd(int K, int C, int *x, int *y) {
    int q;
    int d_arr[] = {K, C},
        x_arr[] = {1, 0},
        y_arr[] = {0, 1};
    
    while(d_arr[1] != 0) {
        q = d_arr[0] / d_arr[1];
        updatedxy(q, d_arr);
        updatedxy(q, x_arr);
        updatedxy(q, y_arr);
    }
    if(d_arr[0] != 1 || y_arr[0] > 1000000000) return 0;
    *y = y_arr[0] <= 0 ? y_arr[0]+K : y_arr[0];
    return 1;
}

int main(void) {
    int t, K, C, x, y;

    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        scanf("%d %d", &K, &C);
        if(C == 1 && K == 1000000000) printf("IMPOSSIBLE\n");
        else if(C == 1) printf("%d\n", K+1);
        else if(K == 1) printf("1\n");
        else if(xgcd(K, C, &x, &y) == 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", y);
    }
    return 0;
}
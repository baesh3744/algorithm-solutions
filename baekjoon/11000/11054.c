#include <stdio.h>

#define max(a, b) (a < b ? b : a)

int incrs[1000], decrs[1000];

/*
 * findMaxLen - start_idx부터 end_idx까지 증가/감소하는 수열의 최대 길이를 배열에 저장한다.
 * @param   A           입력받은 수열
 * @param   i           기준이 되는 인덱스
 * @param   start_idx   기준과 비교할 인덱스의 시작 인덱스
 * @param   end_idx     기준과 비교할 인덱스의 마지막 인덱스
 * @param   type        incrs/decrs
 */
void findMaxLen(int A[1000], int i, int start_idx, int end_idx, int type[1000]) {
    int max_len = 0;
    for(int j = start_idx; j < end_idx; j++) {
        if(A[j] < A[i]) max_len = max(max_len, type[j]);
    }
    type[i] = max_len + 1;
}

/*
 * getDecrsArr - decrs 배열을 채운다.
 * decrs는 배열의 값을 최댓값으로 감소하는 수열의 최대 길이를 저장한다.
 * @param   A   입력받은 수열
 * @param   N   수열의 길이
 */
void getDecrsArr(int A[1000], int N) {
    for(int i = N-1; i >= 0; i--) {
        findMaxLen(A, i, i+1, N, decrs);
    }
}

/*
 * getIncrsArr - incrs 배열을 채운다.
 * incrs는 배열의 값을 최댓값으로 증가하는 수열의 최대 길이를 저장한다.
 * @param   A   입력받은 수열
 * @param   N   수열의 길이
 */
void getIncrsArr(int A[1000], int N) {
    for(int i = 0; i < N; i++) {
        findMaxLen(A, i, 0, i, incrs);
    }
}

int main(void) {
    int N;
    int len = 0;
    int A[1000];

    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    getIncrsArr(A, N);
    getDecrsArr(A, N);

    for(int i = 0; i < N; i++) {
        len = max(len, incrs[i] + decrs[i] - 1);
    }
    printf("%d\n", len);

    return 0;
}
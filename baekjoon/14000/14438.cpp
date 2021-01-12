#include <stdio.h>
#include <algorithm>
using namespace std;

#define MAX_VAL 1000000001

/*
 * findMinSegTree - 수열 A의 left와 right 범위 내 최소값을 리턴한다.
 * 
 * @param   left, right     부분 수열의 인덱스 범위
 * @return  left와 right 범위 내의 최소값
 */
int findMinSegTree(int *seg_tree, int node, int start, int end, int left, int right) {
    if((right < start) || (end < left)) return MAX_VAL;
    if((left <= start) && (end <= right)) return seg_tree[node];

    int a, b;
    int mid = (start + end) / 2;
    return min((a = findMinSegTree(seg_tree, node*2, start, mid, left, right)), (b = findMinSegTree(seg_tree, node*2+1, mid+1, end, left, right)));
}

/*
 * updateSegTree - 수열 A에서 값이 변할 때, 세그먼트 트리 seg_tree를 업데이트한다.
 * 
 * @param   index           수열에서 변화한 값의 인덱스
 */
int updateSegTree(const int *A, int *seg_tree, int node, int start, int end, int index) {
    if((index < start) || (end < index)) return seg_tree[node];
    if(start == end) return seg_tree[node] = A[start];

    int mid = (start + end) / 2;
    return seg_tree[node] = min(updateSegTree(A, seg_tree, node*2, start, mid, index), updateSegTree(A, seg_tree, node*2+1, mid+1, end, index));
}

/*
 * initSegTree - 수열 A를 바탕으로 세그먼트 트리 seg_tree를 초기화한다.
 */
int initSegTree(const int *A, int *seg_tree, int node, int start, int end) {
    if(start == end) return seg_tree[node] = A[start];

    int mid = (start + end) / 2;
    return seg_tree[node] = min(initSegTree(A, seg_tree, node*2, start, mid), initSegTree(A, seg_tree, node*2+1, mid+1, end));
}

int main(void) {
    int N, M, type, i, v, ans;
    int A[100001], seg_tree[400000];

    scanf("%d", &N);
    for(int j = 1; j <= N; j++) {
        scanf("%d", &A[j]);
    }

    initSegTree(A, seg_tree, 1, 1, N);

    scanf("%d", &M);
    for(int j = 0; j < M; j++) {
        scanf("%d %d %d", &type, &i, &v);
        if(type == 1) {
            A[i] = v;
            updateSegTree(A, seg_tree, 1, 1, N, i);
        } else {
            ans = findMinSegTree(seg_tree, 1, 1, N, i, v);
            printf("%d\n", ans);
        }
    }
    return 0;
}
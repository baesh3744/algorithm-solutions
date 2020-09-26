#include <stdio.h>
#include <algorithm>
using namespace std;

#define ERR 1000000001

/*
 * findMinVal - 주어진 구간에서 최소값을 찾아낸다.
 */
int findMinVal(const int *seg_tree, int node, int start, int end, int left, int right) {
    if((right < start) || (end < left)) return ERR;
    if((left <= start) && (end <= right)) return seg_tree[node];

    int mid = (start + end) / 2;
    return min(findMinVal(seg_tree, node*2, start, mid, left, right), findMinVal(seg_tree, node*2+1, mid+1, end, left, right));
}

/* 
 * initSegTree - arr에서 Segment Tree를 생성한다.
 */
int initSegTree(const int *arr, int *seg_tree, int node, int start, int end) {
    if(start == end) return seg_tree[node] = arr[start];

    int mid = (start + end) / 2;
    return seg_tree[node] = min(initSegTree(arr, seg_tree, node*2, start, mid), initSegTree(arr, seg_tree, node*2+1, mid+1, end));
}

int main(void) {
    int N, M, a, b;
    int arr[100001], seg_tree[400004];

    scanf("%d %d", &N, &M);
    for(int i = 1; i <= N; i++) {
        scanf("%d", &arr[i]);
    }

    initSegTree(arr, seg_tree, 1, 1, N);

    for(int i = 0; i < M; i++) {
        scanf("%d %d", &a, &b);

        printf("%d\n", findMinVal(seg_tree, 1, 1, N, a, b));
    }
    return 0;
}
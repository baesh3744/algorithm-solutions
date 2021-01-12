#include <stdio.h>

#define min(a, b) (a < b ? a : b)

/*
 * findIndex - 수열에서 최소값의 인덱스를 구한다.
 * 
 * @param   seg_tree    세그먼트 트리
 * @param   node        세그먼트 트리의 인덱스
 * @param   start       세그먼트 트리에서 참조하는 부분수열의 시작 인덱스
 * @param   end         세그먼트 트리에서 참조하는 부분수열의 마지막 인덱스
 */
int findIndex(int seg_tree[262144], int node, int start, int end) {
    if(start == end) return start;

    int mid = (start + end) / 2;
    
    if(seg_tree[node] == seg_tree[node*2]) return findIndex(seg_tree, node*2, start, mid);
    else return findIndex(seg_tree, node*2+1, mid+1, end);
}

/*
 * updateSegTree - 세그먼트 트리에서 인덱스 node에 저장된 값이 변할 때 부모 노드를 따라가며 값을 업데이트한다.
 * 
 * @param   seg_tree    세그먼트 트리
 * @param   node        세그먼트 트리의 인덱스
 */
void updateSegTree(int seg_tree[262144], int node) {
    if(node < 2) return ;

    if(node % 2 == 0) seg_tree[node/2] = min(seg_tree[node], seg_tree[node+1]);
    else seg_tree[node/2] = min(seg_tree[node-1], seg_tree[node]);
    
    updateSegTree(seg_tree, node/2);
}

/*
 * initSegTree - 수열 A의 최소값을 저장한 세그먼트 트리 seg_tree를 생성한다.
 * 
 * @param   A           입력받은 수열
 * @param   seg_tree    A의 세그먼트 트리
 * @param   A_idx       A의 값이 세그먼트 트리에서 저장된 인덱스
 * @param   node        세그먼트 트리의 인덱스
 * @param   start       세그먼트 트리가 참조하는 부분수열의 시작 인덱스
 * @param   end         세그먼트 트리가 참조하는 부분수열의 마지막 인덱스
 * @return  세그먼트 트리에서 인덱스 node에 저장된 값
 */
int initSegTree(int A[100000], int seg_tree[262144], int A_idx[262144], int node, int start, int end) {
    if(start == end) {
        A_idx[start] = node;
        return seg_tree[node] = A[start];
    }

    int mid = (start + end) / 2;

    return seg_tree[node] = min(initSegTree(A, seg_tree, A_idx, node*2, start, mid), initSegTree(A, seg_tree, A_idx, node*2+1, mid+1, end));
}

int main(void) {
    int N, M, type, i, v;
    int A[100001], seg_tree[262144], A_idx[262144];

    scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
        scanf("%d", &A[i]);
    }
    
    initSegTree(A, seg_tree, A_idx, 1, 1, N);
    
    scanf("%d", &M);
    for(int ii = 0; ii < M; ii++) {
        scanf("%d", &type);
        if(type == 1) {
            scanf("%d %d", &i, &v);
            seg_tree[A_idx[i]] = v;
            updateSegTree(seg_tree, A_idx[i]);
        } else {
            printf("%d\n", findIndex(seg_tree, 1, 1, N));
        }
    }
    return 0;
}
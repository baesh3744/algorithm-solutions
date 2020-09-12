#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct NodeStruct {
    char name[21];
    int idx;
    struct NodeStruct* leftChild;
    struct NodeStruct* rightChild;
} Node;

char name_arr[100001][21];
Node* root = NULL;

Node* BSTInsert(Node* node, int idx) {
    if(node == NULL) {
        node = (Node*) malloc(sizeof(Node));
        node->leftChild = node->rightChild = NULL;
        strcpy(node->name, name_arr[idx]);
        node->idx = idx;
    } else {
        if(strcmp(node->name, name_arr[idx]) > 0) {
            node->leftChild = BSTInsert(node->leftChild, idx);
        } else {
            node->rightChild = BSTInsert(node->rightChild, idx);
        }
    }
    return node;
}

int BSTSearch(Node* node, char* name) {
    if(strcmp(node->name, name) == 0) return node->idx;
    else if(strcmp(node->name, name) < 0) return BSTSearch(node->rightChild, name);
    else return BSTSearch(node->leftChild, name);
}

int stringToInt(char* qstn) {
    int ret = 0;
    for(int i = 0; qstn[i] != '\0'; i++) {
        ret *= 10;
        ret += qstn[i] - '0';
    }
    return ret;
}

int main(void) {
    int N, M, num;
    char qstn[21];

    scanf("%d %d", &N, &M);
    for(int i = 1; i <= N; i++) {
        scanf("%s", name_arr[i]);

        root = BSTInsert(root, i);
    }

    for(int i = 0; i < M; i++) {
        scanf("%s", qstn);

        if('A' <= qstn[0] && qstn[0] <= 'Z') {
            printf("%d\n", BSTSearch(root, qstn));
        } else {
            num = stringToInt(qstn);
            printf("%s\n", name_arr[num]);
        }
    }

    return 0;
}
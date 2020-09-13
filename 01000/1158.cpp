#include <stdio.h>
#include <queue>
using namespace std;

int main(void) {
    int N, K;
    queue<int> que;

    scanf("%d %d", &N, &K);

    for(int i = 1; i <= N; i++) {
        que.push(i);
    }

    printf("<");
    while(que.size() != 1) {
        for(int i = 0; i < K - 1; i++) {
            int first = que.front();
            que.pop();
            que.push(first);
        }
        printf("%d, ", que.front());
        que.pop();
    }
    printf("%d>\n", que.front());

    return 0;
}
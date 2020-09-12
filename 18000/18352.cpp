#include <stdio.h>
#include <string.h>
#include <queue>
#include <vector>
using namespace std;

#define SIZE 300001

int main(void) {
    int N, M, K, X, A, B;
    int visit[SIZE];
    queue<int> que;
    vector<vector<int> > graph(SIZE);
    int dist = 0, found = 0;

    memset(visit, 0, sizeof(int) * SIZE);
    scanf("%d %d %d %d", &N, &M, &K, &X);
    for(int i = 0; i < M; i++) {
        scanf("%d %d", &A, &B);
        graph[A].push_back(B);
    }

    que.push(X);
    visit[X] = 1;
    while(que.size() != 0) {
        if(dist == K) {
            priority_queue<int, vector<int>, greater<int> > pq;
            
            while(que.size() != 0) {
                pq.push(que.front());
                que.pop();
            }
            
            if(pq.size() == 0) printf("-1\n");
            else {
                while(pq.size() != 0) {
                    printf("%d\n", pq.top());
                    pq.pop();
                }
            }
            
            found = 1;
            break;
        }

        dist++;
        
        int q_size = que.size();
        for(int i = 0; i < q_size; i++) {
            int current = que.front();
            que.pop();

            for(int j = 0; j < graph[current].size(); j++) {
                int next = graph[current][j];
                
                if(visit[next] == 0) {
                    visit[next] = 1;
                    que.push(next);
                }
            }
        }
    }
    if(found == 0) printf("-1\n");

    return 0;
}
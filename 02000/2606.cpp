#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

#define SIZE 101

int main(void) {
    int c_num, p_num, c1, c2, com;
    int graph[SIZE][SIZE];
    int computers[SIZE];
    queue<int> que;
    int ans = 0;

    scanf("%d", &c_num);
    scanf("%d", &p_num);
    for(int i = 0; i < p_num; i++) {
        scanf("%d %d", &c1, &c2);
        graph[c1][c2] = 1;
        graph[c2][c1] = 1;
    }
    memset(computers, 0, sizeof(int) * SIZE);

    que.push(1);
    computers[1] = -1;
    while(que.size() != 0) {
        com = que.front();
        que.pop();
        
        ans++;

        for(int i = 1; i <= c_num; i++) {
            if(graph[com][i] == 1 && computers[i] == 0) {
                que.push(i);
                computers[i] = -1;
            }
        }
    }
    printf("%d\n", ans - 1);

    return 0;
}
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

#define SIZE 1001

int n;
char type[SIZE];
int price[SIZE], check[SIZE];
vector<vector<int> > vt;

int dfs(int cur, int p) {
    if(type[cur] == 'L' && p < price[cur]) p = price[cur];
    else if(type[cur] == 'T') {
        if(p < price[cur]) return 0;
        else p -= price[cur];
    }
    
    if(cur == n) return 1;

    for(int i = 0; i < vt[cur].size(); i++) {
        int next_cur = vt[cur][i];
        
        if(check[next_cur] == 0) {
            check[next_cur] = 1;
            if(dfs(next_cur, p) == 1) return 1;
            check[next_cur] = 0;
        }
    }
    return 0;
}

int main(void) {
    while(1) {
        scanf("%d", &n);

        if(n == 0) return 0;

        vector<int> empty;
        
        empty.push_back(0);
        vt.push_back(empty);
        memset(check, 0, sizeof(int) * SIZE);
        for(int i = 1; i <= n; i++) {
            int num;
            vector<int> v;

            getchar();
            scanf("%c %d", &type[i], &price[i]);
            while(1) {
                scanf("%d", &num);
                if(num == 0) break;
                v.push_back(num);
            }

            vt.push_back(v);
        }

        check[1] = 1;
        if(dfs(1, 0) == 1) printf("Yes\n");
        else printf("No\n");
        vt.clear();
    }
}
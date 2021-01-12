#include <stdio.h>
#include <vector>
using namespace std;

typedef vector<long long> vll;

long long mod = 1e17;
int N;
int board[101][101];
vll cache[101][101];

int isRange(int now) {
    return (0 < now && now <= N);
}

vll add(vll n1, vll n2) {
    if(n2.size() > n1.size()) swap(n1, n2);

    int n1_size = n1.size(), n2_size = n2.size();
    long long carry = 0;
    for(int i = 0; i < n1_size; i++) {
        if(carry > 0) n1[i] += carry, carry = 0;

        if(i < n2_size) n1[i] += n2[i];
        
        if(n1[i] >= mod) carry = n1[i] / mod, n1[i] %= mod;
    }
    if(carry != 0) n1.push_back(carry);
    return n1;
}

vll dp(int i, int j) {
    if(i == N && j == N) return vll(1, 1);
    if(board[i][j] == 0) return vll(1, 0);
    if(cache[i][j].size() != 0) return cache[i][j];

    vll ret;
    int next_i = i + board[i][j], next_j = j + board[i][j];
    if(isRange(next_i)) ret = add(ret, dp(next_i, j));
    if(isRange(next_j)) ret = add(ret, dp(i, next_j));
    return (cache[i][j] = ret);
}

int main(void) {
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            scanf("%d", &board[i][j]);
        }
    }

    vll ans = dp(1, 1);
    int start = ans.size() - 1;
    for(int i = start; i >= 0; i--) {
        if(i == start) printf("%lld", ans[i]);
        else printf("%017lld", ans[i]);
    }
    printf("\n");
    return 0;
}

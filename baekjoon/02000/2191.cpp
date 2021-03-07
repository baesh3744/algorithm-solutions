#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 100

int N, M, S, V;
double mouses[MAX][2], tunnels[MAX][2];
int A[MAX], B[MAX];
vector<int> graph[MAX];
bool visited[MAX];

double distance(int m, int t) {
    return sqrt(pow((mouses[m][0] - tunnels[t][0]), 2) + pow((mouses[m][1] - tunnels[t][1]), 2));
}

bool dfs(int a) {
    visited[a] = true;

    for(int b : graph[a]) {
        if(B[b] == -1 || (!visited[B[b]] && dfs(B[b]))) {
            A[a] = b;
            B[b] = a;
            return true;
        }
    }
    return false;
}

int main(void) {
    scanf("%d %d %d %d", &N, &M, &S, &V);
    for(int i = 0; i < N; i++) {
        scanf("%lf %lf", &mouses[i][0], &mouses[i][1]);
    }
    for(int i = 0; i < M; i++) {
        scanf("%lf %lf", &tunnels[i][0], &tunnels[i][1]);
    }

    double max_distance = 1.0 * S * V;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(distance(i, j) <= max_distance) graph[i].push_back(j);
        }
    }

    int matching = 0;
    fill(A, A + N, -1);
    fill(B, B + M, -1);
    for(int i = 0; i < N; i++) {
        if(A[i] == -1) {
            fill(visited, visited + N, false);

            if(dfs(i)) matching++;
        }
    }
    printf("%d\n", N - matching);
    return 0;
}

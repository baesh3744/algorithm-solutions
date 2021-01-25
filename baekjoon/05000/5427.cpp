#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> location_t;

bool isEdge(int cur_h, int cur_w, int h, int w) {
    return (cur_h == 0 || cur_h == h-1 || cur_w == 0 || cur_w == w-1);
}

bool isRange(int cur_h, int cur_w, int h, int w) {
    return (0 <= cur_h && cur_h < h && 0 <= cur_w && cur_w < w);
}

int main(void) {
    int test;
    scanf("%d", &test);

    for(int t = 0; t < test; t++) {
        int w, h;
        scanf("%d %d", &w, &h);

        bool visited[1000][1000] = { false };
        char building[1000][1001];
        queue<location_t> sang_geuns;
        queue<location_t> fires;
        for(int i = 0; i < h; i++) {
            scanf("%s", building[i]);

            for(int j = 0; j < w; j++) {
                if(building[i][j] == '@') {
                    sang_geuns.push(make_pair(i, j));
                    visited[i][j] = true;
                    building[i][j] = '.';
                }

                if(building[i][j] == '*') {
                    fires.push(make_pair(i, j));
                }
            }
        }

        // 첫 위치가 가장자리인 경우
        location_t sang_geun = sang_geuns.front();
        if(isEdge(sang_geun.first, sang_geun.second, h, w)) {
            printf("1\n");
            continue;
        }

        // 한 번 이상을 움직여 가장자리에 위치하는 경우
        int answer = -1;
        int move = 0;
        int move_w[] = {  0, 1, 0, -1},
            move_h[] = { -1, 0, 1,  0};
        while(answer == -1 && !sang_geuns.empty()) {
            move++;

            // 불 이동
            int fires_size = fires.size();
            for(int i = 0; i < fires_size; i++) {
                location_t fire = fires.front(); fires.pop();
                for(int j = 0; j < 4; j++) {
                    int next_h = fire.first + move_h[j];
                    int next_w = fire.second + move_w[j];
                    if(isRange(next_h, next_w, h, w) && building[next_h][next_w] == '.') {
                        fires.push(make_pair(next_h, next_w));
                        building[next_h][next_w] = '*';
                    }
                }
            }

            // 상근 이동
            int sang_geuns_size = sang_geuns.size();
            for(int i = 0; i < sang_geuns_size; i++) {
                location_t sang_geun = sang_geuns.front(); sang_geuns.pop();
                for(int j = 0; j < 4; j++) {
                    int next_h = sang_geun.first + move_h[j];
                    int next_w = sang_geun.second + move_w[j];
                    if(isRange(next_h, next_w, h, w) && building[next_h][next_w] == '.' && !visited[next_h][next_w]) {
                        // 상근이의 다음 위치가 가장자리이면 탈출
                        if(isEdge(next_h, next_w, h, w)) {
                            answer = move + 1;
                            break;
                        }

                        sang_geuns.push(make_pair(next_h, next_w));
                        visited[next_h][next_w] = true;
                    }
                }
            }
        }

        if(answer == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", answer);
    }
    return 0;
}

#include <algorithm>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, int> pii;

int main(void) {
    int N;
    vector<pair<pii, pii> > vt;
    map<int, int> ans;
    map<pii, int, greater<> > mp;

    cin >> N;
    for(int i = 0; i < N; i++) {
        int left, right, height;
        cin >> left >> height >> right;

        vt.push_back({ {left, right}, {height, 1} });
        vt.push_back({ {right, left}, {height, 0} });
    }

    // x좌표를 기준으로 오름차순 정렬
    sort(vt.begin(), vt.end());

    int max_height = -1;
    for(int i = 0; i < vt.size(); i++) {
        int here = vt[i].first.first;
        int opp = vt[i].first.second;
        int height = vt[i].second.first;
        int type = vt[i].second.second;

        // 건물의 시작점이라면 map에 추가
        if(type == 1) {
            mp[{ height, here }] = opp;
        }
        
        // 건물의 마지막점이라면 map에서 제거
        else {
            auto it = mp.find({ height, opp });
            mp.erase(it);
        }

        // 현재 최고 높이를 측정
        int first_height = mp.begin()->first.first;

        // 현재 최고 높이가 기존의 최고 높이와 다르면,
        // (더 높은 건물이 추가 or 기존의 최고 건물이 제거)
        // 현재 x좌표와 높이를 저장
        if(first_height != max_height) {
            max_height = first_height;

            // 건물이 시작하는 경우
            if(type == 1) {
                ans[here] = max(ans[here], max_height);
            }

            // 건물이 끝나는 경우
            else {
                ans[here] = max_height;
            }
        }
    }

    int prev = -1;
    for(auto it = ans.begin(); it != ans.end(); it++) {
        if(it->second != prev) cout << it->first << " " << it->second << " ";
        prev = it->second;
    }
    cout << "\n";

    return 0;
}

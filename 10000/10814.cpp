#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

bool comp(pair<int, string> p1, pair<int, string> p2) {
    return p1.first < p2.first;
}

int main(void) {
    int N; cin >> N;
    vector<pair<int, string> > vt(N);

    for(int i = 0; i < N; i++) { cin >> vt[i].first >> vt[i].second; }

    stable_sort(vt.begin(), vt.end(), comp);
    for(int i = 0; i < N; i++) { cout << vt[i].first << " " << vt[i].second << "\n"; }

    return 0;
}
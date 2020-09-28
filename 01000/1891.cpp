#include <iostream>
#include <string>
#include <utility>
using namespace std;

/*
 * findIJ - 주어진 사분면 번호의 좌표를 구한다.
 */
pair<long long, long long> findIJ(string str, int idx, long long i, long long j, long long size) {
    if(size == 1) return make_pair(i, j);

    int next_idx = idx+1;
    long long next_size = size / 2;
    if(str[idx] == '1') return findIJ(str, next_idx, i, j+next_size, next_size);
    if(str[idx] == '2') return findIJ(str, next_idx, i, j, next_size);
    if(str[idx] == '3') return findIJ(str, next_idx, i+next_size, j, next_size);
    if(str[idx] == '4') return findIJ(str, next_idx, i+next_size, j+next_size, next_size);
}

/*
 * go - 이동 후의 좌표를 통해 사분면 번호를 구한다.
 */
string go(long long x, long long y, long long i, long long j, long long size) {
    if(size == 1) return "";

    long long next_size = size / 2;
    if(x < i+next_size && j+next_size <= y) return "1" + go(x, y, i, j+next_size, next_size);
    if(x < i+next_size && y < j+next_size) return "2" + go(x, y, i, j, next_size);
    if(i+next_size <= x && y < j+next_size) return "3" + go(x, y, i+next_size, j, next_size);
    if(i+next_size <= x && j+next_size <= y) return "4" + go(x, y, i+next_size, j+next_size, next_size);
}

int main(void) {
    int d;
    long long x, y;
    string str;

    cin >> d >> str;
    cin >> x >> y;

    long long size = (1LL << d);

    pair<long long, long long> p = findIJ(str, 0, 0, 0, size);

    p.first -= y;
    p.second += x;

    if(0 <= p.first && p.first < size && 0 <= p.second && p.second < size) {
        cout << go(p.first, p.second, 0, 0, size) << "\n";
    } else {
        cout << "-1" << "\n";
    }
    return 0;
}

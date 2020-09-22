#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

/*
 *  solve - T에서 S를 만들 수 있는지 판단한다.
 *          T가 A로 끝나면, 마지막 A를 제거한다.
 *          T가 B로 끝나면, 마지막 B를 제거하고 문자열을 뒤집는다.
 */
bool solve(const string S, string T) {
    if(S.length() == T.length()) return (S == T);

    char tb = T.back();
    int t_len = T.length();
    string new_T = T.substr(0, t_len-1);
    if(tb == 'B') reverse(new_T.begin(), new_T.end());
    return solve(S, new_T);
}

int main(void) {
    string S, T;

    cin >> S >> T;
    
    cout << (solve(S, T) == true ? 1 : 0) << '\n';
    return 0;
}
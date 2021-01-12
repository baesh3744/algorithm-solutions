#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

/*
 * solve - T를 S로 바꿀 수 있는지 판단한다.
 *         A ~ A - 맨 뒤의 A를 제거한다.
 *         A ~ B - 불가능하다.
 *         B ~ A - 맨 뒤의 A를 제거하거나, 맨 앞의 B를 제거한 후 뒤집는다.
 *         B ~ B - 맨 앞의 B를 제거한 후 뒤집는다.
 */
bool solve(const string S, string T) {
    if(S.length() == T.length()) return (S == T);

    bool ret = false;
    char tf = T.front(), tb = T.back();
    int t_len = T.length();
    if(tf == 'A' && tb == 'A') {
        return solve(S, T.substr(0, t_len-1));
    } else if(tf == 'A' && tb == 'B') {
        return false;
    } else if(tf == 'B') {
        if(tb == 'A') ret = solve(S, T.substr(0, t_len-1));
        string new_T = T.substr(1);
        reverse(new_T.begin(), new_T.end());
        return ret | solve(S, new_T);
    }
}

int main(void) {
    int s_len, t_len, need_B, cnt_A;
    string S, T;

    cin >> S >> T;

    cout << (solve(S, T) == true ? 1 : 0) << '\n';
    return 0;
}
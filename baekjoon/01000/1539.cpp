#include <stdio.h>
#include <map>
using namespace std;

int main(void) {
    int N;
    scanf("%d", &N);

    long long ans = 0;
    map<int, int> valueMap;
    for (int i = 0; i < N; i++) {
        int value;
        scanf("%d", &value);

        int m = 0;
        auto iter = valueMap.lower_bound(value);

        // value보다 큰 값과 비교
        // iter == end이면, 기존 map에서 value보다 큰 값이 없다.
        if (iter != valueMap.end()) m = max(m, iter->second);

        // value보다 작은 값과 비교
        // iter == begin이면, 기존 map에서 value보다 작은 값이 없다.
        if (iter != valueMap.begin()) m = max(m, (--iter)->second);

        valueMap[value] = m + 1;
        ans += 1LL + m;
    }

    printf("%lld\n", ans);
    return 0;
}

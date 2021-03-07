#include <stdio.h>
#include <map>
using namespace std;

int main(void) {
    int N;
    scanf("%d", &N);

    long long c = 0;
    map<int, int> m;
    for(int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);

        int current_c = 0;
        if(i != 0) {
            auto iter = m.upper_bound(num);

            if(iter != m.end()) current_c = max(current_c, iter->second);
            if(iter != m.begin()) current_c = max(current_c, (--iter)->second);
        }

        m[num] = current_c + 1;
        c += (long long)current_c;
        printf("%lld\n", c);
    }
    return 0;
}

#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int g_frequency[26];

void saveFrequency(char *word) {
    int size;
    for(size = 0; word[size] != '\0'; size++);

    for(int i = 0; i < size; i++) {
        int alphabet = word[i] - 'A';
        int idx = size - i - 1;

        g_frequency[alphabet] += (int)pow((double)10, (double)idx);
    }
}

bool compare(int left, int right) {
    return left > right;
}

int main(void) {
    int N;
    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        char word[9];
        scanf("%s", word);

        saveFrequency(word);
    }

    sort(g_frequency, g_frequency+26, compare);

    int ans = 0;
    for(int i = 0; i < 10; i++) {
        ans += g_frequency[i] * (9 - i);
    }
    printf("%d\n", ans);
    return 0;
}

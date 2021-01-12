#include <stdio.h>

int N;
int g_alphabet[10];  // 알파벳에 해당하는 값을 저장
int g_is_first[10];  // 알파벳이 처음으로 사용되면 1, 사용되지 않으면 0
int g_map_add[10][12];  // 알파벳의 자리별 빈도 수
char arrInput[50][13];

/*
 * saveInputToMap - 알파벳수가 주어졌을 때, 이를 g_is_first와 g_map_add에 저장한다.
 */
void saveInputToMap(char *arrInput) {
    int size;
    for(size = 0; arrInput[size] != '\0'; size++);

    // 처음 사용된 알파벳을 g_is_first에 1로 저장
    g_is_first[arrInput[0] - 'A'] = 1;

    // 알파벳의 자리별 빈도를 1씩 증가
    for(int i = 0; arrInput[i] != '\0'; i++) {
        int alphabet = arrInput[i] - 'A';
        int idx = 12 - size + i;
        g_map_add[alphabet][idx]++;

        // 빈도가 10을 넘어가면 자리 수를 하나 옮긴다.
        while(idx != 0) {
            if(g_map_add[alphabet][idx] < 10) break;

            g_map_add[alphabet][idx--] -= 10;
            g_map_add[alphabet][idx]++;
        }
    }
}

/*
 * assignValueToAlphabet - 알파벳에 값을 할당한다.
 */
void assignValueToAlphabet() {
    // 0을 할당할 때까지, 높은 자리부터 살펴본다.
    int value = 9;
    for(int i = 0; value >= 0 && i < 12; i++) {
        int max = -1;
        int isUpdate = 0;

        for(int now = 0; now < 10; now++) {
            // 값이 할당되었거나 해당 자리에 사용되지 않은 알파벳은 건너뛴다.
            if(g_alphabet[now] || !g_map_add[now][i]) continue;

            // 해당 자리에서 사용된 빈도 수가 더 높은 알파벳으로 max를 최신화한다.
            if(max == -1 || g_map_add[max][i] < g_map_add[now][i]) {
                max = now;
                isUpdate = 1;
            }

            // 사용된 빈도 수가 같다면
            else if(g_map_add[max][i] == g_map_add[now][i]) {
                // 다음으로 사용되는 자리가 높은 알파벳으로 max를 최신화한다.
                for(int j = i+1; j < 12; j++) {
                    if(g_map_add[max][j] > g_map_add[now][j]) break;
                    else if(g_map_add[now][j] > g_map_add[max][j]) {
                        max = now;
                        isUpdate = 1;
                        break;
                    }
                }
            }
        }
        
        // max가 최신화가 되었으면, 알파벳에 값을 할당한다.
        if(max != -1) g_alphabet[max] = value--;

        // 값이 할당되었으면, i를 1 감소시켜 해당 자리를 한 번 더 살펴본다.
        if(isUpdate) i--;
    }

    // 예외 처리 - 처음으로 사용된 알파벳에 0이 할당된 경우
    // 처음으로 사용되지 않은 알파벳 중 최소값을 구한다.
    int min = 100;
    for(int i = 0; i < 10; i++) {
        if(!g_is_first[i] && g_alphabet[i] < min) min = g_alphabet[i];
    }

    // 최소값을 가지는 알파벳을 0으로 바꾼다.
    // 처음으로 사용된 알파벳 중 최소값보다 작은 값을 가지는 알파벳의 값을 1 증가시킨다.
    for(int i = 0; i < 10; i++) {
        if(g_alphabet[i] == min) g_alphabet[i] = 0;
        else if(g_alphabet[i] < min) g_alphabet[i]++;
    }
}

/*
 * calculateSum - 주어진 알파벳수의 합을 구한다.
 */
long long calculateSum() {
    long long sum = 0;
    for(int i = 0; i < N; i++) {
        long long sub_sum = 0;
        for(int j = 0; arrInput[i][j] != '\0'; j++) {
            sub_sum *= 10;
            sub_sum += g_alphabet[arrInput[i][j] - 'A'];
        }
        sum += sub_sum;
    }
    return sum;
}

int main(void) {
    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        scanf("%s", arrInput[i]);

        saveInputToMap(arrInput[i]);
    }

    assignValueToAlphabet();

    printf("%lld\n", calculateSum());
    return 0;
}

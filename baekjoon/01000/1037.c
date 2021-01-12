#include <stdio.h>

int main(void) {
    int num, min_idx, tmp;
    int arr[50];

    scanf("%d", &num);
    for(int i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    for(int i = 0; i < num - 1; i++) {
        min_idx = i;
        for(int j = i + 1; j < num; j++) {
            if(arr[j] < arr[min_idx]) min_idx = j;
        }
        
        tmp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = tmp;
    }

    if(num == 1) printf("%d\n", arr[0] * arr[0]);
    else printf("%d\n", arr[0] * arr[num - 1]);

    return 0;
}
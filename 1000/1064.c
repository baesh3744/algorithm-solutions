#include <stdio.h>
#include <math.h>

double distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow((double)(x1 - x2), 2) + pow((double)(y1 - y2), 2));
}

int main(void) {
    int xa, ya, xb, yb, xc, yc;
    double max_len, min_len;

    scanf("%d %d %d %d %d %d", &xa, &ya, &xb, &yb, &xc, &yc);

    if((xb - xa) * (yc - ya) == (xc - xa) * (yb - ya)) printf("-1\n");
    else {
        double ab = distance(xa, ya, xb, yb);
        double ac = distance(xa, ya, xc, yc);
        double bc = distance(xb, yb, xc, yc);

        max_len = ab > ac ? ab : ac;
        max_len = max_len > bc ? max_len : bc;
        
        min_len = ab > ac ? ac : ab;
        min_len = min_len > bc ? bc : min_len;

        printf("%.10lf\n", (max_len - min_len) * 2);
    }

    return 0;
}
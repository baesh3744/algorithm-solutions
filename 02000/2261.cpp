#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <vector>
using namespace std;

struct Point {
    int x, y;
    Point() {
    }
    Point(int x, int y) : x(x), y(y) {
    }
    bool operator < (const Point &v) const {
        if(y == v.y) {
            return x < v.x;
        } else {
            return y < v.y;
        }
    }
};

bool cmp(const Point &p1, const Point &p2) {
    return p1.x < p2.x;
}

int dist(Point p1, Point p2) {
    return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y);
}

int main(void) {
    int n;
    scanf("%d", &n);
    
    vector<Point> dots(n);
    for(int i = 0; i < n; i++) {
        scanf("%d %d", &dots[i].x, &dots[i].y);
    }

    sort(dots.begin(), dots.end(), cmp);

    set<Point> candidate = { dots[0], dots[1] };
    int min_dist = dist(dots[0], dots[1]);
    int start = 0;
    for(int i = 2; i < n; i++) {
        Point now = dots[i];

        while(start < i) {
            auto p = dots[start];
            int x = now.x - p.x;
            if(min_dist < x*x) {
                candidate.erase(p);
                start += 1;
            } else {
                break;
            }
        }

        int d = (int)sqrt((double)min_dist)+1;
        auto lower_point = Point(-100000, now.y-d);
        auto upper_point = Point(100000, now.y+d);
        auto lower = candidate.lower_bound(lower_point);
        auto upper = candidate.upper_bound(upper_point);

        for(auto it = lower; it != upper; it++) {
            int d = dist(now, *it);
            if(d < min_dist) min_dist = d;
        }

        candidate.insert(now);
    }

    printf("%d\n", min_dist);

    return 0;
}

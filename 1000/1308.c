#include <stdio.h>

int isLeapYear(int year) {
    if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0)) return 1;
    return 0;
}

int countDay(int year, int month, int day) {
    int total = 0;
    int month_day[] = {29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    for(int y = 1; y < year; y++) {
        if(isLeapYear(y) == 1) total += 366;
        else total += 365;
    }
    for(int m = 1; m < month; m++) {
        if(m == 2 && isLeapYear(year) == 1) total += month_day[0];
        else total += month_day[m];
    }
    total += day;

    return total;
}

int main(void) {
    int year, month, day, d_year, d_month, d_day;

    scanf("%d %d %d", &year, &month, &day);
    scanf("%d %d %d", &d_year, &d_month, &d_day);

    if(d_year - year >= 1000 && d_month >= month && d_day >= day) printf("gg\n");
    else printf("D-%d\n", countDay(d_year, d_month, d_day) - countDay(year, month, day));

    return 0;
}
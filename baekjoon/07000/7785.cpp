#include <iostream>
#include <set>
#include <string>
using namespace std;

int main(void) {
    int n;
    string name, eorl;
    set<string> name_set;

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> name >> eorl;

        if(eorl.compare("enter") == 0) name_set.insert(name);
        else name_set.erase(name);
    }

    for(set<string>::reverse_iterator riter = name_set.rbegin(); riter != name_set.rend(); riter++) {
        cout << *riter << '\n';
    }

    return 0;
}
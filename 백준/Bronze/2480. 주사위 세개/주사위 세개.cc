#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int A, B, C;
    int money;
    
    cin >> A >> B >> C;
    
    if (A != B && A != C && B != C) {
        int maximum = max({A, B, C});
        cout << maximum * 100;
    }
    else if (A == B && A == C) {
        cout << 10000 + A * 1000;
    }
    else if (A == B || A == C) {
        cout << 1000 + A * 100;
    }
    else {
        cout << 1000 + B * 100;
    }
    return 0;
}
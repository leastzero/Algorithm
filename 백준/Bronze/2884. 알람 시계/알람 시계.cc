#include <iostream>
using namespace std;

int main() {
    int H, M;
    cin >> H >> M;
    if (M - 45 < 0) {
        H = H - 1;
        M = 60 - 45 + M;
    }
    else {
        M = M - 45;
    }
    if (H < 0) {
        H = 23;
    }
    cout << H << " " << M;
    return 0;
}
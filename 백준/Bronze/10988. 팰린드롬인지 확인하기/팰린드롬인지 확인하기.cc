#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string S, RS;
    cin >> S;
    
    RS = S;
    reverse(RS.begin(), RS.end());
    
    if (RS == S) {
        cout << "1";
    } else {
        cout << "0";
    }
    return 0;
}
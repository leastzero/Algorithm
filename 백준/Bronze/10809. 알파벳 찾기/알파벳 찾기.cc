#include <iostream>
using namespace std;

int main() {
    string S;
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    cin >> S;
    for (int i = 0; i < alpha.length(); i++) {
        cout << (int)S.find(alpha[i]) << " ";
    }
    return 0;
}
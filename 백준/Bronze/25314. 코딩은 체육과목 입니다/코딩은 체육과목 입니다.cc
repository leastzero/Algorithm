#include <iostream>
using namespace std;

int main() {
    int N;
    string byte;
    cin >> N;
    
    for (int i = 0; i < N; i += 4) {
        byte += "long ";
    }
    cout << byte + "int";
    return 0;
}
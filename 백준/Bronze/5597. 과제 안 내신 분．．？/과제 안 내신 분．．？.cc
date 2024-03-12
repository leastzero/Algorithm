#include <iostream>
using namespace std;

int main() {
    int number;
    int array[31] = { 0 };
    for (int i = 0; i < 28; i++) {
        cin >> number;
        array[number] = 1;
    }
    
    for (int j = 1; j <= 30; j++) {
        if (!array[j]) {
            cout << j << "\n";
        }
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int number;
    int diff = 0;
    int array[42] = { 0 };
    for (int i = 0; i < 10; i++) {
        cin >> number;
        array[number % 42]++;
    }
    
    for (int j = 0; j < 42; j++) {
        if (array[j] != 0) {
            diff++;
        }
    }
    cout << diff;
    return 0;
}
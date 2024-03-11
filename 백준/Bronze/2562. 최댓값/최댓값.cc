#include <iostream>
using namespace std;

int main() {
    int array[9], number;
    int max = -1;
    for (int i = 0; i < 9; i++) {
        cin >> array[i];
        if (array[i] > max) {
            max = array[i];
            number = i;
        }
    }
    cout << max << "\n" << number + 1;
    return 0;
}
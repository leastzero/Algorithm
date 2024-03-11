#include <iostream>
using namespace std;

int main() {
    int N, v;
    int number = 0;
    cin >> N;
    int* array = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }
    cin >> v;
    for (int j = 0; j < N; j++) {
        if (array[j] == v) {
            number += 1;
        }
    }
    cout << number;
    return 0;
}
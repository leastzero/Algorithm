#include <iostream>
using namespace std;

int main() {
    int N, min, max;
    cin >> N;
    
    int* array = new int[N];
    
    for (int i = 0; i < N; i++) {
        cin >> array[i];
        min = array[0];
        max = array[0];
    }
    for (int j = 0; j < N; j++) {
        if (array[j] < min) {
            min = array[j];
        }
        if (array[j] > max) {
            max = array[j];
        }
    }
    cout << min << " " << max;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    
    int* array = new int[N];
    
    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }
    for (int j = 0; j < N; j++) {
        if (array[j] < X) {
            cout << array[j] << " ";
        }
    }
    return 0;
}
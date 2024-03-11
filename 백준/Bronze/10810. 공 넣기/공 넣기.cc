#include <iostream>
using namespace std;

int main() {
    int N, M, i, j, k;
    cin >> N >> M;
    
    int* array = new int[N];
    for (int r = 0; r < N; r++) {
        array[r] = 0;
    }
    for (int t = 0; t < M; t++) {
        cin >> i >> j >> k;
        for (i; i <= j; i++) {
            array[i - 1] = k;
        }
    }
    for (int e = 0; e < N; e++) {
        cout << array[e] << " ";
    }
    delete[] array;
    return 0;
}
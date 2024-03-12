#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M, i, j;
    cin >> N >> M;
    
    int* array = new int[N + 1];
    for (int t = 1; t <= N; t++) {
        array[t] = t;
    }
    for (int r = 0; r < M; r++) {
        cin >> i >> j;
        reverse(array + i, array + j + 1);
    }
    for (int e = 1; e <= N; e++) {
        cout << array[e] << " ";
    }
    
    delete[] array;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N, M, i, j, k;
    cin >> N >> M;
    
    int* array = new int[N];
    for (int r = 0; r < N; r++) {
        array[r] = r+1;
    }
    for (int t = 0; t < M; t++) {
        cin >> i >> j;
        k = array[i-1];
        array[i-1] = array[j-1];
        array[j-1] = k;
    }
    for (int e = 0; e < N; e++) {
        cout << array[e] << " ";
    }
    delete[] array;
    return 0;
}
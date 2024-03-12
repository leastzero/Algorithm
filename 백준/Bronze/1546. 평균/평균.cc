#include <iostream>
using namespace std;

int main() {
    int N;
    double score, A;
    double M = 0;
    double sum = 0;
    cin >> N;
    
    double* array = new double[N];
    for (int i = 0; i < N; i++) {
        cin >> score;
        array[i] = score;
    }
    for (int j = 0; j < N; j++) {
        if (array[j] > M) {
            M = array[j];
        }
    }
    for (int t = 0; t < N; t++) {
        array[t] = array[t] / M * 100;
        sum += array[t];
    }
    A = sum / N;
    cout << A;
    
    delete[] array;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    string* array = new string[T];
    
    for (int i = 0; i < T; i++) {
        cin >> array[i];
    }
    for (int j = 0; j < T; j++) {
        cout << array[j].front() << array[j].back() << "\n";
    }
    
    delete[] array;
    return 0;
}
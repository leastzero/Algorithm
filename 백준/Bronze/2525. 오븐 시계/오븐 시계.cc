#include <iostream>
using namespace std;

int main() {
    int A, B, C;
    int hour;
    cin >> A >> B;
    cin >> C;
    
    hour = A * 60 + B;
    hour += C;
    
    A = (hour / 60) % 24;
    B = hour % 60;
    
    cout << A << " " << B;
    return 0;
}
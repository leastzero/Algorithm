#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string S;
    getline(cin, S);
    
    stringstream ss(S);
    string words;
    int count = 0;
    
    while (ss >> words) {
        count++;
    }
    
    cout << count;
    return 0;
}
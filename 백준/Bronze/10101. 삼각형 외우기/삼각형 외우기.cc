#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> angle(3);
	for (int i = 0; i < 3; i++) {
		cin >> angle[i];
	}

	int sum = 0;
	for (int i = 0; i < 3; i++) {
		sum += angle[i];
	}

	if (sum != 180) {
		cout << "Error";
	}
	else if (angle[0] == angle[1] && angle[1] == angle[2]) {
		cout << "Equilateral";
	}
	else if (angle[0] == angle[1] || angle[1] == angle[2] || angle[0] == angle[2]) {
		cout << "Isosceles";
	}
	else {
		cout << "Scalene";
	}

	return 0;
}

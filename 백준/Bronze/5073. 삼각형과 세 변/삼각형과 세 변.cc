#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int> length(3);

	while (true) {
		cin >> length[0] >> length[1] >> length[2];
		if (length[0] == 0) break;

		sort(length.begin(), length.end());

		if (length[2] >= length[0] + length[1]) {
			cout << "Invalid" << endl;
		}
		else if (length[0] == length[1] && length[1] == length[2]) {
			cout << "Equilateral" << endl;
		}
		else if (length[0] == length[1] || length[1] == length[2] || length[0] == length[2]) {
			cout << "Isosceles" << endl;
		}
		else {
			cout << "Scalene" << endl;
		}
	}

	return 0;
}

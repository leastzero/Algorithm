#include <iostream>
using namespace std;

int main() {
	int array[9][9];
	int max = -1, c = 0, r = 0;

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> array[i][j];
		}
	}

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (array[i][j] > max) {
				max = array[i][j];
				c = i + 1;
				r = j + 1;
			}
		}
	}

	cout << max << "\n";
    cout << c << " " << r;

	return 0;
}
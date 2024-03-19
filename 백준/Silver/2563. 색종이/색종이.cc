#include <iostream>
using namespace std;

int main() {
	int count, x, y;
	int sum = 0;
	cin >> count;

	int paper[100][100] = { 0 };

	while (count--) {
		cin >> x >> y;
		for (int i = y; i < y + 10; i++) {
			for (int j = x; j < x + 10; j++) {
				if (paper[i][j]) continue;
				paper[i][j] = 1;
				sum++;
			}
		}
	}

	cout << sum;

	return 0;
}
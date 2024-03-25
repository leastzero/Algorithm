#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N, B;
	string ten;
	cin >> N >> B;

	while (N > 0) {
		int r = N % B;
		if (0 <= r && r <= 9) {
			ten += r + '0';
		}
		else {
			ten += r - 10 + 'A';
		}
		N = N / B;
	}

	reverse(ten.begin(), ten.end());

	cout << ten;
	return 0;
}
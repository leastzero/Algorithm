#include <iostream>
using namespace std;

int main() {
	int T, C;
	double Q, D, N, P;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> C;
		int r = C;

		Q = r / 25;
		D = r % 25 / 10;
		N = r % 25 % 10 / 5;
		P = r % 25 % 10 % 5 / 1;
		cout << Q << " " << D << " " << N << " " << P << "\n";
	}
	return 0;
}
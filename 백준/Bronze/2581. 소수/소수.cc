#include <iostream>
#include <vector>
using namespace std;

int main() {
	int M, N, ss = 0, sum = 0, min = 10000;
	cin >> M;
	cin >> N;

	vector<int> sosu;

	for (M; M <= N; M++) {
		for (int j = 1; j <= M; j++) {
			if (M % j == 0) {
				ss = M / j;
				sosu.push_back(ss);
			}
		}
		if (sosu.size() == 2) {
			if (min > M) min = M;
			sum += M;
		}
		sosu.clear();
	}

	if (sum == 0) {
		cout << "-1";
	}
	else {
		cout << sum << endl << min;
	}

	return 0;
}
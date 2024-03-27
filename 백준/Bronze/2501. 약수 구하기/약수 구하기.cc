#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, K, count = 0;
	cin >> N >> K;

	vector<int> factor;
	for (int i = 1; i <= N; i++) {
		if (N % i == 0) {
			factor.push_back(i);
			count++;
		}
	}

	if (count < K) {
		cout << "0";
	}
	else {
		cout << factor[K - 1];
	}
	return 0;
}
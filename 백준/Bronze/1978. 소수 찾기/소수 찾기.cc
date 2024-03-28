#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, s, count = 0;
	cin >> N;

	vector<int> sosu;

	for (int i = 0; i < N; i++) {
		cin >> s;
		for (int j = 1; j <= s; j++) {
			if (s % j == 0) {
				int ss = s / j;
				sosu.push_back(ss);
			}
		}
		if (sosu.size() == 2) count++;
		sosu.clear();
	}

	cout << count;
	return 0;
}
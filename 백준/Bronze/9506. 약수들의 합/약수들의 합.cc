#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, fac = 0;
	vector<int> factor;

	while (true) {
		int sum = 0;
		cin >> n;
		if (n == -1) break;

		for (int i = 2; i <= n; i++) {
			if (n % i == 0) {
				fac = n / i;
				factor.push_back(fac);
				sum += fac;
			}
		}

		sort(factor.begin(), factor.end());

		if (sum == n) {
			cout << n << " = ";
			for (int i = 0; i < factor.size(); i++) {
				if (i != factor.size()-1) cout << factor[i] << " + ";
				else cout << factor[i] << endl;
			}
		}
		else {
			cout << n << " is NOT perfect." << endl;
		}
		factor.clear();
	}
	return 0;
}
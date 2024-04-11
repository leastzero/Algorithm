#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, sum, final_sum = 0;
	cin >> N >> M;

	int card[100] = { 0 };

	for (int i = 0; i < N; i++) {
		cin >> card[i];
	}

	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			for (int k = j + 1; k < N; k++) {
				sum = card[i] + card[j] + card[k];
				if (sum <= M && sum > final_sum) final_sum = sum;
			}
		}
	}

	cout << final_sum;
	return 0;
}

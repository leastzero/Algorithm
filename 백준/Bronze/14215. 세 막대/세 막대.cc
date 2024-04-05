#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int> length(3);

	cin >> length[0] >> length[1] >> length[2];

	sort(length.begin(), length.end());

	if (length[2] < length[0] + length[1]) {
		cout << length[0] + length[1] + length[2];
	}
	else {
		cout << 2 * (length[0] + length[1]) - 1;
	}

	return 0;
}

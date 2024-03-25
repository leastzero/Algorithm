#include <iostream>
using namespace std;

int main() {
	int N;
	int result = 2;
	cin >> N;

	while (N--)
		result = result * 2 - 1;

	cout << result * result;
	return 0;
}
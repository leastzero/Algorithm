#include <iostream>
using namespace std;

int main() {
	string N;
	int B;
	int ten = 0;
	cin >> N >> B;

	for (int i = 0; i < N.length(); i++) {
		if ('0' <= N[i] && N[i] <= '9') {
			ten = ten * B + (N[i] - '0');
		}
		else {
			ten = ten * B + (N[i] - 'A' + 10);
		}
	}

	cout << ten;
	return 0;
}
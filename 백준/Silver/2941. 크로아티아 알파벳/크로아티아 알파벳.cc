#include <iostream>
using namespace std;

int main() {
	string S;
	cin >> S;

	int count = S.length();

	for (int i = 0; i < S.length(); i++) {
		if (i + 2 < S.length() && S.substr(i, 3) == "dz=") {
			count -= 1;
		}
		else if (i + 1 < S.length() && S.substr(i, 2) == "c=" ||
			i + 1 < S.length() && S.substr(i, 2) == "c-" ||
			i + 1 < S.length() && S.substr(i, 2) == "d-" ||
			i + 1 < S.length() && S.substr(i, 2) == "lj" ||
			i + 1 < S.length() && S.substr(i, 2) == "nj" ||
			i + 1 < S.length() && S.substr(i, 2) == "s=" ||
			i + 1 < S.length() && S.substr(i, 2) == "z=") {
			count -= 1;
		}
	}

	cout << count;
	return 0;
}
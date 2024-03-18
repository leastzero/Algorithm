#include <iostream>
using namespace std;

int main() {
	string S;
	cin >> S;

	int alpha[26] = { 0 };

	for (int i = 0; i < S.length(); i++) {
		S[i] = toupper(S[i]);
		alpha[S[i] - 65]++;
	}

	int max = 0, index = 0, count = 0;

	for (int i = 0; i < 26; i++) {
		if (max < alpha[i]) {
			max = alpha[i];
			index = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		if (max == alpha[i]) {
			count++;
		}
	}

	if (count > 1) cout << "?";
	else cout << (char)(index + 65);


	return 0;
}
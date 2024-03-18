#include <iostream>
using namespace std;

int main() {
	int count;
	cin >> count;

	string* word = new string[count];

	for (int i = 0; i < count; i++) {
		cin >> word[i];
	}

	int group = 0;

	for (int i = 0; i < count; i++) {
		bool check = true;
		for (int j = 0; j < word[i].length(); j++) {
			for (int k = 0; k < j; k++) {
				if (word[i][j] != word[i][j - 1] && word[i][j] == word[i][k]) {
					check = false;
					break;
				}
			}
		}
		if (check) group++;
	}

	cout << group;

	delete[] word;
	return 0;
}
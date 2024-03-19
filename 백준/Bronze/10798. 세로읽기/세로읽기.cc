#include <iostream>
using namespace std;

int main() {
	string array[5];

	for (int i = 0; i < 5; i++) {
		cin >> array[i];
	}

	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 5; j++) {
			if (i < array[j].size())
				cout << array[j][i];
		}
	}

	return 0;
}
#include <iostream>
using namespace std;

int main() {
	int X;
	cin >> X;

	int d = 1, count = 0;

	while (X > count + d) {
		count += d;
		d++;
	}

	if (d % 2 == 1) {
		int a = d - (X - count - 1);
		int b = X - count;
		cout << a << "/" << b;
	}
	else {
		int a = X - count;
		int b = d - (X - count - 1);
		cout << a << "/" << b;
	}
	return 0;
}
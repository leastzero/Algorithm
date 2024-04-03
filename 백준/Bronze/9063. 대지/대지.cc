#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> x(N);
	vector<int> y(N);

	for (int i = 0; i < N; i++) {
		cin >> x[i] >> y[i];
	}

	int maxx = -10000, minx = 10000;
	int maxy = -10000, miny = 10000;

	for (int i = 0; i < N; i++) {
		if (x[i] > maxx) maxx = x[i];
		if (x[i] < minx) minx = x[i];
		if (y[i] > maxy) maxy = y[i];
		if (y[i] < miny) miny = y[i];
	}

	int s = 0;
	s = (maxx - minx) * (maxy - miny);

	cout << s;

	return 0;
}
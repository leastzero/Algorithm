#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int x, y, w, h;
	cin >> x >> y >> w >> h;

	vector<int> distance;

	distance.push_back(w - x);
	distance.push_back(x);
	distance.push_back(h - y);
	distance.push_back(y);

	sort(distance.begin(), distance.end());

	cout << distance[0];

	return 0;
}
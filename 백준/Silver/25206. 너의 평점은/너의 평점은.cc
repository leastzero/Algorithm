#include <iostream>
using namespace std;

int main() {
	string subject, grade;
	double score;
	double sum = 0, score_sum = 0;

	for (int i = 0; i < 20; i++) {
		cin >> subject >> score >> grade;
		if (grade == "A+") {
			sum += score * 4.5;
			score_sum += score;
		}
		else if (grade == "A0") {
			sum += score * 4.0;
			score_sum += score;
		}
		else if (grade == "B+") {
			sum += score * 3.5;
			score_sum += score;
		}
		else if (grade == "B0") {
			sum += score * 3.0;
			score_sum += score;
		}
		else if (grade == "C+") {
			sum += score * 2.5;
			score_sum += score;
		}
		else if (grade == "C0") {
			sum += score * 2.0;
			score_sum += score;
		}
		else if (grade == "D+") {
			sum += score * 1.5;
			score_sum += score;
		}
		else if (grade == "D0") {
			sum += score * 1.0;
			score_sum += score;
		}
		else if (grade == "F") {
			sum += score * 0.0;
			score_sum += score;
		}
	}

	cout << sum / score_sum;
	return 0;
}
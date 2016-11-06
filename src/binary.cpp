#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <functional>
#include <array>

using namespace std;

//string words [9902];
array<string, 9902> words;

void setUpArray(){
	string line;
	ifstream file ("words.txt");
	int count = 0;
	while (getline (file,line)) {
		words[count] = line;
		count++;
	}
	file.close();
	sort(words.begin(), words.end());
}

int round(double num) {
	if( (num + 0.5) >= (int(num) + 1) ){
		return int(num)+1;
	} else {
		return int(num);
	}
}

int binSearch(array<string, 9902> arr, string val, double pos) {
	if (arr[round(pos)] > val) {
		int x = round(pos / 2);
		return binSearch(arr, val, pos - x);
	} else if (arr[round(pos)] < val) {
		int x = round(pos / 2);
		return binSearch(arr, val, pos + x);
	} else {
		return pos;
	}
}

int main () {
	setUpArray();
//	array<string, 10> kek= {"aa", "abc", "fe", "ghe", "hgc", "ldjc", "ldjd", "uyr", "yzx", "zzx"};
	cout << binSearch(words, "latvia", round(words.size() / 2)) << endl;
	return 0;
}

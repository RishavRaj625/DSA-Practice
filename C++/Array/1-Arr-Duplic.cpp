// Finding the Duplicate number

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> findDuplicates(vector<int>& arr) {
        vector<int> result;

        for (int i = 0; i < arr.size(); i++) {
            int index = abs(arr[i]) - 1;

            if (arr[index] < 0) {
                result.push_back(abs(arr[i]));
            } else {
                arr[index] = -arr[index];
            }
        }
        return result;
    }
};

int main(){
    vector<int> arr = {2, 3, 1, 2, 3};
    Solution sol;
    vector<int> duplicates = sol.findDuplicates(arr);

    cout << "Duplicates: ";
    for (int num : duplicates) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}

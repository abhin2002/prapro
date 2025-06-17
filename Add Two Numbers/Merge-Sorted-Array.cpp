#include <iostream>
using namespace std;
#include <vector>

class Solution {
    public:
        void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
            int i = m - 1; // Pointer for nums1
            int j = n - 1; // Pointer for nums2
            int k = m + n - 1; // Pointer for merged array

            while (i >= 0 && j >= 0) {
                if (nums1[i] > nums2[j]) {
                    nums1[k--] = nums1[i--];
                } else {
                    nums1[k--] = nums2[j--];
                }
            }

            // If there are remaining elements in nums2, copy them
            while (j >= 0) {
                nums1[k--] = nums2[j--];
            }
            // No need to copy remaining elements from nums1, they are already in place
        }
    };


int main() {
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2,5,6};
    int m = 3;
    int n = 3;
    Solution s;
    s.merge(nums1, m, nums2, n);
    cout << "Merged array: ";
    for (int i = 0; i < m + n; i++) {
        cout << nums1[i] << " ";
    }
    
    cout << endl;
    return 0;
}

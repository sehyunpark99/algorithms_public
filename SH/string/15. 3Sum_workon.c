#include <stdlib.h>

/*
We advance a integer pointer called i from 0→n−20 \rightarrow n-20→n−2. This represents the first number of our sum. Then we use two pointers l and r. l is incremented when the sum of the three pointers is too low, and r is decremented when the sum is too high. Eventually l and r converge to a point where nums[i] + nums[l] + nums[r] == 0. At this point we come across a solution. Afterward, we keep incrementing l in case another solution comes up which is possible:

e.g [-3,-2,-1,0,4,5] we have a solution [-3,-2,5] but [-3,-1,4] also works.

But to avoid duplicates we need to increment further l in the case that there are duplicates of nums[l]. We also skip nums[i] using continue if we come across a duplicate for the i pointer also. It's not possible for r to have a duplicate because assuming i and l are unique there can only be a unique r that sums to 000.
*/

// To compare
int cmp(const void *a,const void *b) {
    return *((int*) a) - *((int*) b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    qsort(nums, numsSize, sizeof(int), cmp);
    (*returnSize) = 0;
    (*returnColumnSizes) = (int*) malloc(sizeof(int) * numsSize * numsSize);
    int **ret = (int**) malloc(sizeof(int*) * numsSize * numsSize);
    for (int i = 0; i < numsSize - 2; i++) {
        if (i == 0 || nums[i] != nums[i-1]) {
            int l = i + 1;
            int r = numsSize - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } else if (nums[i] + nums[l] + nums[r] > 0) {
                    r--;
                } else {
                    ret[(*returnSize)] = (int*) malloc(sizeof(int) * 3);
                    (*returnColumnSizes)[(*returnSize)] = 3;
                    ret[(*returnSize)][0] = nums[i];
                    ret[(*returnSize)][1] = nums[l];
                    ret[(*returnSize)][2] = nums[r];
                    (*returnSize)++;
                    l++;
                    while (l < r && nums[l] == nums[l-1])
                        l++;
                }
            }
        }
    }
    return ret;
}
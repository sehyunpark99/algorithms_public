#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int longestConsecutive(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }

    qsort(nums, numsSize, sizeof(int), compare);

    int cnt = 1;
    int maxi = 0;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) {
            if (nums[i] == nums[i - 1] + 1) {
                cnt++;
            } else {
                maxi = (maxi > cnt) ? maxi : cnt;
                cnt = 1;
            }
        }
    }

    return (maxi > cnt) ? maxi : cnt;
}

int main() {
    int nums[] = {100, 4, 200, 1, 3, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    printf("Longest consecutive sequence length: %d\n", longestConsecutive(nums, numsSize));
    return 0;
}

struct Solution {
    int (*containsNearbyDuplicate)(int*, int, int);
};

int containsNearbyDuplicate(int* nums, int numsSize, int k) {
    int* window = (int*)malloc(k * sizeof(int));
    int windowSize = 0;

    for (int i = 0; i < numsSize; i++) {
        if (i > k) {
            windowSize--;
        }
        for (int j = windowSize - 1; j >= 0; j--) {
            if (window[j] == nums[i]) {
                free(window);
                return 1;
            }
        }
        window[windowSize++] = nums[i];
    }
    free(window);
    return 0;
}
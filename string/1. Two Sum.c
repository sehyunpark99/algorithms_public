int* twoSum(int* nums, int numsSize, int target) {
  int* ret = (int *)malloc(2 * sizeof(int));
  for (ret[0] = 0; ret[0] < numsSize; ++ret[0]) {
    for (ret[1] = ret[0] + 1; ret[1] < numsSize; ++ret[1]) {
      if (nums[ret[0]] + nums[ret[1]] == target) {
        return ret;
      }
    }
  }
  return ret;
}
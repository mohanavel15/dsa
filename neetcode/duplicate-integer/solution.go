package main

func hasDuplicate(nums []int) bool {

	seen := map[int]bool{}

	for i := range len(nums) {
		if _, ok := seen[nums[i]]; ok {
			return true
		}

		seen[nums[i]] = true
	}

	return false
}

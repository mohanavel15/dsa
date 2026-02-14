package main

func twoSum(nums []int, target int) []int {
	mappings := map[int]int{}

	for idx := range len(nums) {
		if idx2, ok := mappings[target-nums[idx]]; ok {
			return []int{idx2, idx}
		}

		mappings[nums[idx]] = idx
	}

	return []int{}
}

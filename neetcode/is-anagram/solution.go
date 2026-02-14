package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	freq := [26]int{}

	for idx := range len(s) {
		freq[s[idx]-'a'] += 1
		freq[t[idx]-'a'] -= 1
	}

	for idx := range 26 {
		if freq[idx] != 0 {
			return false
		}
	}

	return true
}

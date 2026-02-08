package main

import "fmt"

func main() {
	var username string

	fmt.Scanln(&username)

	var alphabets [26]bool
	unique := 0

	for _, c := range username {
		if !alphabets[c-'a'] {
			alphabets[c-'a'] = true
			unique += 1
		}

	}

	if unique%2 == 0 {
		fmt.Println("CHAT WITH HER!")
	} else {
		fmt.Println("IGNORE HIM!")
	}
}

package main

import "fmt"

func main() {
	var n int
	var word string

	fmt.Scanln(&n)

	for _ = range n {
		fmt.Scanln(&word)

		ln := len(word)

		if ln <= 10 {
			fmt.Println(word)
		} else {
			fmt.Printf("%c%d%c\n", word[0], ln-2, word[ln-1])
		}
	}
}

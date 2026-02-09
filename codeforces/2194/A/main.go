package main

import "fmt"

func main() {
	var t int
	fmt.Scanln(&t)

	var n int
	var w int

	for _ = range t {
		fmt.Scanln(&n, &w)

		max_hole := w - 1
		if max_hole <= 0 {
			fmt.Println(0)
			continue
		}

		removed := (n/w)*max_hole + (n % w)

		fmt.Println(removed)
	}
}

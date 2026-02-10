package main

import "fmt"

func main() {
	var a, b int

	fmt.Scanln(&a, &b)
	years := 0

	for {
		years += 1
		a *= 3
		b *= 2
		if a > b {
			break
		}
	}

	fmt.Println(years)
}

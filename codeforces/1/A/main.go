package main

import "fmt"

func main() {
	var n, m, a int

	fmt.Scanln(&n, &m, &a)

	n_a := n / a
	if n%a != 0 {
		n_a += 1
	}

	m_a := m / a

	if m%a != 0 {
		m_a += 1
	}

	fmt.Println(n_a * m_a)
}

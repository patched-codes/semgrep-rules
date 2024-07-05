// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import "fmt"

var vector []*string

func appendVector(s *string) {
	vector = append(vector, s)
}

func printVector() {
	for _, item := range vector {
		fmt.Printf("%s", *item)
	}
	fmt.Println()
}

func foo() (int, **string, *string) {
	for _, item := range vector {
		return 0, &item, item
	}
	return 0, nil, nil
}

func appendrange() {
	// ruleid:go_memory_rule-memoryaliasing
	for _, item := range []string{"A", "B", "C"} {
		appendVector(&item)
	}

	printVector()

	zero, c_star, c := foo()
	fmt.Printf("%d %v %s", zero, c_star, c)
}

func saferange() {
	sampleMap := map[string]string{}
	sampleString := "A string"
	for sampleString = range sampleMap {
		fmt.Println(sampleString)
	}
}

func safeiter() {
	// ok:go_memory_rule-memoryaliasing
	array := []string{"a", "b"}
	for i := range array {
		appendVector(&array[i])
	}
}

// https://gitlab.com/gitlab-org/gitlab/-/issues/348952
// ok:go_memory_rule-memoryaliasing
func shouldNotBeReported() {
	array := []string{"a", "b"}
	for _, s := range array {
		fmt.Println(s)
	}
}

func shouldBeReported() {
	array := []string{"a", "b"}
	// ruleid:go_memory_rule-memoryaliasing
	for i, s := range array {
		fmt.Printf("%d %p\n", i, &s)
	}
}

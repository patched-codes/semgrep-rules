// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"fmt"
	"strconv"
)

func foo1() {
	// ruleid: go_memory_rule-integer-overflow
	bigValue, _ := strconv.Atoi("2147483648"); value := int32(bigValue)
	fmt.Println(value)
}

func foo2() {
	// ruleid: go_memory_rule-integer-overflow
	bigValue, _ := strconv.Atoi("32768"); if int16(bigValue) < 0 { fmt.Println(bigValue) }
}

func foo3() {
	bigValue, err := strconv.Atoi("2147483648")
	if err != nil {
		panic(err)
	}
	fmt.Println(bigValue)
}

func foo4() {
	bigValue, err := strconv.Atoi("2147483648")
	if err != nil {
		panic(err)
	}
	fmt.Println(bigValue)
	test()
}

func test() {
	bigValue := 30
	value := int32(bigValue)
	fmt.Println(value)
}

func foo5() {
	value := 10
	if value == 10 {
		value, _ := strconv.Atoi("2147483648")
		fmt.Println(value)
	}
	v := int32(value)
	fmt.Println(v)
}

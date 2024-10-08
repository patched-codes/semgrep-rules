// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"fmt"
	"os"
)

func foo0() {
	err := os.Mkdir("/tmp/mydir", 0700)
	if err != nil {
		fmt.Println("Error when creating a directory!")
		return
	}
}

func foo1() {
	// ruleid: go_file-permissions_rule-mkdir
	err := os.Mkdir("/tmp/mydir", 0777)
	if err != nil {
		fmt.Println("Error when creating a directory!")
		return
	}
}

func foo2() {
	// ruleid: go_file-permissions_rule-mkdir
	err := os.MkdirAll("/tmp/mydir", 0777)
	if err != nil {
		fmt.Println("Error when creating a directory!")
		return
	}
}

func foo3() {
	err := os.Mkdir("/tmp/mydir", 0600)
	if err != nil {
		fmt.Println("Error when creating a directory!")
		return
	}
}

func foo4() {
	err := os.Mkdir("/tmp/mydir", 0750)
	if err != nil {
		fmt.Println("Error when creating a directory!")
		return
	}
}

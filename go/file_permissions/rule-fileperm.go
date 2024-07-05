// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"fmt"
	"os"
)

func foo1() {
	// ruleid:go_file-permissions_rule-fileperm
	err := os.Chmod("/tmp/somefile", 0777)
	if err != nil {
		fmt.Println("Error when changing file permissions!")
		return
	}
}

func foo2() {
	// ruleid:go_file-permissions_rule-fileperm
	_, err := os.OpenFile("/tmp/thing", os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		fmt.Println("Error opening a file!")
		return
	}
}

func foo3() {
	// ruleid:go_file-permissions_rule-fileperm
	err := os.WriteFile("/tmp/thing", []byte("Hello, World!"), 0o666)
	if err != nil {
		fmt.Println("Error writing file")
		return
	}
}

func foo4() {
	// ok:go_file-permissions_rule-fileperm
	_, err := os.OpenFile("/tmp/thing", os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		fmt.Println("Error opening a file!")
		return
	}
}

func foo5() {
	// ok:go_file-permissions_rule-fileperm
	err := os.Chmod("/tmp/mydir", 0400)
	if err != nil {
		fmt.Println("Error")
		return
	}
}

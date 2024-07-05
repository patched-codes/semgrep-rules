// License: Apache 2.0
package main

// ruleid: go_blocklist_rule-blocklist-sha1
import (
	"crypto/sha1"
	"fmt"
)

func mainSHA1() {
	h := sha1.New()
	h.Write([]byte("stuff"))
}

func mainSHA1Sum() {
	out := sha1.Sum([]byte("stuff"))
	fmt.Println(out)
}

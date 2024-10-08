// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

// ruleid: go_blocklist_rule-blocklist-des
import (
	"crypto/des"
	"fmt"
)

func maindes() {
	k := []byte("super secret key")
	block, err := des.NewCipher(k)
	if err != nil {
		return
	}
	out := make([]byte, 0)
	in := []byte("cleartext")
	block.Encrypt(out, in)
	decrypted := make([]byte, 0)
	block.Decrypt(decrypted, out)
	fmt.Printf("Doing something with: %s\n", string(decrypted))
}

func main3des() {
	k := []byte("super secret key")
	block, err := des.NewTripleDESCipher(k)
	if err != nil {
		return
	}
	out := make([]byte, 0)
	in := []byte("cleartext")
	block.Encrypt(out, in)
	decrypted := make([]byte, 0)
	block.Decrypt(decrypted, out)
	fmt.Printf("Doing something with: %s\n", string(decrypted))
}

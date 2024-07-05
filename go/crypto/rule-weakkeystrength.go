// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42
package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

func mainweakkey() {
	//Generate Private Key
	// ruleid: go_crypto_rule-weakkeystrength
	pvk, err := rsa.GenerateKey(rand.Reader, 1024)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(pvk)
}

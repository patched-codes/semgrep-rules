// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"golang.org/x/crypto/ssh"
)

func main() {
	// ruleid: go_crypto_rule-insecure-ignore-host-key
	_ = ssh.InsecureIgnoreHostKey()
}

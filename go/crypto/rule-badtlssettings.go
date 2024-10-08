// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42
package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func mainbadciphersuites() {
	tr := &http.Transport{
		// ruleid: go_crypto_rule-badtlssettings
		TLSClientConfig: &tls.Config{CipherSuites: []uint16{ tls.TLS_RSA_WITH_AES_128_GCM_SHA256, tls.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
		}},
	}

	client := &http.Client{Transport: tr}
	_, err := client.Get("https://golang.org/")
	if err != nil {
		fmt.Println(err)
	}
}

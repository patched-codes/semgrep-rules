// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
)

func bad1() {
	http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	})
	// ruleid:go_leak_rule-pprof-endpoint
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func bad2() {
	http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	})
	// ruleid:go_leak_rule-pprof-endpoint
	log.Fatal(http.ListenAndServeTLS(":8443", "cert.crt", "key.enc", nil))
}

func bad3() {
	http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	})
	// ruleid:go_leak_rule-pprof-endpoint
	log.Fatal(http.Serve(nil, nil))
}

func bad4() {
	http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	})
	// ruleid:go_leak_rule-pprof-endpoint
	log.Fatal(http.ServeTLS(nil, nil, "cert.key", "key.enc"))
}

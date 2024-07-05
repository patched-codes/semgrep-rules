// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"log"
	"net"
)

func Unsafe() {
	// ruleid:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp", "0.0.0.0:2000")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

func Unsafe_PortOmitted() {
	// ruleid:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp", "0.0.0.0")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

func Unsafe_AddressOmitted() {
	// ruleid:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

func Unsafe_IPv6() {
	// ruleid:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp6", "[::]:1234")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

func Unsafe_Ipv6PortOmitted() {
	// ruleid:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp6", "[::]")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

func Safe() {
	// ok:go_network_rule-bind-to-all-interfaces
	l, err := net.Listen("tcp", "127.0.0.1:1234")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
}

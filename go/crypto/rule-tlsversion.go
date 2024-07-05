// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42
package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
)

func bad1_tls() {
    // Setup TLS configuration
    tlsConfig := &tls.Config{
     // ruleid: go_crypto_rule-tlsversion
        MinVersion: tls.VersionTLS10, // Minimum TLS version
        MaxVersion: tls.VersionTLS13, // Maximum TLS version
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello, TLS!"))
    })

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func bad2_tls() {
    
    min := uint16(tls.VersionTLS11)
    max := uint16(tls.VersionTLS13)
    
	// Setup TLS configuration
    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MinVersion: min, // Minimum TLS version
        MaxVersion: max, // Maximum TLS version
    }

    transport := &http.Transport{
        TLSClientConfig: tlsConfig,
    }

    client := &http.Client{
        Transport: transport,
    }

    resp, err := client.Get("https://example.com")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
}

func bad3_tls() {
    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MinVersion: tls.VersionTLS11, // Only accept TLS versions 1.1 and higher
    }

    transport := &http.Transport{
        TLSClientConfig: tlsConfig,
    }

    client := &http.Client{
        Transport: transport,
    }

    resp, err := client.Get("https://example.com")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
}


func bad4_tls() {
    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MaxVersion: tls.VersionTLS11, // Accept any TLS version up to 1.1
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func bad5_tls() {

    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MaxVersion: tls.VersionTLS13, // Accept any TLS version up to 1.3
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func bad6_tls() {
    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MinVersion:               tls.VersionTLS10,
        MaxVersion:               tls.VersionTLS13,
        CipherSuites:             []uint16{tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384},
        PreferServerCipherSuites: true,
        SessionTicketsDisabled:   false,
        ClientAuth:               tls.NoClientCert,
        InsecureSkipVerify:       false,
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func bad7_tls(){
    tlsConfig := &tls.Config{
        // ruleid: go_crypto_rule-tlsversion
        MaxVersion:               tls.VersionTLS13,
        CipherSuites:             []uint16{tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384},
        PreferServerCipherSuites: true,
        SessionTicketsDisabled:   false,
        ClientAuth:               tls.NoClientCert,
        InsecureSkipVerify:       false,
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func bad8() {
    
    min := uint16(tls.VersionTLS11)
    max := uint16(tls.VersionTLS13)
    
    transport := &http.Transport{
        TLSClientConfig: &tls.Config{
            // ruleid: go_crypto_rule-tlsversion
            MinVersion: min, // Minimum TLS version
            MaxVersion: max, // Maximum TLS version
        },
    }

    client := &http.Client{
        Transport: transport,
    }

    resp, err := client.Get("https://example.com")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
}



func safe1_tls(){

    tlsConfig := &tls.Config{
     // ok: go_crypto_rule-tlsversion
        MinVersion: tls.VersionTLS12, // Minimum TLS version
        MaxVersion: tls.VersionTLS13, // Maximum TLS version
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func safe2_tls(){

    min := uint16(tls.VersionTLS12)
    max := uint16(tls.VersionTLS13)
    
	// Setup TLS configuration
    tlsConfig := &tls.Config{
        // ok: go_crypto_rule-tlsversion
        MinVersion: min, // Minimum TLS version
        MaxVersion: max, // Maximum TLS version
    }

    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
    }

    log.Println("Starting TLS server on :443")
    log.Fatal(server.ListenAndServeTLS("cert.pem", "key.pem"))
}

func safe3_tls(version string) uint16 {
	
	var tlsMinVersion uint16

	switch version {
	    case "TLS13":
			tlsMinVersion = tls.VersionTLS13
		case "TLS12":
			tlsMinVersion = tls.VersionTLS12
		case "TLS11":
            // ok: go_crypto_rule-tlsversion
			tlsMinVersion = tls.VersionTLS11
		case "TLS10":
            // ok: go_crypto_rule-tlsversion
			tlsMinVersion = tls.VersionTLS10
	}
    
	return tlsMinVersion
}


func safe4_tls() map[string]uint16{

    var SupportedTLSVersions = map[string]uint16{
	// ok: go_crypto_rule-tlsversion
    "tls1.0": tls.VersionTLS10,
    // ok: go_crypto_rule-tlsversion
	"tls1.1": tls.VersionTLS11,
	"tls1.2": tls.VersionTLS12,
	"tls1.3": tls.VersionTLS13,
    }

	return SupportedTLSVersions
}


func safe5_tls(v string) uint16 {
	switch v {
	case "1.0":
    // ok: go_crypto_rule-tlsversion
		return tls.VersionTLS10
	case "1.1":
    // ok: go_crypto_rule-tlsversion
		return tls.VersionTLS11
	case "1.2", "":
		return tls.VersionTLS12
	case "1.3":
		return tls.VersionTLS13
	default:
		log.Fatalln("error: unknown minimum TLS version:", v)
		return 0
	}
}

func safe6_tls() []struct {
    val uint16
    str string
} {
    
	var tlsVersionTable = []struct {
        val uint16
        str string
    }{
        // ok: go_crypto_rule-tlsversion
        {tls.VersionTLS10, "tls1.0"},
        // ok: go_crypto_rule-tlsversion
        {tls.VersionTLS11, "tls1.1"},
        {tls.VersionTLS12, "tls1.2"},
        {tls.VersionTLS13, "tls1.3"},
    }

	return tlsVersionTable
}

func safe7_tls(version string) (uint16, error) {
	switch version {
	case "1.0":
    // ok: go_crypto_rule-tlsversion
		return tls.VersionTLS10, nil
	case "1.1":
    // ok: go_crypto_rule-tlsversion
		return tls.VersionTLS11, nil
	case "1.2":
		return tls.VersionTLS12, nil
	case "1.3":
		return tls.VersionTLS13, nil
	default:
		return 0, fmt.Errorf("unknown tls version: %s", version)
	}
}

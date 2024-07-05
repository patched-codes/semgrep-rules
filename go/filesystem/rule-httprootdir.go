// License: MIT (c) GitLab Inc.

package main

// ruleid: go_filesystem_rule-httprootdir
import (
	"log"
	"net/http"
)

func serveRoot() {
	const path = "/"
	fs := http.FileServer(http.Dir(path))
	log.Fatal(http.ListenAndServe(":9000", fs))
}

func serveSubdir() {
	const path = "/var/www/html/public"
	// ok: go_filesystem_rule-httprootdir
	fs := http.FileServer(http.Dir(path))
	log.Fatal(http.ListenAndServe(":9000", fs))
}

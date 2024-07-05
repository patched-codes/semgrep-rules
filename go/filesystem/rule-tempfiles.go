// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func maintempfiles() {
	// ruleid: go_filesystem_rule-tempfiles
	err := ioutil.WriteFile("/tmp/demo2", []byte("This is some data"), 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}
	// ok: go_filesystem_rule-tempfiles
	err = ioutil.WriteFile("./some/tmp/dir", []byte("stuff"), 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ruleid: go_filesystem_rule-tempfiles
	err = os.WriteFile("/tmp/demo2", []byte("This is some data"), 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ruleid: go_filesystem_rule-tempfiles
	_, err = os.OpenFile("/tmp/demo2", os.O_CREATE|os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ruleid: go_filesystem_rule-tempfiles
	_, err = os.OpenFile("/tmp/demo2", os.O_APPEND|os.O_CREATE|os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ok: go_filesystem_rule-tempfiles
	_, err = os.OpenFile("/tmp/demo2", os.O_RDONLY, 0644)
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ruleid: go_filesystem_rule-tempfiles
	_, err = os.Create("/tmp/demo2")
	if err != nil {
		fmt.Println("Error while writing!")
	}

	// ok: go_filesystem_rule-tempfiles
	_, err = os.CreateTemp("/tmp", "demo2")
	if err != nil {
		fmt.Println("Error while writing!")
	}
}

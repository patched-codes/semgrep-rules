// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

// Input from the std in is considered insecure
package main

import (
	"bufio"
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"html/template"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"net/http/httputil"
	"net/smtp"
	"net/url"
	"os"
	"time"

	"github.com/go-ldap/ldap"
	"github.com/hashicorp/go-retryablehttp"
	"github.com/jlaffaye/ftp"
)

const defaultURL = "http://localhost:8080/ping"

func getParam(r *http.Request) string {
	param := r.URL.Query().Get("param")
	if param == "" {
		param = defaultURL
	}
	return param
}

func vulnerable0001(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.Get(getParam(r))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0002(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.Head(getParam(r))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0003(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.Post(getParam(r), "image/jpeg", nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprint(w, string(data))
}

func vulnerable0004(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.PostForm(getParam(r), nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0005(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.Get(getParam(r))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))

}

func vulnerable0006(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.Head(getParam(r))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))

}

func vulnerable0007(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	request, err := http.NewRequest("POST", getParam(r), nil)
	response, err := http.DefaultClient.Do(request)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0008(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	request, err := http.NewRequestWithContext(context.TODO(), "POST", getParam(r), nil)
	response, err := http.DefaultClient.Do(request)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0009(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.Post(getParam(r), "image/jpeg", nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0010(w http.ResponseWriter, r *http.Request) {
	os.Setenv("TAINTED_URL", "http://example.com")
	url := os.Getenv("TAINTED_URL")
	// ruleid:go_injection_rule-ssrf
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	fmt.Fprintf(w, string(body))
}

var UnsafeUrl = defaultURL

func vulnerable0011_helper() string {
	UnsafeUrl := UnsafeUrl
	response, err := http.Get(UnsafeUrl)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	return string(data)
}

func vulnerable0011(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, vulnerable0011_helper())
}

func vulnerable0012(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.Get(r.PostFormValue("param"))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}
func vulnerable0013() {
	in := bufio.NewReader(os.Stdin)
	url, err := in.ReadString('\n')
	if err != nil {
		panic(err)
	}
	// ruleid:go_injection_rule-ssrf
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s", body)
}

func vulnerable0014_helper() string {
	url := os.Getenv("TAINTED_URL")
	// ruleid:go_injection_rule-ssrf
	response, err := http.Get(url)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	return string(data)
}

func vulnerable0014(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, vulnerable0014_helper())
}

func vulnerable0015_helper() string {
	// ruleid:go_injection_rule-ssrf
	response, err := http.Get(os.Getenv("TAINTED_URL"))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	return string(data)
}

func vulnerable0015(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, vulnerable0015_helper())
}

func vulnerable0016(w http.ResponseWriter, r *http.Request) {
	url := getParam(r)
	if url == "" {
		url = "ftp.localhost:21"
	}
	// ruleid:go_injection_rule-ssrf
	connection, err := ftp.Dial(url)
	err = connection.NoOp()
	var data string
	if err != nil {
		log.Fatal(err)
	} else {
		data = "success"
	}
	fmt.Fprintf(w, data)
}

func vulnerable0017(w http.ResponseWriter, r *http.Request) {
	url := getParam(r)
	if url == "" {
		url = "ldaps://ldap.localhost:636"
	}
	// ruleid:go_injection_rule-ssrf
	_, err := ldap.DialURL(url)
	var data string
	if err != nil {
		log.Fatal(err)
	} else {
		data = "success"
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0018(w http.ResponseWriter, r *http.Request) {
	url := getParam(r)
	if url == "" {
		url = "mail.ietf.org:25"
	}
	// ruleid:go_injection_rule-ssrf
	client, err := smtp.Dial(url)
	err = client.Noop()
	var data string

	if err != nil {
		log.Fatal(err)
	} else {
		data = "success"
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0019_helper() string {
	// ruleid:go_injection_rule-ssrf
	response, err := http.Get(os.Getenv("TAINTED_URL"))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	return string(data)
}

func vulnerable0019(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, vulnerable0019_helper())
}

func vulnerable0020(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.Get(r.URL.Query().Get("param"))
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func vulnerable0021(w http.ResponseWriter, r *http.Request) {
	// ruleid:go_injection_rule-ssrf
	response, err := http.DefaultClient.PostForm(r.PostFormValue("param"), url.Values{})
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

type JsonPayload struct {
	URL string `json:"url"`
}

func vulnerable0022(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Fatal(err)
		return
	}

	var payload JsonPayload
	err = json.Unmarshal(body, &payload)
	if err != nil {
		log.Fatal(err)
		return
	}

	// need pro engine in order to use propagators 
	http.Get(payload.URL)
}

func vulnerable0023(w http.ResponseWriter, r *http.Request) {
	var payload JsonPayload
	decoder := json.NewDecoder(r.Body)
	decoder.Decode(&payload)

	// need pro engine in order to use propagators 
	resp, err := http.Get(payload.URL)
	if err != nil {
		log.Fatal(err)
		return
	}
	defer resp.Body.Close()
}

func vulnerable0024(w http.ResponseWriter, r *http.Request) {
	url := os.Getenv("TAINTED_URL")

	client := retryablehttp.NewClient()

	// ruleid:go_injection_rule-ssrf
	req, err := retryablehttp.NewRequest("GET", url, nil)
	if err != nil {
		log.Fatal(err)
		return
	}

	client.Do(req)
}

func vulnerable0025(w http.ResponseWriter, r *http.Request) {
	url := os.Getenv("TAINTED_URL")

	client := retryablehttp.NewClient()
	// ruleid:go_injection_rule-ssrf
	client.Get(url)
}

var safeUrl01 string = "http://localhost:8080/ping"

func safe0001(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.Get(safeUrl01)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}
	fmt.Fprintf(w, string(body))
}

func safe0002() string {
	in := bufio.NewReader(os.Stdin)
	url, err := in.ReadString('\n')
	if err != nil {
		panic(err)
	}
	// ruleid:go_injection_rule-ssrf
	response, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}
	return string(body)
}

func safe0003(w http.ResponseWriter, r *http.Request) {
	url1 := "test"
	var url2 string = "http://127.0.0.1:8080/ping"
	url2 = url1
	// ok:go_injection_rule-ssrf
	response, err := http.Get(url2)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0004(w http.ResponseWriter, r *http.Request) {
	url := safeUrl01
	// ok:go_injection_rule-ssrf
	response, err := http.Get(url)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

const safeUrl02 = "http://localhost:8080/ping"

func safe0005(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.DefaultClient.Get(safeUrl02)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0006(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.DefaultClient.Head(safeUrl02)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0007(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.DefaultClient.Post(safeUrl02, "image/jpeg", nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0008(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.DefaultClient.PostForm(safeUrl02, nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0009(w http.ResponseWriter, r *http.Request) {
	var q = []byte(`your query`)
	// ok:go_injection_rule-ssrf
	req, _ := http.NewRequest("POST", safeUrl02, bytes.NewBuffer(q))
	req.Header.Set("X-Custom-Header", "myvalue")
	req.Header.Set("Content-Type", "text/plain")

	client := &http.Client{}
	response, err := client.Do(req)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0010(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.Get(safeUrl02)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))

}

func safe0011(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	request, err := http.NewRequest("POST", "http://localhost:8080/ping", nil)
	response, err := http.DefaultClient.Do(request)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0012(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	request, err := http.NewRequestWithContext(context.TODO(), "POST", "http://localhost:8080/ping", nil)
	response, err := http.DefaultClient.Do(request)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))

}

func safe0013(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.Post("http://localhost:8080/ping", "image/jpeg", nil)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0014(w http.ResponseWriter, r *http.Request) {
	// ok:go_injection_rule-ssrf
	response, err := http.Get(safeUrl02)

	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

func safe0015(w http.ResponseWriter, r *http.Request) {
	var url string = "http://127.0.0.1:8080/ping"
	// ok:go_injection_rule-ssrf
	response, err := http.Get(url)
	var data []byte
	if err != nil {
		log.Fatal(err)
	} else {
		data, _ = httputil.DumpResponse(response, true)
	}
	fmt.Fprintf(w, string(data))
}

type IndexParams struct {
	Title string
	Time  string
}

func ping(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "pong")
}

func index(w http.ResponseWriter, r *http.Request) {

	templates := template.Must(
		template.ParseFiles("templates/index.html"),
	)

	indexParams := IndexParams{
		"GitLab Vulnerable MRE",
		time.Now().Format(time.Stamp),
	}
	if title := r.FormValue("title"); title != "" {
		indexParams.Title = title
	}
	if err := templates.ExecuteTemplate(w, "index.html", indexParams); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func main() {

	http.Handle(
		"/assets/",
		http.StripPrefix(
			"/assets/",
			http.FileServer(http.Dir("assets")),
		),
	)

	http.HandleFunc("/", index)
	http.HandleFunc("/ping", ping)

	os.Setenv("TAINTED_URL", "http://example.com")

	http.HandleFunc("/vulnerable0001", vulnerable0001)
	http.HandleFunc("/vulnerable0002", vulnerable0002)
	http.HandleFunc("/vulnerable0003", vulnerable0003)
	http.HandleFunc("/vulnerable0004", vulnerable0004)
	http.HandleFunc("/vulnerable0005", vulnerable0005)
	http.HandleFunc("/vulnerable0006", vulnerable0006)
	http.HandleFunc("/vulnerable0007", vulnerable0007)
	http.HandleFunc("/vulnerable0008", vulnerable0008)
	http.HandleFunc("/vulnerable0009", vulnerable0009)
	http.HandleFunc("/vulnerable0010", vulnerable0010)
	http.HandleFunc("/vulnerable0011", vulnerable0011)
	http.HandleFunc("/vulnerable0012", vulnerable0012)

	http.HandleFunc("/vulnerable0014", vulnerable0014)
	http.HandleFunc("/vulnerable0015", vulnerable0015)
	http.HandleFunc("/vulnerable0016", vulnerable0016)
	http.HandleFunc("/vulnerable0017", vulnerable0017)
	http.HandleFunc("/vulnerable0018", vulnerable0018)
	http.HandleFunc("/vulnerable0019", vulnerable0019)
	http.HandleFunc("/vulnerable0020", vulnerable0020)
	http.HandleFunc("/vulnerable0021", vulnerable0021)
	http.HandleFunc("/vulnerable0022", vulnerable0022)
	http.HandleFunc("/vulnerable0023", vulnerable0023)
	http.HandleFunc("/vulnerable0024", vulnerable0024)

	http.HandleFunc("/safe0001", safe0001)

	http.HandleFunc("/safe0003", safe0003)
	http.HandleFunc("/safe0004", safe0004)
	http.HandleFunc("/safe0005", safe0005)
	http.HandleFunc("/safe0006", safe0006)
	http.HandleFunc("/safe0007", safe0007)
	http.HandleFunc("/safe0008", safe0008)
	http.HandleFunc("/safe0009", safe0009)
	http.HandleFunc("/safe0010", safe0010)
	http.HandleFunc("/safe0011", safe0011)
	http.HandleFunc("/safe0012", safe0012)
	http.HandleFunc("/safe0013", safe0013)
	http.HandleFunc("/safe0014", safe0014)
	http.HandleFunc("/safe0015", safe0015)

	fmt.Println(
		http.ListenAndServe(":8080", nil),
	)
}

package main

import (
	"os"
	"io"
	"log"
	"net/http"
	"io/ioutil"
)

func main() {
	http.Handle("/", http.FileServer(http.Dir(".")))

	http.HandleFunc("/log/all", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != "GET" {
			http.Error(w, "invalid method", 405)
			return
		}
		
		files, err := ioutil.ReadDir("log")
		if err != nil {
			log.Print(err.Error())
			http.Error(w, err.Error(), 500)
			return
		}

		for _, file := range files {
			if file.IsDir() { continue }

			f, err := os.Open("log/" + file.Name())
			if err != nil {
				log.Print(err.Error())
				http.Error(w, err.Error(), 500)
				return
			}

			_, err = io.Copy(w, f)
			f.Close()

			if err != nil {
				log.Print(err.Error())
				http.Error(w, err.Error(), 500)
				return
			}
		}
	})

	log.Printf("Hle!\n")

	log.Fatal(http.ListenAndServe(":80", nil))
}


// main.go (Go Service)
package main

import (
	"encoding/json"
	"net/http"
)

type TowResponse struct {
	Message string `json:"message"`
	Vehicle string `json:"vehicle"`
}

func assistHandler(w http.ResponseWriter, r *http.Request) {
	vehicle := r.URL.Query().Get("vehicle")
	if vehicle == "" {
		http.Error(w, "Vehicle number is required", http.StatusBadRequest)
		return
	}

	// Prepare response
	response := TowResponse{
		Message: "Tow truck dispatched",
		Vehicle: vehicle,
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/assist", assistHandler)
	http.ListenAndServe(":8080", nil)
}


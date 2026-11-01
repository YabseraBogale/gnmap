package main

import (
	"log"
	"net/rpc"
)

func main(){
	client,err:=rpc.DialHTTP("tcp","0.0.0.0:55553")
	if err!=nil{
		log.Fatalln(err)
	}
	client.Close()
}

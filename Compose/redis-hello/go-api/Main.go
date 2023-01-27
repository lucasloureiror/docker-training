package main

import (
	"context"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/redis/go-redis/v9"
)

func main(){
	server := gin.Default()
	var ctx = context.Background()

	rdb := redis.NewClient(&redis.Options{
        Addr:     "172.26.80.1:6379",
        Password: "", // no password set
        DB:       0,  // use default DB
    })

	err := rdb.Set(ctx, "key", "value", 0).Err()
    if err != nil {
        panic(err)
    }
	server.GET("/edit/:value", func(c *gin.Context) {
		valor, _ := strconv.Atoi(c.Param("value"))
		rdb.Set(ctx, "counter", valor, 0)

		c.String(http.StatusOK, "Valor do contador alterado para %d", valor)
		
	  })
	server.Run(":8080")
}
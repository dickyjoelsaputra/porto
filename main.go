package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()

	e.GET("/", func(c echo.Context) error {
		return c.HTML(http.StatusOK, `
            <!DOCTYPE html>
            <html>
            <head><title>Hello Echo</title></head>
            <body>
                <h1>Hello from Echo + Docker!</h1>
				<p>ngentod</p>
            </body>
            </html>
        `)
	})

	e.Logger.Fatal(e.Start(":8080"))
}

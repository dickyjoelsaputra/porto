package main

import (
	"log"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cache"
	"github.com/gofiber/fiber/v2/middleware/compress"
	"github.com/gofiber/fiber/v2/middleware/etag"
	"github.com/gofiber/fiber/v2/middleware/recover"
	"github.com/gofiber/template/html/v2"
)

func main() {
	// Load templates with custom template engine
	engine := html.New("./", ".html") // Path, extension

	// You can define a custom function map if needed
	engine.AddFunc("reverse", func(routeName string) string {
		// You would need to implement your own reverse routing
		// Fiber doesn't support named routes by default
		return "/" + routeName
	})

	app := fiber.New(fiber.Config{
		Views: engine,
		// Prefork: true,
	})

	app.Use(recover.New())
	app.Use(compress.New(compress.Config{
		Level: compress.LevelBestCompression,
	}))
	app.Use(etag.New())
	app.Use(cache.New(cache.Config{
		Expiration: 60 * time.Second,
	}))

	// Static files
	app.Static("/static", "./static")
	// app.Static("/css", "./css")
	// app.Static("/images", "./images")

	// Routes
	app.Get("/", cache.New(), func(c *fiber.Ctx) error {
		return c.Render("index", fiber.Map{
			"name": "Dolly!",
		})
	})

	// Start server
	log.Fatal(app.Listen(":8080"))
}

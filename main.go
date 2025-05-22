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

type PortfolioItem struct {
	Image       string
	Image2x     string
	Title       string
	Category    string
	ProjectLink string
	ModalID     string
	Description string
	Tags        []string
}

var portfolioItems = []PortfolioItem{
	{
		Image:       "static/images/portfolio/fuji.jpg",
		Image2x:     "static/images/portfolio/fuji@2x.jpg",
		Title:       "AG Force",
		Category:    "Backend & Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-01",
		Description: "api mobile, api dashboard & monolith dashboard internal",
		Tags:        []string{"Branding", "Product Design"},
	},
	{
		Image:       "static/images/portfolio/lamp.jpg",
		Image2x:     "static/images/portfolio/lamp@2x.jpg",
		Title:       "AG Force - Warung Berkah",
		Category:    "Backend & Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-02",
		Description: "api mobile & api dashboard",
		Tags:        []string{"Branding"},
	},
	{
		Image:       "static/images/portfolio/lamp.jpg",
		Image2x:     "static/images/portfolio/lamp@2x.jpg",
		Title:       "AG Force - Kemala Run",
		Category:    "Backend",
		ProjectLink: "#",
		ModalID:     "modal-03",
		Description: "api mobile & api dashboard",
		Tags:        []string{"Product Design"},
	},
	{
		Image:       "static/images/portfolio/rucksack.jpg",
		Image2x:     "static/images/portfolio/rucksack@2x.jpg",
		Title:       "claverio.com",
		Category:    "Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-04",
		Description: "monolith",
		Tags:        []string{"Website"},
	},
	{
		Image:       "static/images/portfolio/skaterboy.jpg",
		Image2x:     "static/images/portfolio/skaterboy@2x.jpg",
		Title:       "Eten",
		Category:    "Backend",
		ProjectLink: "#",
		ModalID:     "modal-05",
		Description: "api dashboard",
		Tags:        []string{"Illustration"},
	},
	{
		Image:       "static/images/portfolio/sanddunes.jpg",
		Image2x:     "static/images/portfolio/sanddunes@2x.jpg",
		Title:       "scbd.com",
		Category:    "Maintainer Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-06",
		Description: "monolith",
		Tags:        []string{"Branding", "Product Design"},
	},
	{
		Image:       "static/images/portfolio/minimalismo.jpg",
		Image2x:     "static/images/portfolio/minimalismo@2x.jpg",
		Title:       "SCBD Apps",
		Category:    "Backend & Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-07",
		Description: "api mobile & monolith dashboard",
		Tags:        []string{"Branding", "Product Design"},
	},
	{
		Image:       "static/images/portfolio/minimalismo.jpg",
		Image2x:     "static/images/portfolio/minimalismo@2x.jpg",
		Title:       "propertycuan.id",
		Category:    "Fullstack",
		ProjectLink: "#",
		ModalID:     "modal-08",
		Description: "monolith",
		Tags:        []string{"Branding", "Product Design"},
	},
}

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

	app.Use(func(c *fiber.Ctx) error {
		c.Set("X-Powered-By", "Go")
		return c.Next()
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
			"name":           "Dolly!",
			"portfolioItems": portfolioItems,
		})
	})

	// Start server
	log.Fatal(app.Listen(":8080"))
}

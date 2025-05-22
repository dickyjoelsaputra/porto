package main

import (
	"html/template"
	"io"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()
	e.Debug = false

	// Serve static files from js and css directories
	e.Static("/static", "static")
	// e.Static("/css", "css")
	// e.Static("/images", "images")

	renderer := &TemplateRenderer{
		templates: template.Must(template.ParseGlob("*.html")),
	}

	e.Renderer = renderer

	e.GET("", func(c echo.Context) error {
		return c.Render(http.StatusOK, "index.html", map[string]interface{}{
			"name": "Dolly!",
		})
	}).Name = "index"

	e.Use(middleware.Recover())
	e.Logger.Fatal(e.Start(":8080"))
}

// TemplateRenderer is a custom html/template renderer for Echo framework
type TemplateRenderer struct {
	templates *template.Template
}

// Render renders a template document
func (t *TemplateRenderer) Render(w io.Writer, name string, data interface{}, c echo.Context) error {

	// Add global methods if data is a map
	if viewContext, isMap := data.(map[string]interface{}); isMap {
		viewContext["reverse"] = c.Echo().Reverse
	}

	return t.templates.ExecuteTemplate(w, name, data)
}

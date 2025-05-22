# Stage 1: Build binary menggunakan Go terbaru
FROM golang:1.24-alpine AS builder

# Install git (kadang dibutuhkan untuk go mod)
RUN apk add --no-cache git

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

# Build dengan output statis
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# Stage 2: Minimal runtime image
FROM alpine:latest

WORKDIR /app

# Copy hasil build dari builder
COPY --from=builder /app/main .

# Copy static files
COPY index.html .
COPY css/ ./css/
COPY js/ ./js/
COPY images/ ./images/

# Port default (informasi)
EXPOSE 8080

# Jalankan binary
CMD ["./main"]

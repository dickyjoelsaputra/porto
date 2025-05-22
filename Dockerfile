# Gunakan base image
FROM golang:1.24

# Set workdir
WORKDIR /app

# Copy go.mod dan download dependency
COPY go.mod ./
RUN go mod download

# Copy semua file
COPY . .

# Build aplikasi
RUN go build -o main .

# Jalankan aplikasi
CMD ["./main"]

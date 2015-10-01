server {
    listen 80 default;
    server_name johndietrick.com www.johndietrick.com;

    location / { try_files $uri @johndietrick; }
    location @johndietrick {
        proxy_pass http://127.0.0.1:9000;
    }
}

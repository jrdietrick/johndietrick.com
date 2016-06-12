server {
    listen 80;
    server_name johndietrick.com www.johndietrick.com;

    location / {
        return 301 https://johndietrick.com$request_uri;
    }
}

server {
    listen 80;
    server_name 204.44.86.53;

    location /static/ {
        alias /var/www-static/;
        autoindex off;
    }
}

server {
    listen 80 default_server;
    server_name _;
    server_name_in_redirect off;
    return 444;
}

server {
    listen 443 ssl default_server;
    server_name johndietrick.com www.johndietrick.com;

    ssl_certificate /etc/nginx/certs/johndietrick.com.crt;
    ssl_certificate_key /etc/nginx/certs/johndietrick.com.key;

    location / { try_files $uri @johndietrick; }
    location @johndietrick {
        proxy_pass http://127.0.0.1:9000;
    }

    location ~ /cv/?$ {
        return 301 https://johndietrick.com/static/cv.pdf;
    }
}

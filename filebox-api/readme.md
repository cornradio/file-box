
## onserver
```
pip install flask
pip install flask-cors

cd /root/file-box/filebox-api/; flask run -p3000 --host=0.0.0.0
```

## server nginx



```
vim /etc/nginx/nginx.conf

```
add a mutiple server config like this:

nginx will proxy 3000 > 3008 

```
	server
	{
		listen 3008 ssl;
		server_name b.kill9pid.top;
    ssl_certificate xxx
    ssl_certificate_key xxx

		ssl_protocols TLSv1.2; # 支持的 SSL 协议版本
		ssl_prefer_server_ciphers on; # 使用服务器端密码优先
		ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH"; # 使用的密码套件
	location / {
		proxy_pass http://127.0.0.1:3000/;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-Forwarded-Host $host;
		proxy_set_header X-Forwarded-Prefix /;
	}

}

```

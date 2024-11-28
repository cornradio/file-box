python3 -m http.server 80 > /dev/null 2>&1 &
cd filebox-api;flask run -p3000 --debug > /dev/null 2>&1 &

echo '
front end server started on 80
back end server started on 3000

you may edit port.js 

> incase u need kill them
kill -9 $(lsof -t -i :3000)
kill -9 $(lsof -t -i :80)
'

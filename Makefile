build:
	tsc app.ts
	docker-compose build
start:
	cd ./monitor && tsc --lib 'es6' ./app.ts
	docker-compose up -d
log-socket:
	docker-compose logs socketio
stop:
	docker-compose stop
	docker-compose rm -f

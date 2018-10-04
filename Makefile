build:
	tsc app.ts
	docker-compose build
start:
	cd ./monitor && tsc --lib 'es6' ./app.ts
	docker-compose up -d
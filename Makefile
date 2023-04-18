run:
	docker-compose up -d
	uvicorn main:app --reload
install:
	pip3 install -r requirements.txt

docker-build:
	docker build \
	-f builds/docker/Dockerfile \
	-t  portafolio:local .


docker-run:
	docker run --rm -it -p 8000:8000 \
	--env-file ./.env \
	portafolio:local
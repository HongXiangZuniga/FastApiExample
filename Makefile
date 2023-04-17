run:
	docker-compose up -d
	uvicorn main:app --reload
install:
	pip3 install -r requirements.txt
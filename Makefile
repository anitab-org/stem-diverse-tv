dev: 
	python run.py
docker_host_dev: 
	flask run --host 0.0.0.0
python_tests: 
	python -m unittest discover tests 
docker_test: 
	docker-compose -f docker-compose.test.yml up --build --exit-code-from stem_diverse_tv_test --remove-orphans
docker_dev: 
	docker-compose up --build --remove-orphans 


	


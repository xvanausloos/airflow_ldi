generate-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install -r requirements.txt

deploy-infrastructure:
	./deploy.sh
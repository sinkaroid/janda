install:
	pip install -r requirements.txt

janda: 
	python -m unittest test.test_build

nhentai-get: # testing nhentai
	python -m unittest test.test_nhentai

pururin-get: # testing pururin
	python -m unittest test.test_pururin

hentaifox-get: # testing hentaifox
	python -m unittest test.test_hentaifox

hentai2read-get: # testing hentai2read
	python -m unittest test.test_hentai2read

simplyh-get: # testing simplyh
	python -m unittest test.test_simplyh

api-mock: # check api if something down
	python -m unittest test.test_api

build-docs: # build and deploy docs
	pdoc --html janda

upload:
	bash build.sh
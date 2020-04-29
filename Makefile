.PHONY: default build clean publish

default: build

build:
	npm install
	hugo

clean:
	rm -rf public/*

publish: clean build
	cd public && git add . \
		&& git commit -m "make publish" \
		&& git push origin gh-pages

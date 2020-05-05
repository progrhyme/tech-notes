.PHONY: default setup build build-production clean publish

default: build

setup:
	npm install

build: setup
	hugo

build-production: setup
	env HUGO_ENV=production hugo --minify

clean:
	rm -rf public/*

publish: clean build-production
	cd public && git add . \
		&& git commit -m "make publish" \
		&& git push origin gh-pages

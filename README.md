![github pages](https://github.com/progrhyme/tech-notes/workflows/github%20pages/badge.svg)

# progrhyme's Tech Notes

My personal yet public technical notes.

Forked from https://github.com/google/docsy-example .

# Set up
## Install Hugo
You need recent **extended** version of [Hugo](https://gohugo.io) to do local builds and previews of sites (like this one) that use Docsy.  
See [Hugo installation guide](https://gohugo.io/getting-started/installing/) to know how to get extended version.

## Clone This Repository

```sh
git clone git@github.com:progrhyme/tech-notes.git
cd tech-notes
git submodule update --init --recursive
```

## Preview Site

```sh
hugo serve
```

Then you can see the site at http://localhost:1313/tech-notes/

## Build Site

You need Node.js to build site.

```sh
npm install
hugo
```

# Manage Contents
## Add notes

```sh
# Add a section page
hugo new a/path/to/section/_index.md
# Add a note under the section
hugo new a/path/to/section/note.md
```

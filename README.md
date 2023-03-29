# HerbeMalveillante.github.io

This is my <a href="https://herbemalveillante.github.io">Personal Website !</a>

## How does this project works ?

All I really wanted when creating this project was the simplest way possible to create a website and a blog, using minimal external technologies, hard-to-master frameworks, and unbloated code.

After trying to create multiple websites with **Flask**, **Hugo**, **Jekyll** and many more, I finally decided to write a little compiler that takes **Mardown files** as input, and produces clean **static HTML files**.

In fact, even the **HTML to Markdown** converter was not written by me, and the whole converting process takes up only **±100 lines of code** (with comments !)

All I had to do was to write the **HTML template** and add some **CSS Magic** and voilà ! Simple blog. To write an article, all I have to do is create a new markdown file with my content, run the compiler, and push to GitHub. As the website is static, everything is managed with **Github Pages** and no additional step is required. Simplicity at its best !

## Installation

If you want to create a blog working similarly as mine, you can **clone the project**, **install the dependencies**, and **replace my HTML / Markdown code with yours** !

Install the python modules

```bash
pip install --upgrade pip rich markdown
```

Install Tailwind

```bash
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss

```

run the tailwind server

```bash
./tailwindcss -i static/input.css -o static/output.css --watch
```

## Markdown file structure

The first four lines are used to describe the article :

1. Title
2. Date
3. Author
4. Tags

After that, any other line is considered content and will be compiled to HTML.

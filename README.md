# HerbeMalveillante.github.io

## Installation

```bash
pip install --upgrade pip rich markdown

curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss
```

## Running tailwind server

```bash
./tailwindcss -i static/input.css -o static/output.css --watch
```

## Project structure

The compiler should do two things :

1. Generate HTML files from every `.md` file contained in the `garden` folder.
2. Add a `head` tag and info at the beginning that contains information about the file (Title / Author / Date)
3. Add the navbar and the footer to the final HTML file
4. Add the final HTML file in the blog folder
5. Update `blog.html` to show all articles, lastest first.

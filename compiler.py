from rich import print
import os
import markdown
import re

class Fruit():

    def __init__(self, filepath):
        """
        Opens the file at the file path and reads the content.
        First line is the title of the article
        Second line is the Date
        Third line is the author
        Fourth line are the tags, separated by commas

        Lines below are the file content.
        """

        print("Loading file: [bold blue]" + filepath + "[/bold blue]")

        self.filepath = filepath

        with open("garden/"+filepath, 'r') as f:
            self.content = f.read()

        self.title = self.content.splitlines()[0]
        self.date = self.content.splitlines()[1]
        self.author = self.content.splitlines()[2]
        self.tags = self.content.splitlines()[3].split(',')

        self.content = "\n".join(self.content.splitlines()[4:])
        self.contentHTML = markdown.markdown(self.content)

    def generateFinalHTML(self):
        """
        Generates the final HTML file.
        The HTML file is a copy of the 'templates/template.html' file,
        with the title of the article inserted in place of the '@title@' string,
        and the content of the article inserted in place of the '@content@' string.

        The final HTML file is saved in the 'blog' folder, with the same name as the original file (self.filepath),
        but with the .html extension.
        """
        with open("templates/template.html", 'r') as f:
            html = f.read()

        html = html.replace("@title@", self.title)
        html = html.replace("@content@", self.contentHTML)

        with open("blog/"+self.filepath.replace(".md", ".html"), 'w') as f:
            f.write(html)

        print("Created file: [bold green]" + self.filepath.replace(".md", ".html") + "[/bold green]")

def getFileNames ():
    """
    Returns a list of all the files in the current directory
    """
    return os.listdir("garden")


def updateBlog():
    """
    Updates the blog.html file by generating a preview of each article.
    The base of the blog.html file is contained in the 'templates/blogTemplate.html' file.
    It contains a '@content@' string, which should be replaced by the previews of each article.

    The preview of an article should be generated using the 'templates/articlePreview.html' file.
    It contains a '@title@' string, which should be replaced by the title of the article,
    a '@date@' string, which should be replaced by the date of the article,
    a '@author@' string, which should be replaced by the author of the article,
    a '@tags@' string, which should be replaced by the tags of the article,
    a '@link@' string, which should be replaced by the link to the article,
    and a '@preview@' string, which should be replaced by the preview of the article (first 200 characters of the article)
    """

    with open("templates/blogTemplate.html", 'r') as f:
        html = f.read()

    content = ""

    for f in getFileNames():
        fruit = Fruit(f)

        with open("templates/articlePreview.html", 'r') as f:
            preview = f.read()

        preview = preview.replace("@title@", fruit.title)
        preview = preview.replace("@date@", fruit.date)
        preview = preview.replace("@author@", fruit.author)
        preview = preview.replace("@tags@", ", ".join(fruit.tags))
        preview = preview.replace("@link@", fruit.filepath.replace(".md", ".html"))
        preview = preview.replace("@preview@", re.sub('<[^<]+?>', '', markdown.markdown(fruit.content)[:200]))

        content += preview

    html = html.replace("@content@", content)

    with open("blog.html", 'w') as f:
        f.write(html)

    print("Created file: [bold green]blog.html[/bold green]")

for f in getFileNames():
    fruit = Fruit(f)
    fruit.generateFinalHTML()
updateBlog()

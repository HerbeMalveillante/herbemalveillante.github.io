from rich import print
import os
import markdown
import datetime
import re
from dateutil import parser
from datetime import datetime


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

    def __str__(self):
        """Returns the title of the article, the date, and the author"""
        return self.title + " - " + self.date + " - " + self.author

    def __repr__(self):
        return self.__str__()

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
        html = html.replace("@date@", self.date)
        html = html.replace("@author@", self.author)
        html = html.replace("@tags@", ", ".join(self.tags))
        html = html.replace("@content@", self.contentHTML)

        with open("blog/"+self.filepath.replace(".md", ".html"), 'w') as f:
            f.write(html)

        print("Written file: [bold green]" + self.filepath.replace(".md", ".html") + "[/bold green]")

def getFileNames ():
    """
    Returns a list of all the files in the current directory
    """
    return os.listdir("garden")

def cleanup():
    """
    At any moment, I might want to delete a file from the 'garden' folder.
    This function searches the 'blog' folder for files that are not in the 'garden' folder, and deletes them.
    """

    files = getFileNames()
    files = [f.replace(".md", ".html") for f in files]

    for f in os.listdir("blog"):
        if f not in files:
            os.remove("blog/"+f)
            print("Deleted file: [bold red]" + f + "[/bold red]")

    print("[bold yellow]Cleanup complete.[/bold yellow]")


def updateBlog():
    """
    Updates the blog.html file by generating a preview of each article.
    The base of the blog.html file is contained in the 'templates/blogTemplate.html' file.

    The preview of an article should be generated using the 'templates/articlePreview.html' file.
    It contains a '@title@' string, which should be replaced by the title of the article,
    a '@date@' string, which should be replaced by the date of the article,
    a '@author@' string, which should be replaced by the author of the article,
    a '@tags@' string, which should be replaced by the tags of the article,
    a '@link@' string, which should be replaced by the link to the article,
    and a '@preview@' string, which should be replaced by the preview of the article (first 500 characters of the article)

    Warning : the articles should be sorted by date, from the most recent to the oldest. If two articles have the same date, sort them alphabetically.
    The date of the article can be found in the 'self.date' variable as a string formatted as 'YYYY-MM-DD'.

    To sort the articles by date, simply add the most recent article first in the 'content' variable.
    """

    fruits = [Fruit(f) for f in getFileNames()]
    dates = [fruit.date for fruit in fruits]
    date_objects = sorted([datetime.strptime(date, '%d/%m/%Y') for date in dates], reverse=True)

    print(dates)
    print(date_objects)
    # dates are in the format "DD/MM/YYYY"
    # we need to sort the dates using the datetime module
    # sortedDates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%y'), reverse=True)


    # then sort the fruits by date
    sortedFruits = []
    for date in date_objects:
        for fruit in fruits:
            if datetime.strptime(fruit.date, '%d/%m/%Y') == date:
                sortedFruits.append(fruit)
                break

    # then generate the previews
    content = ""

    for fruit in sortedFruits:
        fruit.generateFinalHTML()

        with open("templates/articlePreview.html", 'r') as f:
            preview = f.read()

        preview = preview.replace("@title@", fruit.title)
        preview = preview.replace("@date@", fruit.date)
        preview = preview.replace("@author@", fruit.author)
        preview = preview.replace("@tags@", ", ".join(fruit.tags))
        preview = preview.replace("@link@", fruit.filepath.replace(".md", ".html"))
        preview = preview.replace("@preview@", re.sub('<[^<]+?>', '', markdown.markdown(fruit.content))[:200] + "...")

        content += preview

    with open("templates/blogTemplate.html", 'r') as f:
        html = f.read()

    html = html.replace("@content@", content)

    with open("blog.html", 'w') as f:
        f.write(html)

    print("Updated file: [bold green]blog.html[/bold green]")

    cleanup()



# for f in getFileNames():
#     fruit = Fruit(f)
#     fruit.generateFinalHTML()
updateBlog()

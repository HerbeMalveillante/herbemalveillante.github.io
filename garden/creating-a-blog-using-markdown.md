Generating a static blog using Markdown and Tailwind
30/03/2023
Vergazon
meta, project

blah

# What is this project ?

I've been looking for a **quick**, **customizable** and **performant** way to create a website and a **blog** for a long time. I can safely say I tried the majority of the existing solutions, and after always being disappointed by the method or language I was using, I finally decided to write a **little compiler** that takes Markdown files as input, and produces clean static HTML files.

# I tried many solutions.

## Svelte

Svelte ([svelte.dev](https://svelte.dev/)) is a modern framework that allows for the creation of very powerful **single-page applications**. Altough it is extremely fast, and appreciated by the community, I found it to be a bit too "bleeding edge" for my needs : the community is still relatively small, and the online documentation and exemples are not as complete as I would have liked.

However, I still think this framework is one of the best front-end Javascript frameworks out there, and I definitely will take a look at it again in the future.

## Flask

Flask ([https://flask.palletsprojects.com/](https://flask.palletsprojects.com/en/2.2.x/)) is a micro-framework for Python, that allows for the creation of web applications. It is very easy to use, and the documentation is very complete.

I think this is **the best solution I have found so far**, being extremely powerful while still being beginner-friendly. I even bought a hosting plan for future projects (Not this Blog though, as you will see later on).

However, I found it to be a bit **too bloated for my needs** : in my mind, a blog created with Flask would have a database, a markdown editor, an account/comment system, and many more features. I knew if I started working on this project, I would end up **spending months on it**, and I didn't want to spend that much time on a project that would not be used by anyone but me to write silly articles to the internet.

## Vanilla HTML

Finally, the last solution that came to my mind was to simply write the HTML files **by hand**. I was almost ready to do this, when I realized that I would have to write the same HTML code for every article, and for **every page of the website**. I would have to write the same HTML code for the header, the footer, the navigation bar, and many more, by hand.

As I am a programmer, I don't like to do things by hand, and I don't like to repeat myself (and I'm way too lazy to do it anyways...). So I decided not to use this solution either.

# What is the solution I finally chose ?

As I said in the introduction to this article, I decided to take the simplicity of the Vanilla HTML approach, and the power of Flask templating that I really liked. I also wanted to use a language that I was already familiar with, and that I could use to **write the compiler**.

This led me to the creation of this project, which is extremely simple in terms of code, and very easy to use.

Basically, I will write any Markdown article in a specific folder using VSCode, and ask a Python script to **compile it to HTML**, and to embed it in a custom template. The result is a static HTML file that can be hosted on any web server, or GitHub Pages (which I ended up using, as it is free and very easy to use).

I plan on using another hosting service in the future (GitHub Pages caching is not very good, and I don't want to wait hours for my changes to be visible), but for now, it is more than enough for my needs.

The great thing about static HTML files is that I will be able to optimize the **referencement of my website**, allowing me to rank higher on Google, and to be found more easily.

I also am using VSCode to write Markdown, which is extremely convenient as it **formats the text automatically**, and allows me to preview the result in real time.

# How does this work ?

The Python compiler is extremely simple : It searches for all the Markdown files in the `garden` folder in the root of my project, and for each of them, it will :

-   Extract metadata from the first lines (title, author, etc.)
-   Generate a preview of the blog post, and adds it to the [blog page](../blog.html).
-   Generate a static HTML from a custom template, and add it to the `blog` folder.

Everything fits in more or less **150 lines of code**, in a single Python file. I will not go into the details of the code, as it is not the purpose of this article, but you can find the [source code on GitHub](https://github.com/herbemalveillante/herbemalveillante.github.io/).

# What next ?

I plan on adding more features to this project in the future, such as :

-   A better way to manage the metadata of the blog posts
-   Adding a cover image to posts
-   Adding a search bar
-   Adding pagination to the blog page
-   Adding a separate `Projects` page that links to every blog post containing the `project` tag
-   Adding a better way to embed code snippets (I'm using images for now, which is not ideal )
-   Creating videos for every important project, alongside the blog posts.
-   Adding LaTeX or MathJax support to embed mathematical formulas in the blog posts.

This project is **open-source** : feel free to clone the project and adapt it to your needs, or to **contribute** to it !

# Follow me for more !

You can find me on [Twitter](https://twitter.com/P4CO3), [GitHub](https://github.com/herbemalveillante), [YouTube](https://www.youtube.com/channel/UC0qAWS1GcM8_cRLoPtLgNHA), and [Discord](https://discord.gg/6Qu3FdvHYz).

I'll be posting **many more articles** and projects about programming, game development, reinforcement learning and my learning process in general. I hope you'll enjoy them !

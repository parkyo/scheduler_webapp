# Helloworld Web App
> django2.1

I have created Helloworld web app that includes todo list to practice basic web app development

## Django
> <strong>Django</strong> is a server-side Python web framework. 
<img src = "django.png" width = 70%/>

### Set-Up Django for MacOS
Django Development Environment includes Python scripts and a simple development webserver that you can test local Djnago web applications on web browser. (<a href="https://www.youtube.com/watch?v=UyQn0BhVqNU&list=PLBZBJbE_rGRXBhJNdKbN7IUy-ctlOFxA1&index=1">reference</a>)
#### 1. Install Python
<strong>Homebrew</strong> is an open-source software package manager that helps install different applications on MacOS
<pre><code>$brew install python3</code></pre>
#### 2. Install Pipenv
<strong>Pipenv</strong> is a tool that automatically creates and manages a virtual environment for Python. We need a virtual environment to keep dependencies required by different projects separate by creating isolated python virtual environments for them. Pipenv prevents having to use <code>pip</code> and <code>virtualenv</code> separately. (<a href = "https://www.geeksforgeeks.org/python-virtual-environment/"> GeeksForGeeks </a>)
<pre><code>$pip3 install pipenv</code></pre>
> <strong>pip3</strong> is automatically installed by Homebrew. Pip3 is another package manager that includes <code>pipenv</code>
#### 3. Move to a directory and create a folder for the new project
<pre><code>$mkdir helloworld_webapp
$cd helloworld_webapp
</code></pre>
#### 4. Install django with pipenv
Pipenv creates a virtual environment <i>django</i> of 2.1 version speicifically for this project.
<pre><code>$pipenv instal django==2.1</code></pre>
#### 5. Activate the virtual environment
<pre><code>$pipenv shell</code></pre>
This allows you to use the specific version of django that you installed for your project.
#### 6. Create a new project 
<pre><code>$django-admin startproject helloworld_project .</pre></code>
This starts a new project, helloworld_project in the current directory.
<p>
  Now you can run django server <code>$python manage.py runserver</code> and open the local host to view your project on web browser!
</p>

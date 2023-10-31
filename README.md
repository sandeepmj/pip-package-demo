# Creating your own ```pip install``` package

Before you proceed, please sure your Macs have a recent version of xCode's CLT. You do not need the entire xCode application – just the CLT. Here are the ![instructions to install](https://www.freecodecamp.org/news/install-xcode-command-line-tools/).

## 1. Create a ```GitHub repo```

- Give it a succinct and meaningful name (no more than 2 words).
- Make it public.
- Initialize with a ```README.md``` file.
- Create a ```.gitignore``` file.
- Select an ```MIT license```.

![Repo image](/images/01-create-repo.png)

## 2. Clone repo to your computer
- Stay organized!
- Hit reload to reveal your origin repo:
![Clone 1 image](/images/02A-clone.png)

- Hit clone:
![Clone 2 image](/images/02B-clone.png)

## 3. Create a directory and ```setup.py``` file
- Your clone will look like this:
![files and folder](/images/03A-organization.png)

- Create a folder/directory and give it a one-word name generally referring to the purpose of the functions within.
- Also create an empty ```setup.py```
- Reveal the hidden files and folders by clicking on CMND-SHIFT-.
![Reveal hiddens files and folder](/images/03B-organization.png)

## 4. Prepare ```setup.py``` file
#### Copy, paste and update the following code into your ```setup.py``` file:

```
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pip-package-demo', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.2',
    author='Sandeep Junnarkar', ## your name
    author_email='sjnews@gmail.com', ## your email
    description='Demo on pip package creation', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandeepmj/pip-package-demo/tree/main',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/sandeepmj/pip-package-demo/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['demo'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)
```

In color:
![Clone 4 setup](/images/04-setup.png)

## 5. Inside the folder you created in step 3:

- Create a file which will hold your function. Name it something short that alludes to the purpose of the functions it holds, like```mathFuncs.py```

- Write some functions in that file:

![Functions image](/images/05A-fucntions.png)

## 6. Inside the same folder:

- Create a file called ```__init__.py``` (**exactly that name!**) 
- In that file, we'll called the functions you wrote in your functions file.

```
## .demoFunc refers to file that holds all the functions
from .demoFunc import addNumbers, subNumbers
```

In color:
![Init image](/images/06A-init.png)

## 7. Add ```.DS_Store``` to your ```.gitignore``` file.

## 8. Commit and Push your Remote to Origin

## 9. In a ```Jupyter notebook``` run the following:

```pip install git+https://github.com/full-address-to-repo.git```

Note the **git+** and the **.git**

## 10. Finally, import your functions:
![import functions image](/images/10A-import.png)

When you invariably have to fix or update your functions (or add a new function), you will need to increment the version number in the ```setup.py``` file. **If you don't...it won't work!**
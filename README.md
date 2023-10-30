# Creating your own ```pip install``` package

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

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyVT4002',
     version='0.1.2',
     author="Embida AS",
     author_email="post@embida.no",
     description="A driver for vt4002 Vötsch climate chamber",
     long_description=long_description,
     long_description_content_type="text/markdown",
     project_urls = {
     'Source': 'https://github.com/Embida/pyVT4002'
     },
     packages=setuptools.find_packages(),
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
     ],
 )

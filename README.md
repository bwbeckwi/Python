# Python Resources

A collection of code examples and presentations on Python.

## Installation

#### For Github Enterprise Users

```bash
cd <some-directory>
git clone git@github.intel.com:tmsquill/python-resources.git
```

#### For Everyone Else

```bash
cd <some-directory>
curl -OL https://github.intel.com/tmsquill/python-resources/archive/master.zip && unzip master.zip && rm master.zip
```

#### Installing Conda

You need to have ```conda``` installed to run the examples. The installer can be found [here](https://conda.io/miniconda.html).

## Creating an Environment

You will need use conda to create an environment for installing the various packages used throughout the examples.

```bash
conda create --name python_presentation python=3.6.2
```

Now let's activate the environment.

```bash
source activate python-presentation
```

## Installing Packages to the Environment

Now we can install the various packages to the environment. We will install using both ```conda``` and ```pip``` (a custom ```pip``` was added to this environment when we created it). Any installation that occurs at this point will only apply inside the conda environment ```python_presentation``` since its the active environment.

The only package that we need to install through ```conda``` is ```numba```, let's install it now.

```bash
conda install numba
```

All other packages can be installed directly with ```pip```. By convention, they are specified in ```requirements.txt``` and can be installed in a single line.

```bash
pip install -r requirements.txt
```

At this point, all packages needed for the examples should be installed in the environment.

## Running the Examples

Enter the ```code/<some-example>``` directory, then consult README for the example.

```bash
cd code/<some-example>```
```

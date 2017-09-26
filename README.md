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

## Running the Examples

You will need use conda to create an environment for installing the various packages used throughout the examples.

```bash
conda create --name python-presentation python=3.6.2
```

Now let's activate the environment.

```bash
source activate python-presentation
```

Now we can install the various packages to the environment. We will install using both ```conda``` and ```pip``` (a custom ```pip``` was added to this environment when we created it). Any installation that occur at this point will only apply inside the conda environment ```python-presentation``` because it is the active environment.


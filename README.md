# Math 449 Numerical Applied Mathematics at WUSTL

## Tentative material
[https://scaomath.github.io/teaching/fall2020-math449](https://scaomath.github.io/teaching/fall2020-math449)

## Primer on Python 3
[https://www.kaggle.com/learn/python](https://www.kaggle.com/learn/python)

## Structure of this repo
```bash
├── Homework
│   ├── imports needed
│  
├── Lectures file
├── Office hour files
│   ├── codes during live stream

```

## How to keep your local copy up-to-date
First use either terminal on Mac or Windows powershell to navigate to the folder of your current copy of this repo
then do the following
```bash
git remote add upstream git://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git
git fetch upstream
```
The git will tell your there is new upstream. Now do 
```bash
git pull --rebase upstream master
```
This will keep the version history even for your edited local copies.

# punch
> Description: Keep track of the hours you spend working on a project.
> *This is a work in progress.*

&nbsp;

## Installation

```bash
# Clone the repository
git clone git@github.com:ginsm/punch.git

# Ensure the main file is an executable
chmod +x ./punch/src/punch.py

# Create ~/bin directory
mkdir ~/bin

# Create a symbolic link to the main file
ln -s $PWD/punch/src/punch.py ~/bin/punch
```
Add the following to the end of your `.profile`, `.bashrc`, etc:

`export PATH="~/bin:$PATH"`

Restart your terminal or source the file with the above line.

&nbsp;

## Commands
> Usage: punch `<command>` `<argument>`

| Command | Description | Argument Type |
| :--- | :--- | :--- |
| punch | Toggle between being punched in or out | None |
| punch track `[argument]` | Begin tracking a new project | None or String
| punch info `[argument]` | Output current or specified project's information | None or String |
| punch rm `<argument>` | Stop tracking a specific job | String |
| punch list | Output the jobs you are currently tracking | None |
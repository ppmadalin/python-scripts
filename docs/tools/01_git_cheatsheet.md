
**CONFIGURE TOLLING**
```
# Sets the name you want atached to your commit transactions
$ git config --global user.name "[name]"

# Sets the email you want atached to your commit transactions
$ git config --global user.email "[email address]"

# Enables helpful colorization of command line output
$ git config --global color.ui auto
```
**CREATE REPOSITORIES**
```
# Creates a new local repository with the specified name
$ git init [project-name]

# Downloads a project and its entire version history
$ git clone [url]
```

**MAKE CHANGES**

```
# Lists all new or modified files to be commited
$ git status

# Snapshots the file in preparation for versioning
$ git add [file]

# Unstages the file, but preserve its contents
$ git reset [file]

# Shows file differences not yet staged
$ git diff

# Shows file differences between staging and the last file version
$ git diff --staged

# Records file snapshots permanently in version history
$ git commit -m "[descriptive message]"
```

**GROUP CHANGES***

```
# Lists all local branches in the current repository
$ git branch

# Creates a new branch
$ git branch [branch-name]

# Switches to the specified branch and updates the working directory
$ git checkout [branch-name]

# Combines the specified branch’s history into the current branch
$ git merge [branch]

# Deletes the specified branch
$ git branch -d [branch-name]
```

**REFACTOR FILENAMES**

```
$ git rm [file]
Deletes the file from the working directory and stages the deletion
$ git rm --cached [file]
Removes the file from version control but preserves the file locally
$ git mv [file-original] [file-renamed]
Changes the file name and prepares it for commit
```

**SUPPRESS TRACKING**

```
t
*.log
build/
temp-*
A text file named .gitignore suppresses accidental versioning of
files and paths matching the specified paterns
$ git ls-files --other --ignored --exclude-standard
Lists all ignored files in this project

```

**SAVE FRAGMENTS**

```
$ git stash
Temporarily stores all modified tracked files
$ git stash list
Lists all stashed changesets
$ git stash pop
Restores the most recently stashed files
$ git stash drop
Discards the most recently stashed changeset
```

**SYNCHRONIZE CHANGES**

```
$ git fetch [bookmark]
Downloads all history from the repository bookmark
$ git merge [bookmark]/[branch]
Combines bookmark’s branch into current local branch
$ git push [alias] [branch]
Uploads all local branch commits to GitHub
$ git pull
Downloads bookmark history and incorporates changes
```

**REDO COMMITS**

```
$ git reset [commit]
Undoes all commits afer [commit], preserving changes locally
$ git reset --hard [commit]
Discards all history and changes back to the specified commit
```

**REVIEW HISTORY**

```
$ git log
Lists version history for the current branch
$ git log --follow [file]
Lists version history for a file, including renames
$ git diff [first-branch]...[second-branch]
Shows content differences between two branches
$ git show [commit]
Outputs metadata and content changes of the specified commit
```


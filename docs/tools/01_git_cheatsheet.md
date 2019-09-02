
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
# Deletes the file from the working directory and stages the deletion
$ git rm [file]

# Removes the file from version control but preserves the file locally
$ git rm --cached [file]

# Changes the file name and prepares it for commit
$ git mv [file-original] [file-renamed]
```

**SUPPRESS TRACKING**

```
# A text file named .gitignore suppresses accidental versioning of
# files and paths matching the specified paterns
t
*.log
build/
temp-*

# Lists all ignored files in this project
$ git ls-files --other --ignored --exclude-standard
```

**SAVE FRAGMENTS**

```
# Temporarily stores all modified tracked files
$ git stash

# Lists all stashed changesets
$ git stash list

# Restores the most recently stashed files
$ git stash pop

# Discards the most recently stashed changeset
$ git stash drop
```

**SYNCHRONIZE CHANGES**

```
# Downloads all history from the repository bookmark
$ git fetch [bookmark]

# Combines bookmark’s branch into current local branch
$ git merge [bookmark]/[branch]

# Uploads all local branch commits to GitHub
$ git push [alias] [branch]

# Downloads bookmark history and incorporates changes
$ git pull
```

**REDO COMMITS**

```
# Undoes all commits afer [commit], preserving changes locally
$ git reset [commit]

# Discards all history and changes back to the specified commit
$ git reset --hard [commit]
```

**REVIEW HISTORY**

```
# Lists version history for the current branch
$ git log

# Lists version history for a file, including renames
$ git log --follow [file]

# Shows content differences between two branches
$ git diff [first-branch]...[second-branch]

# Outputs metadata and content changes of the specified commit
$ git show [commit]
```

**GIT TAG**

```
# Tag a specific commit
git tag -a v1 f855792
git tag v1-test f855792

# Push remote a specific tag
git push origin v1

# Push remote all tags
git push origin --tags
```

**CLEAR LOCAL CACHE**

```
git rm -r --cached .
git add .
git commit -am 'git cache cleared'
git push
```

**TIPS&TRICKS**

```
# Stop displaying branch in page mode
git config --global pager.branch false
```


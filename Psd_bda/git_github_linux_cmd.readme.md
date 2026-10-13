# Git, GitHub & Linux Commands — Complete Cheat Sheet

A structured, beginner-friendly reference guide to essential Git, GitHub, and Linux commands, with syntax, examples, and explanations.

This README is intended for developers, students, and anyone working on software development, data engineering, Big Data, or cloud computing projects.

---

## Table of Contents

- [1. Git vs GitHub](#1-git-vs-github)
- [2. Git Configuration](#2-git-configuration)
- [3. Creating and Cloning Repositories](#3-creating-and-cloning-repositories)
- [4. Basic Git Workflow](#4-basic-git-workflow)
- [5. Git Branching and Merging](#5-git-branching-and-merging)
- [6. Git Remote Commands](#6-git-remote-commands)
- [7. Undoing Changes in Git](#7-undoing-changes-in-git)
- [8. Git Stashing and Tags](#8-git-stashing-and-tags)
- [9. Common Git Errors](#9-common-git-errors)
- [10. Essential Linux Commands](#10-essential-linux-commands)
- [11. Linux File and Directory Operations](#11-linux-file-and-directory-operations)
- [12. Linux Permissions](#12-linux-permissions)
- [13. Linux Search and Text Processing](#13-linux-search-and-text-processing)
- [14. Linux Process and System Commands](#14-linux-process-and-system-commands)
- [15. Linux Redirection and Pipes](#15-linux-redirection-and-pipes)
- [16. Linux Networking and Archives](#16-linux-networking-and-archives)
- [17. Useful Linux Shortcuts](#17-useful-linux-shortcuts)
- [18. Windows PowerShell vs Linux](#18-windows-powershell-vs-linux)
- [19. Common Git Workflow](#19-common-git-workflow)
- [20. Important Safety Tips](#20-important-safety-tips)

---

# 1. Git vs GitHub

| Git | GitHub |
|---|---|
| A distributed version control system. | An online platform for hosting Git repositories. |
| Tracks changes in files. | Stores repositories remotely and enables collaboration. |
| Works locally on your computer. | Accessible over the internet. |
| Supports commits, branches, merges, and history. | Supports pull requests, issues, reviews, and project collaboration. |

**Example:** Git tracks the changes you make to your Python code, while GitHub allows you to store and share that code online.

## Important Git terminology

| Term | Meaning |
|---|---|
| Repository | A project tracked by Git. |
| Working directory | The files you are currently editing. |
| Staging area | The changes selected for the next commit. |
| Commit | A saved snapshot of staged changes. |
| Branch | An independent line of development. |
| Merge | Combines changes from different branches. |
| Remote | A reference to a repository hosted elsewhere. |
| Clone | Creates a local copy of a remote repository. |
| Push | Sends local commits to a remote repository. |
| Pull | Fetches remote changes and integrates them into the current branch. |
| Fetch | Downloads remote updates without integrating them. |
| Pull request | A GitHub feature for proposing and reviewing changes before merging. |

## How Git works

```text
Working Directory
       |
       | git add
       v
 Staging Area
       |
       | git commit
       v
 Local Repository
       |
       | git push
       v
 Remote Repository (GitHub)
```

---

# 2. Git Configuration

Configure Git before starting your first project.

### `git --version`

Displays the installed Git version.

```bash
git --version
```

### `git config`

Sets or displays Git configuration values.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

- `--global`: Applies the setting to your user account across repositories.
- `user.name`: Sets the name recorded in commits.
- `user.email`: Sets the email recorded in commits.

Check your configuration:

```bash
git config --global --list
git config user.name
git config user.email
```

### `git help`

Displays documentation for Git commands.

```bash
git help commit
git help branch
```

You can also use:

```bash
git commit --help
```

---

# 3. Creating and Cloning Repositories

### `git init`

Initializes a new Git repository in the current directory.

```bash
git init
```

Use this when you have an existing project on your computer and want to start tracking it with Git.

### `git clone`

Downloads an existing repository and creates a local copy.

```bash
git clone https://github.com/username/repository.git
```

Clone into a directory with a custom name:

```bash
git clone https://github.com/username/repository.git my-project
```

### `git status`

Shows the current branch and the status of your files.

```bash
git status
git status --short
```

It helps you identify:

- Modified files.
- New, untracked files.
- Files staged for commit.
- Changes that have already been committed.

### `git log`

Displays commit history.

```bash
git log
git log --oneline
git log --oneline --graph --all
```

- `--oneline`: Displays each commit on one line.
- `--graph`: Shows branch and merge history graphically.
- `--all`: Includes commits reachable from all local references.

---

# 4. Basic Git Workflow

These are the Git commands you will use most frequently.

### `git add`

Moves changes into the staging area.

Stage one file:

```bash
git add app.py
```

Stage multiple files:

```bash
git add app.py README.md
```

Stage all changes in the current directory and its subdirectories:

```bash
git add .
```

Stage all changes throughout the working tree, including deletions:

```bash
git add -A
```

**Remember:** `git add` stages changes; it does not create a commit.

### `git commit`

Records staged changes in the local repository.

```bash
git commit -m "Add login functionality"
```

- `-m`: Specifies the commit message.

A good commit message briefly describes the change.

Examples:

```bash
git commit -m "Add README documentation"
git commit -m "Fix database connection"
git commit -m "Implement binary search"
```

### `git diff`

Shows differences between versions of files.

```bash
git diff
```

Shows unstaged changes.

```bash
git diff --staged
```

Shows staged changes that will be included in the next commit.

### `git show`

Displays information about a particular commit, including its changes.

```bash
git show
git show <commit-hash>
```

### `git restore`

Restores files in the working directory.

Discard unstaged changes to a file:

```bash
git restore app.py
```

Unstage a file while preserving its working-directory changes:

```bash
git restore --staged app.py
```

**Warning:** Restoring a file without `--staged` can permanently discard its uncommitted edits.

---

# 5. Git Branching and Merging

Branches allow you to develop features or fix bugs independently of the main line of development.

### `git branch`

Lists local branches.

```bash
git branch
git branch -a
```

- `-a`: Lists local and remote-tracking branches.

Create a new branch:

```bash
git branch feature-login
```

### `git switch`

Switches to another branch.

```bash
git switch main
```

Create and switch to a new branch:

```bash
git switch -c feature-login
```

### `git checkout`

An older, still-supported command that can switch branches and restore files.

```bash
git checkout main
git checkout -b feature-login
```

For new workflows, `git switch` and `git restore` make these separate tasks clearer.

### `git merge`

Combines changes from another branch into the current branch.

```bash
git switch main
git merge feature-login
```

The example merges `feature-login` into `main`.

### `git branch -d`

Deletes a local branch that Git considers safely merged.

```bash
git branch -d feature-login
```

Force-delete a local branch:

```bash
git branch -D feature-login
```

**Warning:** `-D` can delete a branch even when its changes have not been merged.

### Delete a remote branch

```bash
git push origin --delete feature-login
```

This deletes the branch from the remote repository named `origin`.

---

# 6. Git Remote Commands

Remote commands connect your local repository with GitHub or another Git hosting service.

### `git remote -v`

Lists remote repositories and their URLs.

```bash
git remote -v
```

### `git remote add`

Connects your local repository to a remote repository.

```bash
git remote add origin https://github.com/username/repository.git
```

Here, `origin` is the conventional name for the remote.

### `git remote set-url`

Changes the URL associated with an existing remote.

```bash
git remote set-url origin https://github.com/username/new-repository.git
```

### `git fetch`

Downloads updates from a remote without merging them into your current branch.

```bash
git fetch origin
git fetch --all
```

### `git pull`

Fetches remote changes and integrates them into the current branch.

```bash
git pull origin main
```

### `git push`

Uploads local commits to a remote repository.

```bash
git push origin main
```

For the first push of a new branch:

```bash
git push -u origin feature-login
```

`-u` sets the upstream tracking branch, so future pushes and pulls can often use shorter commands.

### `git ls-remote`

Lists references advertised by a remote repository.

```bash
git ls-remote origin
```

Useful when you want to inspect remote branches and tags without cloning the repository.

---

# 7. Undoing Changes in Git

Choose the command based on what you want to undo.

| Situation | Command | Effect |
|---|---|---|
| Discard unstaged edits to a file | `git restore file.py` | Restores the file from the index. |
| Unstage a file | `git restore --staged file.py` | Keeps working-directory edits. |
| Undo a commit safely | `git revert <hash>` | Creates a new commit that reverses the target commit. |
| Move the current branch pointer back | `git reset --soft HEAD~1` | Keeps changes staged. |
| Move the current branch pointer back | `git reset --mixed HEAD~1` | Keeps changes in the working directory, unstaged. |
| Move the current branch pointer back | `git reset --hard HEAD~1` | Discards tracked changes covered by the reset. |

### `git revert`

Reverses a commit by creating another commit.

```bash
git revert <commit-hash>
```

This is generally preferable when undoing changes that have already been shared with others.

### `git reset`

Moves the current branch pointer to another commit.

Keep the changes staged:

```bash
git reset --soft HEAD~1
```

Keep the changes but unstage them:

```bash
git reset --mixed HEAD~1
```

Discard tracked working-tree changes covered by the reset:

```bash
git reset --hard HEAD~1
```

**Important:** `HEAD~1` means the first parent of the current commit. `--hard` can destroy uncommitted work. Untracked files are not automatically removed by `git reset --hard`.

### `git reflog`

Shows recent movements of local references, including many resets and branch switches.

```bash
git reflog
```

It can help recover commits that are no longer visible in the current branch history, provided the relevant reflog entry still exists.

### `git clean`

Removes untracked files.

Preview what would be deleted:

```bash
git clean -n
```

Remove untracked files:

```bash
git clean -f
```

Remove untracked files and directories:

```bash
git clean -fd
```

**Warning:** This is destructive. Preview the results before executing it.

---

# 8. Git Stashing and Tags

## Git stash

Temporarily saves working changes so you can switch tasks without committing them.

Save tracked changes:

```bash
git stash
```

Include untracked files:

```bash
git stash -u
```

List saved stashes:

```bash
git stash list
```

Apply the most recent stash and keep it in the stash list:

```bash
git stash apply
```

Apply the most recent stash and remove it from the stash list if successful:

```bash
git stash pop
```

Delete a particular stash:

```bash
git stash drop stash@{0}
```

## Git tags

Tags mark particular commits, commonly for releases.

Create a lightweight tag:

```bash
git tag v1.0
```

Create an annotated tag:

```bash
git tag -a v1.0 -m "Version 1.0 release"
```

List tags:

```bash
git tag
```

Push a tag:

```bash
git push origin v1.0
```

Push all local tags:

```bash
git push origin --tags
```

Delete a local tag:

```bash
git tag -d v1.0
```

Delete a remote tag:

```bash
git push origin --delete v1.0
```

---

# 9. Common Git Errors

## Error 1: `fatal: not a git repository`

**Cause:** You are outside a Git repository or the directory is not initialized.

Check your current directory:

```bash
pwd
```

Move into your project directory:

```bash
cd my-project
```

Or initialize Git if this is a new project:

```bash
git init
```

## Error 2: `error: You have not concluded your merge (MERGE_HEAD exists)`

**Cause:** A previous merge is still in progress.

Check the state:

```bash
git status
```

If conflicts exist, resolve them in the affected files, then stage the resolved files and finish the merge:

```bash
git add .
git commit
```

If you intentionally want to cancel the merge and Git permits it:

```bash
git merge --abort
```

Do not abort blindly if you have work from before the merge that you need to preserve.

## Error 3: `rejected — non-fast-forward`

**Cause:** The remote branch has commits that your local branch does not contain.

A common approach is:

```bash
git pull --rebase origin main
git push origin main
```

Resolve any conflicts if they arise. Check `git status` to see whether the rebase is in progress.

## Error 4: `fatal: refusing to merge unrelated histories`

**Cause:** Git cannot find a common ancestor between the histories being merged.

If you intentionally want to combine two independently created histories:

```bash
git pull origin main --allow-unrelated-histories
```

This may produce conflicts. Resolve them before completing the merge.

**Note:** This option should not be used automatically for every pull error. Confirm that combining the two histories is actually intended.

## Error 5: `remote origin already exists`

**Cause:** A remote named `origin` is already configured.

Check the existing remote:

```bash
git remote -v
```

Update its URL if necessary:

```bash
git remote set-url origin https://github.com/username/repository.git
```

## Error 6: Merge conflict

**Cause:** Git cannot automatically reconcile conflicting changes.

Typical workflow:

```bash
git status
```

Open the conflicted files and look for markers such as:

```text
<<<<<<< HEAD
Your changes
=======
Incoming changes
>>>>>>> feature-branch
```

Edit the file to keep the intended result, remove the markers, then:

```bash
git add <resolved-file>
git commit
```

For a conflict during rebase, use `git rebase --continue` instead of creating a normal merge commit. To cancel the rebase, use `git rebase --abort`.

---

# 10. Essential Linux Commands

Linux commands are useful for working with Ubuntu, servers, virtual machines, Hadoop, Spark, and cloud environments.

## Navigation

| Command | Purpose | Example |
|---|---|---|
| `pwd` | Displays the current working directory. | `pwd` |
| `ls` | Lists files and directories. | `ls` |
| `ls -l` | Displays a detailed listing. | `ls -l` |
| `ls -a` | Includes hidden files. | `ls -a` |
| `ls -lh` | Displays file sizes in a readable format. | `ls -lh` |
| `cd` | Changes the current directory. | `cd Documents` |
| `cd ..` | Moves to the parent directory. | `cd ..` |
| `cd ~` | Moves to your home directory. | `cd ~` |
| `cd /` | Moves to the filesystem root. | `cd /` |
| `clear` | Clears the terminal display. | `clear` |
| `history` | Shows previously entered commands. | `history` |
| `man` | Opens a command's manual page. | `man ls` |
| `whoami` | Displays the current username. | `whoami` |

### Linux paths

- `/` — filesystem root.
- `~` — your home directory.
- `.` — current directory.
- `..` — parent directory.
- `/home/username` — an example of a user's home directory.

Example:

```bash
cd ~/Documents
pwd
ls -la
```

This moves to the Documents directory under your home directory, prints its path, and lists its contents, including hidden files.

---

# 11. Linux File and Directory Operations

| Command | Purpose | Example |
|---|---|---|
| `touch` | Creates an empty file if it does not exist; updates its timestamp otherwise. | `touch notes.txt` |
| `mkdir` | Creates a directory. | `mkdir projects` |
| `mkdir -p` | Creates parent directories as needed. | `mkdir -p data/raw` |
| `cp` | Copies files. | `cp a.txt b.txt` |
| `cp -r` | Copies a directory and its contents recursively. | `cp -r src backup` |
| `mv` | Moves or renames a file or directory. | `mv old.txt new.txt` |
| `rm` | Removes files. | `rm notes.txt` |
| `rmdir` | Removes an empty directory. | `rmdir empty_dir` |
| `rm -r` | Removes a directory and its contents recursively. | `rm -r old_folder` |
| `file` | Identifies a file's type. | `file data.csv` |
| `stat` | Displays file metadata. | `stat notes.txt` |
| `ln -s` | Creates a symbolic link. | `ln -s source.txt link.txt` |

## Viewing file contents

| Command | Purpose | Example |
|---|---|---|
| `cat` | Prints file contents. | `cat notes.txt` |
| `less` | Views a file page by page. | `less large.log` |
| `head` | Shows the first 10 lines by default. | `head data.csv` |
| `head -n 20` | Shows the first 20 lines. | `head -n 20 data.csv` |
| `tail` | Shows the last 10 lines by default. | `tail app.log` |
| `tail -n 50` | Shows the last 50 lines. | `tail -n 50 app.log` |
| `tail -f` | Follows new lines added to a file. | `tail -f app.log` |
| `wc -l` | Counts lines. | `wc -l data.csv` |
| `du -sh` | Shows the total size of a file or directory. | `du -sh dataset` |
| `df -h` | Shows filesystem disk space. | `df -h` |

**Example:**

```bash
mkdir data
touch data/sample.txt
echo "Hello Linux" > data/sample.txt
cat data/sample.txt
```

This creates a directory and file, writes text into the file, and displays the contents.

---

# 12. Linux Permissions

Linux permissions control who can read, write, or execute files.

## Understanding permissions

Example output from `ls -l`:

```text
-rwxr-xr-- 1 user group 1200 Oct 10 script.sh
```

The permissions are divided into three groups:

- `rwx` — owner permissions.
- `r-x` — group permissions.
- `r--` — permissions for others.

| Symbol | Meaning | Numeric value |
|---|---|---:|
| `r` | Read | 4 |
| `w` | Write | 2 |
| `x` | Execute | 1 |
| `-` | Permission absent | 0 |

## `chmod`

Changes file permissions.

Add execute permission for the owner:

```bash
chmod u+x script.sh
```

Remove write permission for others:

```bash
chmod o-w script.sh
```

Set permissions numerically:

```bash
chmod 755 script.sh
chmod 644 notes.txt
```

- `755` means owner: read/write/execute; group and others: read/execute.
- `644` means owner: read/write; group and others: read-only.

## `chown`

Changes file ownership.

```bash
sudo chown username:groupname file.txt
```

## `sudo`

Runs a command with elevated privileges, subject to system permissions and policy.

```bash
sudo apt update
```

**Safety:** Understand what a privileged command does before executing it. Avoid running unfamiliar commands copied from the internet with `sudo`.

---

# 13. Linux Search and Text Processing

These commands are particularly useful when analyzing logs, CSV files, configuration files, and program output.

## `grep`

Searches text for a pattern.

```bash
grep "ERROR" app.log
```

Case-insensitive search:

```bash
grep -i "error" app.log
```

Search recursively inside a directory:

```bash
grep -r "TODO" .
```

Show matching line numbers:

```bash
grep -n "ERROR" app.log
```

## `find`

Searches for files and directories.

Find a file by name:

```bash
find . -name "data.csv"
```

Find Python files:

```bash
find . -type f -name "*.py"
```

Find directories:

```bash
find . -type d
```

## `sort`

Sorts lines of text.

```bash
sort names.txt
sort -n numbers.txt
```

`-n` sorts numbers numerically.

## `uniq`

Displays or counts adjacent duplicate lines.

```bash
sort names.txt | uniq
sort names.txt | uniq -c
```

Sorting first allows duplicates that occur at different positions to become adjacent.

## `cut`

Extracts selected fields or character positions.

```bash
cut -d ',' -f 1 data.csv
```

This uses a comma delimiter and extracts the first field from each line. It is suitable for simple delimited text, not every CSV file format.

## `awk`

Processes text by fields and patterns.

```bash
awk '{print $1}' file.txt
```

Prints the first whitespace-separated field from each line.

For a simple comma-separated file:

```bash
awk -F ',' '{print $1}' data.csv
```

## `sed`

Transforms text, often by replacing patterns.

```bash
sed 's/old/new/g' file.txt
```

Prints a version of the file in which each occurrence of `old` is replaced with `new`; it does not modify the original file.

## `sort`, `uniq`, and `wc` together

```bash
sort names.txt | uniq -c | sort -nr
```

Counts repeated lines and sorts the counts in descending numerical order.

---

# 14. Linux Process and System Commands

| Command | Purpose | Example |
|---|---|---|
| `ps` | Displays process information. | `ps aux` |
| `top` | Monitors running processes and resource usage. | `top` |
| `free -h` | Displays memory usage. | `free -h` |
| `uptime` | Shows system uptime and load averages. | `uptime` |
| `uname -a` | Displays kernel and system information. | `uname -a` |
| `hostname` | Displays the system hostname. | `hostname` |
| `date` | Displays the system date and time. | `date` |
| `kill` | Sends a signal to a process. | `kill 1234` |
| `kill -9` | Forcefully terminates a process. | `kill -9 1234` |
| `jobs` | Lists jobs started in the current shell. | `jobs` |
| `bg` | Resumes a suspended job in the background. | `bg %1` |
| `fg` | Brings a shell job to the foreground. | `fg %1` |

### `kill`

By default, `kill PID` sends `SIGTERM`, requesting that the process terminate gracefully.

```bash
kill 1234
```

Use `kill -9` only when necessary because it sends `SIGKILL`, which the process cannot catch or handle for cleanup.

### `&`

Runs a command in the background.

```bash
python script.py &
```

### `killall`

Sends a signal to processes matching a name, where supported.

```bash
killall python
```

**Warning:** This may terminate multiple processes. Inspect the processes first and avoid using it when you are unsure which programs match.

---

# 15. Linux Redirection and Pipes

Redirection and pipes connect commands together and are fundamental to shell scripting and data processing.

## Output redirection: `>`

Writes output to a file, replacing its previous contents.

```bash
echo "Hello" > output.txt
```

## Append output: `>>`

Adds output to the end of a file.

```bash
echo "Another line" >> output.txt
```

## Input redirection: `<`

Uses a file as a command's standard input.

```bash
sort < names.txt
```

## Pipe: `|`

Sends one command's standard output to another command's standard input.

```bash
cat app.log | grep "ERROR"
```

A simpler equivalent is:

```bash
grep "ERROR" app.log
```

Another example:

```bash
ps aux | grep python
```

This searches the displayed process list for lines containing `python`.

## Error redirection: `2>`

Redirects standard error to a file.

```bash
python script.py 2> errors.log
```

## Redirect both standard output and standard error

```bash
python script.py > output.log 2>&1
```

This sends standard output to `output.log` and then redirects standard error to the same destination.

---

# 16. Linux Networking and Archives

## Networking commands

| Command | Purpose | Example |
|---|---|---|
| `ping` | Tests connectivity using ICMP echo requests, if permitted. | `ping example.com` |
| `curl` | Transfers data to or from URLs. | `curl https://example.com` |
| `wget` | Downloads files from supported URLs. | `wget https://example.com/file.zip` |
| `ip addr` | Displays network interface addresses. | `ip addr` |
| `ip route` | Displays routing information. | `ip route` |
| `ss -tuln` | Lists listening TCP/UDP sockets with numeric addresses. | `ss -tuln` |
| `ssh` | Connects to a remote system securely. | `ssh user@server` |
| `scp` | Copies files over SSH. | `scp file.txt user@server:/home/user/` |

A failed `ping` does not necessarily mean a server is unavailable; ICMP traffic may be blocked.

## Archive commands

### `tar`

Creates and extracts archive files.

Create a compressed `.tar.gz` archive:

```bash
tar -czf backup.tar.gz project/
```

Extract an archive:

```bash
tar -xzf backup.tar.gz
```

List the contents of an archive:

```bash
tar -tzf backup.tar.gz
```

Options:

- `-c`: Create an archive.
- `-x`: Extract an archive.
- `-z`: Use gzip compression.
- `-f`: Specify the archive filename.
- `-v`: Show processed files.

### `zip` and `unzip`

Create a ZIP archive:

```bash
zip -r project.zip project/
```

Extract a ZIP archive:

```bash
unzip project.zip
```

List its contents:

```bash
unzip -l project.zip
```

---

# 17. Useful Linux Shortcuts

| Shortcut | Purpose |
|---|---|
| `Ctrl + C` | Interrupts the foreground process. |
| `Ctrl + Z` | Suspends the foreground process. |
| `Ctrl + D` | Sends end-of-file input; often exits a shell when used at an empty prompt. |
| `Ctrl + L` | Clears the terminal display in many shells. |
| `Tab` | Completes commands, filenames, and paths. |
| `↑` / `↓` | Navigates command history. |
| `Ctrl + R` | Searches command history in many shells. |
| `!!` | Repeats the previous command in supported shells. |
| `cd -` | Returns to the previous working directory. |

---

# 18. Windows PowerShell vs Linux

Since Git can be used directly in Windows PowerShell, you do not need Ubuntu merely to learn Git.

However, Linux commands are useful when working with Ubuntu, Hadoop, Spark, and Linux-based cloud servers.

| Task | Windows PowerShell | Linux / Ubuntu |
|---|---|---|
| Show current directory | `Get-Location` | `pwd` |
| List files | `Get-ChildItem` or `ls` | `ls` |
| Change directory | `Set-Location folder` or `cd folder` | `cd folder` |
| Create a directory | `New-Item -ItemType Directory folder` | `mkdir folder` |
| Create a file | `New-Item file.txt -ItemType File` | `touch file.txt` |
| Copy a file | `Copy-Item a.txt b.txt` | `cp a.txt b.txt` |
| Move or rename a file | `Move-Item a.txt b.txt` | `mv a.txt b.txt` |
| Remove a file | `Remove-Item file.txt` | `rm file.txt` |
| Display a file | `Get-Content file.txt` | `cat file.txt` |
| Search text | `Select-String "ERROR" app.log` | `grep "ERROR" app.log` |
| Clear the terminal | `Clear-Host` or `cls` | `clear` |

**Important:** PowerShell aliases can make commands such as `ls`, `cat`, and `curl` behave differently from their Linux counterparts. The underlying command syntax and available options are not always the same.

Git commands such as `git status`, `git add`, `git commit`, `git pull`, and `git push` are generally the same in both environments.

---

# 19. Common Git Workflow

This is the everyday workflow for making changes to an existing GitHub project.

## Step 1: Open the project

```bash
cd my-project
```

## Step 2: Check the current state

```bash
git status
git branch
git remote -v
```

## Step 3: Get the latest changes

```bash
git pull
```

This works when the current branch has an appropriate upstream configured.

## Step 4: Make your code changes

Edit the required files in your editor.

## Step 5: Review your changes

```bash
git diff
git status
```

## Step 6: Stage your changes

```bash
git add .
```

## Step 7: Commit the changes

```bash
git commit -m "Describe the changes"
```

## Step 8: Push to GitHub

```bash
git push
```

If your branch does not have an upstream configured, set one:

```bash
git push -u origin main
```

Replace `main` with your actual branch name when necessary.

## Workflow summary

```text
Pull latest changes
        |
        v
Edit files
        |
        v
Review changes (git diff)
        |
        v
Stage changes (git add)
        |
        v
Commit changes (git commit)
        |
        v
Push to GitHub (git push)
```

---

# 20. Important Safety Tips

1. **Check before deleting:** Review files before using `rm -r`, `git clean -f`, or `git reset --hard`.
2. **Understand staging:** `git add` selects changes; `git commit` records them locally.
3. **Do not confuse push and pull:** Push sends commits to a remote; pull fetches and integrates remote changes.
4. **Fetch before investigating remote history:** `git fetch origin` updates remote-tracking information without merging it into your branch.
5. **Resolve conflicts deliberately:** Inspect both sides of a conflict instead of accepting one side automatically.
6. **Avoid force-pushing shared branches:** `git push --force` can overwrite remote history. If rewriting history is necessary, `git push --force-with-lease` offers an additional safeguard, but still requires care.
7. **Keep credentials out of Git:** Never commit passwords, access tokens, private keys, or `.env` files containing secrets.
8. **Use `.gitignore`:** Exclude generated files, dependency directories, local configuration, and other files that should not be tracked.
9. **Use meaningful commit messages:** Make it easy to understand what changed and why.
10. **Read command help:** Use `git help <command>` or `man <command>` when unsure about options.

---

## Quick Reference: 15 Commands to Remember

| Command | What it does |
|---|---|
| `git status` | Checks the repository state. |
| `git add .` | Stages changes under the current directory. |
| `git commit -m "message"` | Records staged changes. |
| `git pull` | Fetches and integrates remote changes. |
| `git push` | Uploads commits to the configured remote branch. |
| `git log --oneline` | Displays compact commit history. |
| `git switch -c branch` | Creates and switches to a branch. |
| `git merge branch` | Merges a branch into the current branch. |
| `pwd` | Shows the current directory. |
| `ls -la` | Lists files, including hidden files. |
| `cd folder` | Changes directory. |
| `mkdir folder` | Creates a directory. |
| `cp source destination` | Copies a file. |
| `grep "text" file` | Searches a file for matching text. |
| `find . -name "*.py"` | Finds Python files under the current directory. |

---

## Recommended Learning Order

1. Learn Git basics: `status`, `add`, `commit`, `log`, and `diff`.
2. Practice GitHub operations: `clone`, `pull`, `push`, and `remote`.
3. Understand branching, merging, and conflict resolution.
4. Learn safe recovery commands: `restore`, `revert`, `reset`, and `reflog`.
5. Learn Linux navigation and file operations.
6. Practice Linux permissions, text processing, and pipes.
7. Learn process management, networking, and archives.
8. Apply these commands in real projects and Linux-based Big Data environments.

**The best way to learn these commands is to use them in your own projects rather than memorize them individually.**

---

## Contributing

If you find an error or want to add a useful command, feel free to improve this reference.

## License

This documentation may be reused and adapted for personal learning and educational purposes.

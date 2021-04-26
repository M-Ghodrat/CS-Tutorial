# How delete files from local/remote repository

### 1. If you want to push a deleted file to remote:
```
git add <deleted file name>
git commit -m <message>
git push -u origin branch
```

### 2. If you want to delete a file from remote and locally

```
git rm <file name>
git commit -m <message>
git push -u origin branch
```

### 3. If you want to delete a file from remote only

```
git rm --cached <file name>
git commit -m <message>
git push -u origin branch
```

#### 4. Remove a specific file from the staging area:

```
git restore --staged <individual_file>
```
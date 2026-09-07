# 📚
Para meus estudos de **python** e alguns **códigos git**.
# 💻 Git Notes: Terminal Commands Guide

This repository contains my personal notes and quick references for essential **Git** commands. The main goal is to serve as a practical, day-to-day cheat sheet for using Git via the terminal.

---

## 📌 Table of Contents

- [Initial Configuration](#-initial-configuration)
- [Initializing and Cloning Repositories](#-initializing-and-cloning-repositories)
- [File Lifecycle (Basic Workflow)](#-file-lifecycle-basic-workflow)
- [Syncing with Remote Repositories](#-syncing-with-remote-repositories)
- [Working with Branches](#-working-with-branches)
- [History and Undoing Changes](#-history-and-undoing-changes)

---

## ⚙️ Initial Configuration

Before making any commits, you need to configure your global Git identity:

```bash
# Sets the name linked to your commits
git config --global user.name "Your Name"

# Sets the email linked to your GitHub account
git config --global user.email "your-email@provider.com"

# Verifies your current configurations
git config --list
```

---

## 📁 Initializing and Cloning Repositories

```bash
# Initializes a new local Git repository in an existing folder
git init

# Downloads an existing repository from GitHub to your computer
git clone <repository-url>
```

---

## 🔄 File Lifecycle (Basic Workflow)

The core workflow to save your local changes consists of three main steps:

```bash
# 1. Checks the current status of files (modified, staged, or untracked)
git status

# 2. Adds a specific file to the Staging Area
git add filename.txt

# 2b. Adds ALL modified and new files at once
git add .

# 3. Permanently records your staged changes with a descriptive message
git commit -m "Brief explanation of what was done"
```

---

## ☁️ Syncing with Remote Repositories

To send your local commits to the cloud (GitHub, GitLab, etc.) or fetch new updates:

```bash
# Links your local repository to a remote server for the first time
git remote add origin <remote-repository-url>

# Pushes your local commits to the remote server (main branch) and sets upstream
git push -u origin main

# Pushes future updates (after the first push is configured)
git push

# Updates your local repository with changes from the remote server
git pull
```

---

## 🌿 Working with Branches

Branches allow you to work on new features or bug fixes without affecting the main source code.

```bash
# Lists all local branches (the active one will have an asterisk)
git branch

# Creates a new branch
git branch new-branch-name

# Switches to an existing branch
git switch branch-name

# Shortcut: Creates and switches to the new branch at the same time
git checkout -b new-branch-name

# Merges changes from the specified branch into your current branch
git merge other-branch-name
```

---

## 📜 History and Undoing Changes

```bash
# Shows the commit history for the project
git log

# Shows a simplified history with one line per commit
git log --oneline

# Removes a file from the Staging Area (undoes 'git add' before committing)
git reset filename.txt

# Undoes the last commit but keeps your local changes intact
git reset --soft HEAD~1
```

---

> 💡 **Pro Tip:** Keep an eye out for conflicts during `git merge` or `git pull`. The terminal will warn you if changes happen on the exact same line of the same file, letting you choose which version to keep before finalizing.


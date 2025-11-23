# MAAI Bootcamp :: Basic Git

In this session, we will cover the fundamentals of Git, common Git commands, handling merge conflicts, working with branches, and a hands-on exercise to practice these concepts.

Git and GitLab are essential tools in the Master of Applied AI program. Throughout this bootcamp, each group will work with GitLab repositories to store project resources (e.g., source code, experiment results, and documentation such as coaching session summaries, expert reviews, and annotations).

>This session is based on the Git Tutorial provided by GitLab and [available here](https://docs.gitlab.com/ee/topics/git/). Some explanations were used and changed to accommodate the subject within the MAAI bootcamp's timeframe. 

## Step 1: Git Fundamentals

### What is Git?

* Git is a version control system that helps you track changes to code, collaborate with others, and maintain a complete history of your project. It allows you to revert to previous versions and manage contributions from multiple team members efficiently.
* GitLab is a web-based Git repository manager that allows teams to host and manage their Git repositories. HvA has its own GitLab server, which you can access [here](https://gitlab.fdmci.hva.nl/).

### What is a Repository?

A Git repository is a central location where your project files are stored, including the entire history of changes made to the files. Repositories can be hosted on GitLab, and you can clone them to work locally on your machine.

When you clone a repository, Git creates a working directory on your local machine. This directory is where you make changes, and Git tracks any modifications. Once you're ready to share your work, you push those changes back to the remote repository on GitLab.

## Step 2: Familiarize Yourself with Git Commands

To work with Git effectively, you need to understand the basic Git commands. These commands allow you to clone repositories, stage changes, commit, and push code, among other actions. Here are some essential commands to start with:

### git clone

Clone a repository to your local machine

Syntax: 

```
git clone <repository-url>
```

Example:

```
git clone git@gitlab.fdmci.hva.nl:maai/2024-2025-b1/pg-c1-t0.git
```

### git status

Check the presence of unchecked files, not yet in the staging area.

### git add

Stage changes to be committed.

Syntax:

```
git add <file>
```

Example:

```
git add README.md
```

Here we assume that a new README.md file was created in the local folder.

### git commit

Commit the staged changes with a message

Syntax:
```
git commit -m "message here"
```

Example:

```
git commit -m "initial version"
```

### git push

Push local commits to the remote repository: 

Syntax:

```
git push origin <branch-name>
```

Example:

Without parameters, it will push to the current branch.

```
git push
```

### git pull

Fetch and merge changes from the remote repository into your local branch.

Syntax:

```
git pull origin <branch-name>
```

Example:

Without parameters, it will pull from the current branch.

```
git pull
```
 
### git branch

List, create, or delete branches: 

Examples:
* listing branches: `git branch`
* creating a branch: `git branch branch-1` followed by `git checkout branch-1`. A shorthad for both commands can be `git checkout -b branch-1`

A Git repository is essentially a directory containing all a project's files, folders, and version history. It is a central hub where you can store, manage, and share your code or content.

When you initialize a Git repository or clone an existing one, Git creates a hidden directory called .git in the project directory. This hidden directory contains all the necessary metadata and objects that Git uses to manage the repository, including the complete history of changes made to the files. Git tracks changes at the file level so that you can view the modifications made to individual files over time.

To create and change code, you clone a Git repository and work in the local copy in your working directory. Then, to collaborate, you push your changes to a remote Git repository hosted on GitLab. Then, the changes are available to other team members. You can also pull modifications made by others so that your local repository stays up to date.

## Step 2: Learn about branching and merging

In Git, you use branches so that you and your team can work on different features, bug fixes, or experiments simultaneously without interfering with each other's work. 

You can then make changes, commit them, and test them in isolation without impacting the stability of the default branch. Branches can be created, merged, and deleted.

The default branch is usually called main. After a feature is complete or a bug is fixed, you can merge the changes from your branch into the default branch. Merging combines the changes from one branch into another.

If conflicts arise during the merge process (for example, if the same lines of code have been modified in both branches), the conflicts must be resolved manually. After a successful merge, the branch can be deleted if it is no longer needed. Deleting the branch helps keep the repository organized and maintainable.

For more information, see [Branches](https://docs.gitlab.com/ee/user/project/repository/branches/index.html).

## Step 3: Understand the Git workflow

A typical Git workflow involves the following steps:

- Cloning a repository to your local machine.
- Creating a new branch for your changes.
- Making changes to files in your working directory.
- Staging the changes you want to commit.
- Committing the changes to your local repository.
- Pushing the changes to the remote repository.
- Merging your branch into the default branch.

Step 4: Familiarize yourself with Git commands

To work with Git from the command line, you need to use various Git commands. Some of the most commonly used commands include:

- git clone: Clone a repository to your local machine
- git branch: List, create, or delete branches
- git checkout: Switch between branches
- git add: Stage changes for commit
- git commit: Commit staged changes to your local repository
- git push: Push local commits to the remote repository
- git pull: Fetch changes from the remote repository and merge them into your local branch

For more information, see [Command line Git](https://docs.gitlab.com/ee/topics/git/commands.html)

## Step 5: Practice using Git

### Activity

We are following the GitLab tutorial called [Make your first Git commit](https://docs.gitlab.com/ee/tutorials/make_first_git_commit/index.html)

You should follow the tutorial and reach the following objectives:

1. Basic setup
    1. Create a new repository from the [HvA GitLab server](https://gitlab.fdmci.hva.nl/)
    2. Clone the repository in your local computer
2. Feature branch creation
    1. Create a branch to accommodate your changes (e.g. day1-feature)
    2. Move to the newly created branch
3. Working within the branch
    1. Create a README.md file with information about your project. Note that this file uses the [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) notation. Use some time to familiarise yourself with this notation. 
    2. Add a .gitignore file to the root folder of your project. It prevents versioning undesired content, such as temporary files and large datasets. You can reuse the .gitignore file from the bootcamp repository.
    3. In the repository folder, create a folder called *d1*
    4. In this newly added folder, add your Jupyter Notebook file
4. Updating the branch
    1. Stage your changes
    2. Commit your changes
    3. Push your changes within the newly created branch to the remote repository
5. Merging
    1. Move back to the main branch
    2. Merge the contents from *day1-feature* to *main*


# Summary

In this session, we covered the basic concepts of Git and the essential commands you can use. Note that there is much more: examples are the use of tags, merge request workflows, rebasing, stashing, addressing merge conflicts, and so on. To know more, we recommend reading the [GitLab tutorial here](https://gitlab.fdmci.hva.nl/).

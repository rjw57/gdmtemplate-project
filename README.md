# Google Cloud Deployment Manager Template for Google Cloud Projects

This repository contains a [Google Cloud Deployment
Manager](https://cloud.google.com/deployment-manager/docs/) (DM) template for
deploying a new project in Google Cloud.

The DM deployment for the University Media Platform Google Cloud project is within our
dedicated ``uis-automation-dm`` project. This project's service account has been
given elevated privileges to be able to create and manage other projects. See
the [corresponding
page](https://github.com/uisautomation/docs/blob/master/docs/dm-project-setup.md)
in our documentation repository for details.

The project is configured with the team members as admins. This may be changed
in the [project template](automationproject.py).

## Usage

The following is a minimal example of use which fills in all of the required
properties. It will create a new project with the id "my-new-project" and
associate it with the billing account "billing-account-name". It will be placed
under the folder with id number 1234567.

```yaml
resources:
  - name: project
    type: automationproject.py
    properties:
      project-id: "my-new-project"
      project-name: "My new project"
      billing-account-name: "billingAccounts/billing-account-name"
      parent-folder-id: 1234567  # numeric id of parent folder
```

There are some additional optional properties. See the [schema
definition](automationproject.py.schema) for more information.

## git subtree

It is intended that this repository be managed via ``git subtree``. To add a
copy of this directory into another repository:

```bash
$ cd my_shiny_repo  # change to root of repository
$ git remote add gdmtemplate-project https://github.com/uisautomation/gdmtemplate-project
$ git subtree add --prefix project gdmtemplate-project master
```

This will add a copy of this repository to the ``project`` directory in your
repository.

### Getting the latest changes

To pull in the latest changes:

```bash
# ... at top-level of my_shiny_repo
$ git subtree pull --prefix project gdmtemplate-project master
```

This will merge the upstream changes into your own repository.

### Pushing local changes back

You may find that you need to make some local changes which you think are worth
pushing back to the project. If so, you can use ``git subtree push``:

```bash
# ... at top-level of my_shiny_repo
$ git subtree push --prefix project gdmtemplate-project master
```

> **IMPORTANT** This will push *all changes* to the project directory in the 
> current branch back to the gdmtemplate-project repository. ONLY DO THIS IF YOU
> ARE SURE THAT IS WHAT YOU WANT TO DO.

### More information

The following links provide more information on git subtree:

* [git documentation on
    subtree](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.txt)
* [Corresponding chapter from the git
    book](https://git-scm.com/book/en/v1/Git-Tools-Subtree-Merging)
* ["Mastering Git subtrees" blog
    post](https://medium.com/@porteneuve/mastering-git-subtrees-943d29a798ec)
* [Atlassian blog
    post](https://www.atlassian.com/blog/git/alternatives-to-git-submodule-git-subtree)

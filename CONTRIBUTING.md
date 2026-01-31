# Contributing to group_15_data_wrangling

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

*This CONTRIBUTING.md was adapted from the default Python minimal setup template.*

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at https://github.com/meirikson/group_15_data_wrangling/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

group_15_data_wrangling could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/meirikson/group_15_data_wrangling/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/meirikson/group_15_data_wrangling/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## GitHub Workflow for Team Contributions

For this project, our team follows the **GitHub Flow**:

1. **Create a branch** from `dev-milestone-n` for each feature, function, or fix.  
   * Branch naming convention: `feature/<function_name>` or `fix/<issue_name>`

2. **Work on your branch locally**. Make commits regularly with meaningful messages.

3. **Push your branch** to GitHub:

   ```shell
   git push -u origin <branch_name>
   ```

4. **Create a pull request (PR)** to merge your branch into `dev-milestone-n`.
   * Make sure to link the relevant issue if there is one.

   1. The pull request should include tests.
   2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
   3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

5. **Another team member reviews the PR** and approves it.  
   * Provide constructive feedback if changes are needed.

6. Once approved, **merge the PR** into `dev-milestone-n`.  
   * Use “Merge pull request”.

7. **Delete the branch** after merging to keep the repository clean.  
   * This avoids clutter in the repository and keeps `dev-milestone-n` organized.

## Development Workflow

In this project, we applied several development tools and organizational
practices introduced in DSCI-524 to support collaborative and reproducible
work. We used GitHub Issues to track tasks, bugs, and feedback from peer reviewers
and the TA. At the beginning of every milestone/week we would organize all the tasks that had to be completed using Github Projects. This was a very handy way for our group to stay organized and track what had to be completed before the deadline. 

All development was done using our own separate branches to complete our work (a concept introduced in DSCI 522). For this project, pull requests were first merged into a weekly milestone branch and then merged into the main branch. This ensured that changes were reviewed by team members before being merged, which helped with keeping each other accountable for each respective team members work. 

We used GitHub Actions for continuous integration to automatically run tests
and build documentation on every pull request. This provided fast feedback and
helped ensure that the package remained in a working state throughout
development. Testing was done using pytest, with test dependencies
specified as optional extras in our pyproject.toml file. Documentation was created using Quarto aand quartodoc, giving us a clear documentation website directly from the source code. 

### Scaling considerations
If we had to scale up our project we'd still use much of the same tools we've learned in this course, while placing a greater emphasis on automation and code quality controls. This could include enforcing mandatory pull-request reviews and adding stricter automated checks in our CI pipelines. We would also probably expand test coverage to help catch bugs early as new features are added. Clearer contribution guidelines and more detailed documentation would make it easier for new contributors to get started and help keep development practices consistent across the team. As with scaling up our project, the nature of our project might get more complex so it would be imperative to continue using Project Views and analytics when planning. 

## Project retrospective

To support our retrospective, we reviewed GitHub Project views including a
burn-up chart grouped by milestone and assignee, as well as table views grouped
by milestone and assignee.

## Analytical Views

### Burn-up Chart (Completion rate)

When we observed our completion rate burn up chart we noticed the number of issues assigned were very even for three of our team members, Zaki, Limor and Shihan. Our fourth member, Michael had a few more issues assigned to him than the rest of the group. 

### Velocity 

Their definelty was a change in the scope of work over time. The first milestone had one of the most issues (setting up the package and getting everythign sorted) than the next two milestones, milestone 2 and 3 the amount of work decreased significantly in terms of number of issues and then the last milestone (milestone 4) had the most issues assigned to it. One thing we noticed is that our group did not over commit or have extra items left in the "Todo" section at the of milestones. Every Milsetone's respective issues were completed and marked as "done" 

### Contributions
Like mentioned before we beleive that everyone contributed equally in the project and that is reflected in the number of items assigned over the whole project. When looking at the team workload table in views, Limor, Shihan and Zaki all had 16 items assigned while Michael had 21.

## DAKI Classification

### Keep
Using GitHub Issues, milestones, and pull requests helped keep work organized
across all Milestones 1–4. Branch-based development worked well and reduced conflicts
when merging into the main branch. Also continuing to use Project Views (highest formality) was something that we looked into this milestone 4 and we can see the clear benefit of using these views so thats something we'd definelty want to keep moving forward. 

### Add
As the project progressed, automated testing and CI became more important.
Adding checks earlier will help us catch errors sooner and reduce debugging time
later in the project. 

### Improve 
We would improve pull-request review turnaround time by encouraging earlier reviews and clearer review guidelines.

### Drop 
For the most part we didn't have any bottlenecks but going forward but we would drop working on large, loosely defined issues. Breaking tasks into smaller issues would make progress easier to track and reduce review bottlenecks if they did occur. 
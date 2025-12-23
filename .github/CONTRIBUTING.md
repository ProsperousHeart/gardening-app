<a href='https://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

As this repo is meant for my students, this [CONTRIBUTING file](https://opensource.guide/starting-a-project/#writing-your-contributing-guidelines) is meant to explain how to contribute. In other words:
- how to propose fixes to items in this repo
- how to submit homework

# Found A Bug Or Have A Feature Request?
If you've noticed a bug or have a feature request, [make one](https://github.com/prosperousheart/repo-template-python/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

## Fork & Create Branch
If this is something you think you can fix (a bug) or improve upon (feature request) then:
1. (if not already done so) [fork this](https://help.github.com/articles/fork-a-repo) repo
2. create a branch with a descriptive name, e.g.:  `git checkout -b 42-short-description-here` where the #42 is the GitHub Issue you're working on

# Pull Requests

## Making A Pull Request
Your first step (if you haven't already) is to switch back to your main branch & make sure it's up to date with the latest main branch:
```
git remote add upstream git@github.com:prosperousheart/repo-template-python.git
git checkout main
git pull upstream main
```

Then make your changes on your feature or issue branch via your local copy then push!

```
git checkout 42-short-description-her
git rebase main
git push --set-upstream origin 42-short-description-her
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/articles/creating-a-pull-request).

GitHub Actions will automatically run CI checks including linting, formatting, and tests.

## Keeping Your PR Updated
I would add this section in from [here](https://github.com/activeadmin/activeadmin/blob/63146bd720031fc7deee18acab026b2b4c5054e7/CONTRIBUTING.md#keeping-your-pull-request-updated) but the following should work for our purposes:
```
git checkout main
git pull upstream main
git checkout 42-short-description-her
git merge main 42-short-description-her
git push
```

## Merging A PR (Maintainers Only)
While there is great info [here](https://github.com/activeadmin/activeadmin/blob/63146bd720031fc7deee18acab026b2b4c5054e7/CONTRIBUTING.md#merging-a-pr-maintainers-only) for general repos, this boot camp is a bit different.

A PR can only be merged into master by a maintainer if:
- it has been approved by repo owner
- it is up to date with current master
- it is clear what you are requesting

# AI-Assisted Development

This project uses [Project CodeGuard](https://project-codeguard.org/) to maintain security best practices when using AI coding assistants.

## For Contributors Using AI Assistants

If you're using Claude Code or other AI coding assistants:

1. Ensure the CodeGuard plugin is installed and up to date:
   ```bash
   /plugin update codeguard-security@project-codeguard
   ```

2. CodeGuard will automatically provide security guidance during code generation across:
   - Cryptography and key management
   - Input validation (SQL injection, XSS, command injection)
   - Authentication and authorization
   - Supply chain security
   - Cloud and platform security
   - Data protection

3. Review AI-generated code for security best practices before submitting your PR

**Source:** https://github.com/project-codeguard/rules

# Development Setup

This project uses `uv` for dependency management and `make` for common development tasks.

## Initial Setup

1. Install uv:
   ```bash
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone your fork and install dependencies:
   ```bash
   git clone git@github.com:YOUR_USERNAME/gardening-app.git
   cd gardening-app
   make install
   ```

## Development Workflow

Before committing code, ensure it passes all checks:

```bash
make format        # Format code with Black
make lint          # Check code quality with flake8
make test          # Run tests with pytest
```

Our CI pipeline runs these same commands, so running them locally ensures your PR will pass automated checks.

## Available Make Commands

- `make help` - Show all available commands
- `make install` - Install all dependencies
- `make lint` - Run linter (flake8)
- `make format` - Auto-format code (Black)
- `make format-check` - Check formatting without modifying
- `make test` - Run tests (pytest)
- `make test-coverage` - Run tests with coverage report
- `make clean` - Remove cache and temporary files

See the [Makefile Guide](../gardening-docs/docs/tutorials/general/makefile-guide.md) for detailed documentation.

## Code Quality Standards

All pull requests must:
- Pass linting (flake8)
- Be formatted with Black
- Pass all existing tests
- Include tests for new functionality
- Pass security checks (bandit, gitleaks)

The CI pipeline enforces these requirements automatically.

# Important Resources

- [Dependency Management Guide](../gardening-docs/docs/tutorials/general/dependency-management.md)
- [Makefile Guide](../gardening-docs/docs/tutorials/general/makefile-guide.md)
- [Project Documentation](https://prosperousheart.github.io/gardening-app/)

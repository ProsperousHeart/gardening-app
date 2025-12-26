# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Historical Updates

The idea for this app started in Fall 2023.

Version 1 was made in a haste to assist me in my new gardening roles, but this was not sufficient and was put on hold mid 2024. (See the 2024-Django-Attempt folder.)

Nov 2024 - Summer 2025, went through Systems Design certification to complete the requirements documentation. Most of the major milestones have been planned for as of December 2025. Now just trying to put current progress together in a way to utilize specification driven development.

## [Unreleased]

## 20251224-20251225

- converted most of original requirements documentation into markdown files and mermaid diagrams
- cleaned up mkdocs structure and fixed broken links

## 20251215 - AI Development Infrastructure

### Added

- GitHub community health files:
  - `.github/CODEOWNERS` - Code ownership assignments
  - `.github/CODE_OF_CONDUCT.md` - Community code of conduct
  - `.github/CONTRIBUTING.md` - Contributor guidelines
  - `.github/ISSUE_TEMPLATE/` - Issue templates
  - `.github/pull_request_template.md` - PR template
- VS Code workspace settings in `.vscode/`
- Documentation files:
  - `docs/history/2025-11-09-setup-conversation.md` - Environment setup conversation
  - `docs/history/2025-11-09-workflow-usage-guide.md` - Workflow usage examples
  - `specs/general-app-spec-ORIGINAL.md` - Original application specification

### Changed

- Updated README.md with Quick Start section
- Improved setup documentation links
- Added common make commands reference

## 20251110

### Added

- Items from [repo-template-python](https://github.com/ProsperousHeart/repo-template-python) to help add AI requirements for attempts to automate specs driven development needs
- Migrated to `uv` dependency management with `pyproject.toml`
- Added comprehensive AI-assisted development infrastructure:
  - 13 Claude Code slash commands in `.claude/commands/`
  - 13+ reusable prompts in `.github/prompts/`
  - 20+ instruction files for TDD, security review, quality checks
- Project CodeGuard security framework integration (23 security instruction files)
- CI/CD workflows: `ci.yml`, `codeql.yml`, `security.yml`
- Testing infrastructure with pytest examples
- Documentation templates for requirements and specifications
- Utility logger and example code in `src/`
- Development documentation: INDEX.md, INTEGRATION.md, standards guides
- `.github/META-CHECKLIST.md` for documentation synchronization

## 20251013

### Added

- [CLAUDE.md](CLAUDE.md) initial file reading the repo before restructuring of needs.

## 20250117

### Added

- [stakeholders](/index_from-mkdocs.md#stakeholders)
- [project description](/index_from-mkdocs.md#project-description)
- original [scenarios & needs](/index_from-mkdocs.md#scenarios--needs)
- [context diagrams](/scope.md#context-diagrams)
- added link to Miro board in [resources](/resources.md)
- additional [scenarios](/scope.md#scenarios-to-consider)
- use cases to [scope](/scope.md#use-cases)

### Changed

- tweaked theme settings
- added outline of requirements documentation from class work
- split up systems requirement into smaller pieces as built by the Cornell class work I completed
- merged background into index
- moved progress to nav bar
- hid DOCx files from mkdocs config file

## 20250116

### Added

- created CHANGELOG
- setup of mkdocs base

### Changed

- Moved original files / status to [2024-Django-Attempt](/2024-Django-Attempt/) for fresh start
- early stages of learning through updates to site
- configuration for nav and other site needs
- modified index to remove prior mkdocs stuff
- after building mkdocs site, added `site` folder to `.gitignore`
- add additional Mkdocs commands & clarity for publishing

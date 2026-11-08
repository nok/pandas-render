# Agent guidelines

## Commits

All commits that land on `main` must follow [Conventional Commits](https://www.conventionalcommits.org/), because release-please derives versions and the changelog from them. This also applies to PR titles when a PR is squash-merged, since the title becomes the commit message.

Format: `<type>(<optional scope>): <description>`

| Type | Use for | Effect on the release |
|---|---|---|
| `feat` | New functionality | Minor bump |
| `fix` | Bug fixes | Patch bump |
| `docs` | Documentation | Patch bump, listed in the changelog |
| `refactor`, `test`, `ci`, `chore` | Changes that users don't notice | No release on their own |

- Mark breaking changes with `!` after the type or scope (`feat!: ...`) or a `BREAKING CHANGE:` footer. They bump the major version, so on `0.x` the next release is `1.0.0`.
- Scopes used so far are `deps` and `lint`, for example `fix(deps): ...` or `chore(deps): ...`.
- `chore(main): release X.Y.Z` is reserved for release-please.

## Releases

Releases are managed by [release-please](https://github.com/googleapis/release-please) (see `.github/workflows/release-please.yml`, release type `python`):

1. When a push to `main` contains commits that trigger a release (see the table above), release-please opens or updates a release PR titled `chore(main): release X.Y.Z`.
2. Merging that PR creates the tag and GitHub release, builds the package, and publishes it to TestPyPI and PyPI.

Do not do any of the following by hand, release-please owns them:

- Edit `CHANGELOG.md`
- Change `__version__` in `pandas_render/__init__.py`
- Create release tags or GitHub releases
- Publish to PyPI

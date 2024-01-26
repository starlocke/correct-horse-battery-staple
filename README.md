# Correct-Horse-Battery-Staple

## Requirements

- Python 3.11
- pytest
- pip (to get pipenv)
- pipenv (recommended)

## Overlap Check App

Usage:

```
Two lines on the x-axis are needed as input arguments, like so:
    > python is_overlap.py "(1,4)" "(2,3)"
    > python is_overlap.py "(1.0,2.0)" "(1.0,2.0)"
    > python is_overlap.py "-2,-1" "1,2"
    > python is_overlap.py "(-1.5,0)" "(0,1.5)"
note 1: the " quote marks are commonly helpful so that command line shells pass the values correctly, they are not actually a part of the input values.
note 2: the lines are always fully exclusive ranges. the () brackets are optional.
```

## Version Comparison App

Usage:

```
Two version strings are required, like so:
    > python ver_cmp.py "1.1" "1.2"
    > python ver_cmp.py "v1.3" "v1.3"
    > python ver_cmp.py "3.14" "3.1"
    > python ver_cmp.py "v2.0" "v20.0"
    > python ver_cmp.py "v1.0" "v1.0.0"
    > python ver_cmp.py "v2.0-rc" "v2.0-alpha"
    > python ver_cmp.py "v2-alpha" "v2.0-alpha"
```

## Caching

Go to: [Zerocache](https://github.com/starlocke/zerocache)

See also: [Zerocache Development](https://github.com/starlocke/zerocache/blob/main/DEVELOPMENT.md) (shows how to run the tests)

## Testing

Limited to "overlap" and "version comparison" apps.

```
pipenv install --dev
```

```
pipenv run pytest
```

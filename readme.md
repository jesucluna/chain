# Authors
- Yefferson Marín

# Simple Guide
## Development
### 1. Prepare
```sh
  # Clone
  $ git clone https://github.com/yammadev/chain.git
  $ cd chain

  # Install virtual environment
  $ python3 -m venv venv

  # (On Windows)
  $ py -3 -m venv venv

  # Activate virtual environment
  $ . venv/bin/activate

  # (On Windows)
  $ venv\Scripts\activate

  # Install flask
  $ pip install Flask
```

### 2. Run
```sh
  # Setting
  $ export FLASK_APP=init.py

  # (On Windows)
  $ set FLASK_APP=init.py

  # Debug mode
  $ export FLASK_ENV=development

  # (On Windows)
  $ set FLASK_ENV=development

  # Run
  $ flask run

  # Go to http://127.0.0.1:5000
```

# Simple Change log
## [1.1.0]
- `MD5 hash` is generated based on a string in `index` template.
- `Form` data (string, hash, algorithm) is received via `POST` method and returned as `JSON`.
- Readability in code improved.
- Some `CSS` and `JS` libraries added.
- Front-end and scalability improved by using layouts.
- `Windows` instruction added to readme.

## [1.0.0]
- Simple and minimal application.
- Detailed readme.
- Common `.gitignore` flask file.
- Initial `Dockerfile`.

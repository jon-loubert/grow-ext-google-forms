# grow-ext-google-forms

[![Build Status](https://travis-ci.org/grow/grow-ext-google-forms.svg?branch=master)](https://travis-ci.org/grow/grow-ext-google-forms)

(WIP) An extension to integrate Google Forms with Grow. Provides a
serialization for the structure of a Google Forms form, making it easy to
integrate customized, bespoke forms while maintaining the field structure in
Google Forms.

## Concept

(WIP)

## Usage

### Grow setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-google-forms`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
extensions:
  preprocessors:
  - extensions.google_forms.GoogleFormsPreprocessor

preprocessors:
- kind: google_forms
  id: 1FAIpQLSdhq6eKn19c9dpHnCFbUAT1pWsq-erAfw2qPTXgkoQ3qc8vrg  # ID of Google Form.
  path: /content/partials/form.yaml  # Where to save serialized form.
```

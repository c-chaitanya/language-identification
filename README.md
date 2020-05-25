# language-identification
This repo contains code for Detecting language from a given text in python using Facebook's library [fasttext](https://fasttext.cc/docs/en/language-identification.html). A flask Restful API is also provided along.

# Quickstart

### Requirements

    $ pip3 install fasttext
    $ pip3 install flask

### How to run
To use as a Restfull api run the code `app.py`. To simply use code without serving it as a API use `language_identification.py`. Read more about this on my [medium](https://medium.com/@c.chaitanya/language-identification-in-python-using-fasttext-60359dc30ed0#77d0-3ba10d3953be) post.

### Examples

#### Command Line

```
curl -X POST \
  http://127.0.0.1:5000/detect_language \
  -H 'Content-Type: application/json' \
  -d '{"text":"hello"}'
```

### Future work

* As `K` value changes, number of languages returned by the model increases. Formating the return value in API needs to be done accordingly. Additionally the language iso code returned by the model could be converted to human understandable format by using additional libraries like `pycountry`

### License

`anguage-identification` is a public domain work, dedicated using
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do
whatever you want with it.


# Markdown Examples 📝

## List
1. First bullet
1. Second bullet

## Table
| Key        | Value        |
| ---------- | ------------ |
| entry1_key | entry1_value |
| entry2_key | entry2_value |
| entry3_key | entry3_value |

## Code Snippet
_bash_
```bash
./manage.py generateschema > openapi-schema.yml
```

_python_
```python
class MyClass:
    
    MY_STATIC_VARIABLE = "something_static"

    def __init__(self):
        self.x1 = 1

    ...
```

_json_
```json
{
    "key_A": "value_A",
    "key_B": [
      "value_B1",
      "value_B2",
      "value_B3"
    ]
}
```

## Comment/Quote
> "Any fool can write code that a computer can understand. Good programmers
> write code that humans can understand."  
> – Martin Fowler

## Admonitions
!!! note
    Add some note here.

!!! hint
    Some hint text with a code snippet and a link here:
    ```bash
    docker pull python
    ```
    (See also [docker hub](https://hub.docker.com/_/python).)

See [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions)
for more.

## Import other file
```.md
--8<-- "./mkdocs/draft_doc_file.md"
```

# pages-to-signatures
Tool to sort a pdf pages in an order suitable for book binding.

## Usage
The following command will convert a pdf on path INPUT_PDF to a reordered pdf at path
OUTPUT_PDF.

Optionally the number of pages per signature can be specified.
```shell script
python convert.py INPUT_PDF OUTPUT_PDF [--pages_per_signature N]
```

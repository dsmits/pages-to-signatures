#!/usr/bin/env python3
from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter
from click import command, argument, option

from signatures import order_document

DEFAULT_PAGES_PER_SIGNATURE = 4


@command()
@argument('pdf_in')
@argument('pdf_out')
@option('--pages_per_signature', default=4)
def convert(pdf_in: str, pdf_out: str, pages_per_signature=None):
    reader = PdfFileReader(pdf_in)
    writer = PdfFileWriter()

    num_pages = reader.getNumPages()
    order = order_document(num_pages, pages_per_signature)

    for n in order:
        if n is None:
            # Add a padding page
            writer.addBlankPage()
        else:
            page = reader.getPage(n)
            writer.addPage(page)

    with(Path(pdf_out).open('wb')) as f:
        writer.write(f)


def main():
    convert()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from math import cos, sin
from pathlib import Path
from typing import Iterable

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
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

    pages = order_all_pages(order, reader)
    pages = merge_pages(pages)

    for m in pages:
        writer.addPage(m)

    with(Path(pdf_out).open('wb')) as f:
        writer.write(f)


def order_all_pages(order, reader):
    for n in order:

        if n is None:
            # Add a padding page
            yield PageObject.createBlankPage()
        else:
            yield reader.getPage(n)


def merge_pages(pages: [Iterable[PageObject]]) -> Iterable[PageObject]:
    while True:
        try:
            left = next(pages)
            right = next(pages)
        except StopIteration:
            break
        width = left.artBox.upperRight[0]
        height = left.artBox.upperRight[1]
        new_page = PageObject.createBlankPage(width=0, height=0)

        new_page.mergeRotatedScaledTranslatedPage(left, 90, 0.5, 0, 0)
        new_page.mergeRotatedScaledTranslatedPage(right, 90, 0.5, 0, height / 2, expand=True)

        yield new_page


def get_transform(translate):
    return [[cos(.5), sin(.5), 0],
            [-sin(.5), cos(.5), translate],
            [0, 0, 1]]


def main():
    convert()


if __name__ == '__main__':
    main()

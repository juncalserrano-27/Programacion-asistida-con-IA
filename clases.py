# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-29 14:17:39
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-30 14:27:52


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.state = False

    def show_info(self):
        print("Titulo:", self.title)
        print("Autor:", self.author)
        print("Paginas:", self.pages)
        print("Abierto:", "Sí" if self.state else "No")

    def open(self):
        self.state = True
        print("El libro se abrio")

    def close(self):
        self.state = False
        print("El libro se cerro")


def main():
    book_1 = Book("Eleanor & Park", "Rainbow Rowell", 336)
    book_1.show_info()
    book_1.open()
    book_1.close()


if __name__ == "__main__":
    main()
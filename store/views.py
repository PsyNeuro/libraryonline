from django.shortcuts import render
from .models import category, bookdetails

import ebooklib
from ebooklib import epub
import warnings
from bs4 import BeautifulSoup
import ebooklib.epub


warnings.filterwarnings("ignore", category=UserWarning, module="ebooklib.epub")
warnings.filterwarnings('ignore', category=FutureWarning, module='ebooklib.epub')

import epub


def home(request):
    books = bookdetails.objects.all()
    return render(request,"index.html", {"books": books, "category":category})

def read(request,pk):
    book = bookdetails.objects.get(id=pk)
    booklink = book.textlink
    text = epub.read_epub(booklink)
    
    def get_text_from_item(item):
        soup = BeautifulSoup(item.get_body_content(), "html.parser")
        return str(soup)

    text_content = []

    for item in text.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text_content.append(get_text_from_item(item))

    full_text = "/n".join(text_content)
    
    return render(request,"read.html", {"full_text": full_text, "book": book})

def newpage(request):
    return render(request, "newpage.html", {})
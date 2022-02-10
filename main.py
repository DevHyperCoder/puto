from typing import Iterable, List, Optional
from  pdf2image import convert_from_path
from PIL import Image as ImageModule
from PIL.Image import Image
from itertools import zip_longest
import sys

def main():
    p = sys.argv[1] or "./test.pdf"

    print(f"Converting {p} to images")
    pages = pdf_to_image(p)

    final_pages: List[Image] = []

    # Group by 4
    for (page1,page2,page3,page4) in grouper(pages,4,fillvalue=None):
        page1: Image 
        page2: Optional[Image] 
        page3: Optional[Image] 
        page4: Optional[Image] 

        w,h = page1.size
        landscape = (h,w)

        # Create pages to print 
        final_page_1 = ImageModule.new(size=landscape,mode=page1.mode,color="#FFFFFF")
        final_page_2 = ImageModule.new(size=landscape,mode=page1.mode,color="#FFFFFF")

        # Resize images to fit in new landscape page

        page1 = resize_to_new_height(page1,landscape[1])
        final_page_1.paste(page1,(0,0))

        if page4:
            page4 = resize_to_new_height(page4,landscape[1])
            final_page_1.paste(page4,(page1.size[0],0))

        if page2:
            page2 = resize_to_new_height(page2,landscape[1])
            final_page_2.paste(page2,(0,0))

            page2: Image
            if page3:
                page3 = resize_to_new_height(page3,landscape[1])
                final_page_2.paste(page3,(page2.size[0],0))

        final_pages.append(final_page_1)
        final_pages.append(final_page_2)


    print("Writing to file")
    im1,im_list = final_pages[0], final_pages[1:]

    im1.save("/tmp/asdf.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=im_list)


def resize_to_new_height(image: Optional[Image],new_height: int) -> Image:
    if not image: 
        raise Exception("Expected image, got NoneType")
    width, height = image.size
    ratio = width / height
    new_width = int(ratio * new_height)
    return image.resize((new_width, new_height))


def grouper(iterable: Iterable[Image], n, *, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def pdf_to_image(path: str)-> List[Image]:
    """
    Convert a pdf file on disk to a sequence of Images
    """
    images = convert_from_path(path) 
    return images

if __name__ == "__main__":
    main()

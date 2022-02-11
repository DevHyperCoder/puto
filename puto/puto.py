from typing import Any, List, Optional, Tuple

from PIL import Image as ImageModule
from PIL.Image import  Image
from pdf2image.pdf2image import convert_from_path

from puto.grouper import grouper

# A chunk of 4 pages
Pages = Tuple[Image,Image,Image,Image]

def pdf_to_image(path: str)-> List[Image]:
    """
    Convert a pdf file on disk to a sequence of Images
    """
    images = convert_from_path(path) 
    return images

def process_file(path: str,output_path: str):
    """
    Process input file and save to output file
    """
    
    pages = pdf_to_image(path)

    # Quit if empty PDF
    # Don't know if this is actually possible
    if len(pages) <= 0:
        raise Exception("Can not work with a empty pdf")

    # Extract metadata of first page
    page1 = pages[0]
    mode,size = page1.mode,page1.size

    final_pages: List[Image] = []

    # Split by 4 page chunks and process them
    for p in grouper(pages,4,fillvalue=gen_blank_image(size,mode)):
        print(p[0].mode)
        final_pages.extend(process_chunk(p))

    # Convert list of images back to pdf
    im1,im_list = final_pages[0], final_pages[1:]
    im1.save(output_path, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)

def gen_blank_image(size: Tuple[int,int],mode: Any,color="#FFFFFF") -> Image:
    """
    Generate a white (default) blank page with given size and mode
    """
    return ImageModule.new(size=size,mode=mode,color = color)

def process_chunk(pages: Pages) -> List[Image]:
    """
    Process a 4 page chunk
    """
    page1 = pages[0]
    page2 = pages[1]
    page3 = pages[2]
    page4 = pages[3]

    # Flip the width and height of page1 to make it a landscape image
    w,h = page1.size
    landscape = (h,w)

    # Return the two "final" pages in a array
    return [
        generate_final_page(page4,page1,landscape),
        generate_final_page(page2,page3,landscape)
    ]

def generate_final_page(lp:Image,rp:Image,size:Tuple[int,int]) -> Image:
    """
    Generate a final page with given left page (lp) and right page (rp)

    `size` is the size of the landscape page to paste both lp and rp into
    """

    final_page = ImageModule.new(size=size,mode=lp.mode,color="#FFFFFF")  

    lp = resize_to_new_height(lp,size[1])
    rp = resize_to_new_height(rp,size[1])

    final_page.paste(lp,(0,0))
    final_page.paste(rp,(lp.size[0],0))
    return final_page


def resize_to_new_height(image: Optional[Image],new_height: int) -> Image:
    """
    Resize a image to new height while mainting the aspect ratio
    """
    if not image: 
        raise Exception("Expected image, got NoneType")
    width, height = image.size
    ratio = width / height
    new_width = int(ratio * new_height)
    return image.resize((new_width, new_height))

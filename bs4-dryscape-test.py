import sys
import dryscrape
import bs4 as bs

def getClothes():
    """Fetch a list of clothes from a saga-falabella's url

    Args:
        url: Base men url address
        
    Returns:
        This script create json filter with clothe's cathegories

    Example:
        python3 firebase_script_clothes.py <url>

    """

    sess = dryscrape.Session()
    sess.set_attribute('auto_load_images', False)
    sess.visit(sys.argv[1])
    source = sess.body()
    soup = bs.BeautifulSoup(source,'lxml')
    b = soup.select('div.fb-pod__item')
    #vertical-filters-custom

    for index, clothe in enumerate(b.findAll(name='a')):
      try:
          print(clothe['href'])
          sess.visit(clothe['href'])#dryscrape
          source = sess.body()#dryscrape
          soup = bs.BeautifulSoup(source, 'lxml')
          # x = soup.select('div.row.transcripts.video-transcripts')#principal parent tag
          # for subtitle_block in x[0].findAll(name='span'):
          #     saveFile(name_clothe, subtitle_block)
      except:
          print("error")


if __name__ == '__main__':
    getClothes()

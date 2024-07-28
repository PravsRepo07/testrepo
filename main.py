import os
import sys
import logging

from makeblog import HtmlParser



# Create and configure logger
logging.basicConfig(filename=os.getenv('LOG_FILE'), format='%(levelname)s:%(message)s %(asctime)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)



l = len(sys.argv) 
if l != 2:
    print("Please add filename in the args")
    exit
filename = sys.argv[1]



parser = HtmlParser(os.getenv('HTML_DIR')+filename)

parser.parse()
soup, body = parser.get_header()
body = parser.get_body(body)
logger.info('The body tag has been separated from the html parse tree.')
piwik = parser.get_piwik(os.getenv('HTML_DIR')+'piwik.html')
css_link = parser.create_css_link(soup)
parser.get_all_image_details()
respdiv = parser.get_respdiv(os.getenv('HTML_DIR')+'respdiv.html')
replace_body = parser.get_imagename_in_body(body)
html_soup = parser.insert_piwik_css(soup, piwik, css_link, replace_body)
parser.write_html(str(html_soup), file_name = os.getenv('OUTPUT_DIR')+'sampleblog_pic.html')
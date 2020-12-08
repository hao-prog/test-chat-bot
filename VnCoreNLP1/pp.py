import sys
import logging
from vncorenlp import VnCoreNLP

logging.basicConfig(level=logging.DEBUG)
vncorenlp_file = "./VnCoreNLP1/VnCoreNLP-1.1.1.jar"
# annotator = VnCoreNLP("./VnCoreNLP1/VnCoreNLP-1.1.1.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')
with VnCoreNLP(vncorenlp_file) as vncorenlp:
        print(str(vncorenlp.annotate(text)['sentences'][0][0]).replace("'", '"'))

# Input 
# text = str(sys.argv[1])
# text = "Le Van Hao"

# dict = {
#     "nerLabel": "Le Van Hao"
# }

# annotated_text = annotator.annotate(text)   
# print(str(annotated_text['sentences'][0][0]).replace("'", '"'))
# To perform word segmentation only
# word_segmented_text = annotator.tokenize(text)

# print(annotated_text)



# print(str(dict).replace("'", '"'))

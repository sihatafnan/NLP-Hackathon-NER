!git clone https://github.com/sagorbrur/bnlp/ --depth 1

from bnlp import POS
bn_pos = POS()
model_path = "bnlp/model/bn_pos.pkl"
text = "আমি ভাত খাই।" # or you can pass ['আমি', 'ভাত', 'খাই', '।']
res = bn_pos.tag(model_path, text)
print(res)
# [('আমি', 'PPR'), ('ভাত', 'NC'), ('খাই', 'VM'), ('।', 'PU')]
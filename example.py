# -*- coding:utf-8 -*-
import synonyms

# nearby
# print("人脸: ", synonyms.nearby("人脸"))
sen1 = "发生历史性变革"
sen2 = "发生历史性变革"
# compare
# r = synonyms.compare(sen1, sen2, seg=True)
# seg
# r = synonyms.seg(sen1)
# v
# r = synonyms.v("人脸")
# sv
# r = synonyms.sv("西虹市首富")
# keywords
r = synonyms.keywords("9月15日以来，台积电、高通、三星等华为的重要合作伙伴")
print(r)

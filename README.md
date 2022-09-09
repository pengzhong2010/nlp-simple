# nlp-simple
## A simple demo for http server. 

Using nlp base technique. Require package synonyms.


Just test for Chinese demo.Include postman api demo file.
## QuickStart

```
# pkg require
pip3 install -r requirements.txt 
# pip3 install -r requirements.txt  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com # do this if you're in China.

# data
# export SYNONYMS_WORD2VEC_BIN_URL_ZH_CN=https://gitee.com/chatopera/cskefu/attach_files/610602/download/words.vector.gz # do this if you're in China.
python3 -c "import synonyms" # download word vectors file

# start server
python3 main.py
```

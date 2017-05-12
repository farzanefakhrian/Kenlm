# Kenlm Language Model

 
## Installing Kenlm
```
pip install nltk 
git clone https://github.com/vchahun/kenlm.git
cd kenlm
./bjam 
python setup.py install 
cd ..
python –m nltk.download(puntk)
```

## Data
get Data from this address
```
https://www.dropbox.com/s/1ba5w0ofdoo149g/fawiki_normalized_tokenized.txt.zip?dl=1
```
## Testing Program
```
bzcat fawiki_normalized_tokenized.txt.bz2 | ython process.py | wc
```
## Training Model
```
bzcat bible.en.txt.bz2 |\
python process.py |\
./kenlm/bin/lmplz -o 3 > mod.arpa
```
for generate a sentence or calculate probability of a sentence run gensen.py

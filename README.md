## CorpusNet
This project makes use of a wsd model to disambiguate words in English. by extracting the senses related to each input word.


>Tasks involved

>>Convert xml to acceptable format in ism xml -- lexelt
>>add lemma and pos and senses to dev.covered.xml file
>>train using train.semcor.xml
>>test
>>output files
>>evaluate

## To execute

>> python3 src/main.py --train data/<trainfile> --test data/<testfile> --output output/dev.senses.txt



>>> Reference https://github.com/rubenIzquierdo/it_makes_sense_WSD

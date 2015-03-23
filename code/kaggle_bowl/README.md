* Resize all image to 48 X 48

Clone cxxnet using
```
git clone https://github.com/dmlc/cxxnet.git
```

Download data in /home/data/bowl using
```
wget https://www.dropbox.com/s/koixxmawzl4zl4z/train.zip?dl=1
wget https://www.dropbox.com/s/9h5sr8ikut814zs/test.zip?dl=1
wget https://www.dropbox.com/s/p5rcopgs83gyvmk/sampleSubmission.csv.zip?dl=1

sudo apt-get install zip unzip
unzip train.zip
unzip test.zip
unzip sampleSubmission.csv.zip
```

```
mkdir /home/cxxnet/example/kaggle_bowl/data
python gen_train.py /home/data/bowl/train/ /home/cxxnet/example/kaggle_bowl/data/train/
python gen_test.py /home/data/bowl/test/ /home/cxxnet/example/kaggle_bowl/data/test/
```

* Generate img list
```
python gen_img_list.py train /home/data/bowl/sampleSubmission.csv data/train/ train.lst
python gen_img_list.py test /home/data/bowl/sampleSubmission.csv data/test/ test.lst
```

* Generate binary image file
First build im2bin at ```../../tools```, then run
```
../../tools/im2bin train.lst ./ train.bin
../../tools/im2bin test.lst ./ test.bin
```

* Run CXXNET
```
mkdir models
../../bin/cxxnet bowl.conf
```
It take about 5 minute to train a deep conv net model on Geforece 780

* Run Prediction
```
../../bin/cxxnet pred.conf
```
It will write softmax result in test.txt

* Make a submission file

```
python make_submission.py /home/data/bowl/sampleSubmission.csv test.lst test.txt out.csv
```

* Submit out.csv, you will get a result

* Validation

Run
```
sh gen_tr_va.sh train.lst
```
Then you will have ```tr.lst``` and ```va.lst``` as validation set list.


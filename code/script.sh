# Download train, test, sampleSubmission
wget https://www.dropbox.com/s/koixxmawzl4zl4z/train.zip?dl=1
wget https://www.dropbox.com/s/9h5sr8ikut814zs/test.zip?dl=1
wget https://www.dropbox.com/s/p5rcopgs83gyvmk/sampleSubmission.csv.zip?dl=1

# Download augmented training data
wget https://www.dropbox.com/s/skjwc7ctlpirwnh/train_aug.zip?dl=1

# Install screen
sudo apt-get install screen

# Install zip, unzip
sudo apt-get install zip unzip

# Clone Dropbox Uploader for use
# https://www.dropbox.com/developers/apps/info/63wqwk3vj14rn2y
# Usage Method :
# ./dropbox_uploader.sh upload <LOCALFILE/DIR> <REMOTEFILE/DIR>
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
chmod +x dropbox_uploader.sh
./dropbox_uploader.sh

# Install pylearn2
# http://deeplearning.net/software/pylearn2/
git clone git://github.com/lisa-lab/pylearn2.git
sudo python setup.py develop
export PYLEARN2_DATA_PATH=/data/lisa/data

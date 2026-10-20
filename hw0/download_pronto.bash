mkdir pronto
cd pronto
echo "Pronto data from 2015" > README.txt
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
mkdir data
mv open_data_year_one.zip data/
cd data
unzip -o open_data_year_one.zip

head 2015_trip_data.csv

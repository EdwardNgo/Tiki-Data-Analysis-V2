#!bin/bash 
for folder in data01 data02 data03
do
    mkdir ./docker-es/$folder
done

mkdir ./docker-kafka/data
for folder in kafka1 kafka2 kafka3
do
    mkdir ./docker-kafka/data/$folder
done 


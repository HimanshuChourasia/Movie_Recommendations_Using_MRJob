# Movie Recommendations Using MRJob

To process a large corpus of movie ratings for providing recommendations. the program will help us decide what to watch on Netflix tonight. For each pair of movies in the data set, program will compute their statistical correlation and cosine similarity 



## Getting Started

Unzip the given dataset in your local machine or AWS EC2 Instance (prefered) copy the code as well.

### Prerequisites

Assuming having an AWS EC2 Ubuntu Machine 


Note : The code requires python 2.7 version or lower not Python 3


sudo apt update


sudo apt install python-minimal


sudo apt install python-pip


sudo apt install unzip


pip install scipy


pip install mrjob


wget http://files.grouplens.org/datasets/movielens/ml-1m.zip (Large Dataset)


wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip (or you can use the same dataset which I have provided)


unzip ml-1m.zip


unzip ml-latest-small.zip


cd ml-latest-small




```
Screenshots
```
![Screenshot](Images/Example_Step1.JPG?raw=true "Step1")

### Running the Code

1. After Installation , run the following code:
* Python csv_dat.py


This will create dat files for movies.dat & ratings.dat



## Deployment

For running MRJob for movie recommendations , create the following .mrjob.conf file on AWS EC2 linux Instance.
run “nano ~/.mrjob.conf” in command line


runners:

	    emr:
      
	        bootstrap:
          
	        - sudo yum install -y python27-numpy
          
	        - sudo yum install -y python27-scipy
          
	        core_instance_type: m3.xlarge
          
	        num_core_instances: 5
          
	        aws_access_key_id: [your access key id]
          
	        aws_secret_access_key: [your secret access key]


## Built With

* [Python](https://www.python.org/) - Implementation programming language for MapReduce/
* [MRJob](https://pythonhosted.org/mrjob/index.html) - Framework for Mapreduce in Python


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](https://git-scm.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/HimanshuChourasia/Movie_Recommendations_Using_MRJob/tags). 

## Authors

* **Himanshu Chourasia** - *Initial work* - [HimanshuChourasia](https://github.com/HimanshuChourasia)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* StackOverFlow


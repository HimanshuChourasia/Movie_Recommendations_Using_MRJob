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
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy
from scipy import spatial
from itertools import combinations


class MRMovie(MRJob):


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_names,
                   reducer=self.reducer_get_names),
            MRStep(reducer=self.reducer_create_pairs),
            MRStep(reducer=self.reducer_compute_similarities),
            MRStep(reducer=self.reducer_output),
            MRStep(reducer=self.reducer_sort_results)
        ]

    def configure_options(self):
        super(MRMovie, self).configure_options()
        self.add_passthrough_option(
            '-l', '--lowerbound', action="store", type='float',
            default=0.4, help='Lower bound of similarity.')
        self.add_passthrough_option(
            '-p', '--minpairs', action="store", type='int',
            default=8, help='Minimum number of rating pairs.')
        self.add_passthrough_option(
            '-m', '--moviename', action="append",
            default=[], help='Movie name to look up for similar movies')
        self.add_passthrough_option(
            '-k', '--numofitems', action="store", type='int',
            default=15, help='Number of similar movies to show.')

    def mapper_get_names(self, _, line):

        if len(self.options.moviename) == 0:
            raise Exception('Must specify at least one search item.')

        mid, uid, name, rating = '0','0','0','0'
        #line = str(line, errors='ignore')
        line = unicode(line, errors='ignore')
        splits = line.strip().split('::')
        if len(splits) == 4:
            uid,mid,rating = splits[0],splits[1],splits[2]
        else:
            mid,name = splits[0],splits[1]
        yield mid, (uid,name,rating)


    def reducer_get_names(self, key, values):
        last_name = None
        for value in sorted(values):
            list_values = list(value)
            name, uid, rating = list_values[1], list_values[0], list_values[2]
            if uid == '0':
                last_name = name
            else:
                yield uid, (last_name,rating)





    def reducer_create_pairs(self, _, values):
        for movie_ratings_1 ,movie_ratings_2 in combinations(values,2):
            movie_1 = movie_ratings_1[0];
            rating_1 = movie_ratings_1[1];
            movie_2 = movie_ratings_2[0];
            rating_2 = movie_ratings_2[1];
            yield (movie_1,movie_2),(rating_1,rating_2);

    def reducer_compute_similarities(self, _, values):
        movie_1, movie_2 = _[0], _[1];
        l_rating = [] ;
        for value in values:  # rating pair given by one user (3,4)
            list_values = list(value);
            value_1 = float(list_values[0]);
            value_2 = float(list_values[1]);
            l_rating.append([value_1,value_2]);

        # creating two lists rating1, rating2  vectors.
        rating_1,rating_2 = map(list,zip(*l_rating));
        # calculate the similarity score for all previous similar movies
        # since we are checking if there is a new pair of movies we calculate the similarity measure of old pair of movies
        # Statistical correlation
        cor = numpy.corrcoef(rating_1, rating_2)[0, 1];
        # Cosine Correlation
        cos_cor = 1 - spatial.distance.cosine(rating_1, rating_2);
        # Combine two metrics
        avg_cor = 0.5 * (cos_cor + cor);
        # calculate the number of pairs in which ratings were common
        counter = len(rating_1);
        yield (movie_1, movie_2), (movie_1, movie_2, avg_cor, cor, cos_cor, counter);


    def reducer_output(self, _, values):
        for value in values:
            list_values = list(value)
            m1,m2,avg_cor,stat_cor,cos_cor,counter = list_values
        for movie in self.options.moviename:
            if m1 == movie:
                yield m1,(avg_cor,m1,m2,stat_cor,cos_cor,counter)
            elif m2 == movie:
                yield m2,(avg_cor,m2,m1,stat_cor,cos_cor,counter)

    def reducer_sort_results(self, _, values):
        index = 0
        for value in sorted(values):
            list_values = list(value)
            avg_cor,m1,m2,stat_cor,cos_cor,counter = list_values
        if index < self.options.numofitems:
            yield m1,(m2,avg_cor,stat_cor,cos_cor,counter)
        index += 1

if __name__ == '__main__':
    MRMovie.run()

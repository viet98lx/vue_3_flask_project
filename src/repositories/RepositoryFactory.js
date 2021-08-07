import ActorRepository from './ActorRepository';
import FilmRepository from './FilmRepository';

const repositories = {
    'actors': ActorRepository,
    'films': FilmRepository
}
export default {
    get: name => repositories[name]
};
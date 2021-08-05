import ActorRepository from './ActorRepository';
import FilmRepository from './FilmRepository';

const repositories = {
    'actors': ActorRepository,
    'users': FilmRepository
}
export default {
    get: name => repositories[name]
};
import Client from './clients/AxiosClient';
const resource = '/film';

export default {
    get() {
        return Client.get(`${resource}/get`);
    },
    getFilm(id) {
        return Client.get(`${resource}/get/${id}/`);
    },
    create(payload) {
        return Client.post(`${resource}/add`, payload);
    },
    update(payload, id) {
        return Client.put(`${resource}/update/${id}/`, payload);
    },
    delete(id) {
        return Client.delete(`${resource}/delete/${id}/`)
    },

    // MANY OTHER ENDPOINT RELATED STUFFS
};
import axios from 'axios';
const API_URL = 'http://localhost:8000/api';

export default class Service{

    constructor(){}

    async getSongs() {
        const url = `${API_URL}/songs/`;
        return axios.get(url).then(response => response.data);
    }

    async searchSongs(query) {
        const url = `${API_URL}/songs/`;
        return axios.post(url, query).then(response => response.data);
    }
    
    async login(credentials) {
        const url = `${API_URL}/auth/login/`;
        return axios.post(url, credentials).then(response => response.data);
    }
    
    async logout() {
        const url = `${API_URL}/auth/logout/`;
        return axios.post(url).then(response => response.data);
    }

    async register(credentials) {
        const url = `${API_URL}/register/`;
        return axios.post(url, credentials).then(response => response.data);
    }

    setToken(token) {
        axios.defaults.headers.common['Authorization'] = `JWT ${token}`
    }

    removeToken() {
        delete axios.defaults.headers.common['Authorization']
    }

    async getUserData() {
        const url = `${API_URL}/users/`;
        return axios.get(url).then(response => response.data);
    }

    async getFavoriteSongs() {
        const url = `${API_URL}/favorite_songs/`;
        return axios.get(url).then(response => response.data);
    }

    async addFavoriteSong(query) {
        const url = `${API_URL}/favorite_songs/`;
        return axios.post(url, query).then(response => response.data);
    }

    async removeFavoriteSong(query) {
        const url = `${API_URL}/favorite_songs_delete/`;
        return axios.post(url, query).then(response => response.data);
    }

    async createUser(user) {
        const url = `${API_URL}/users/`;
        return axios.post(url, user)
    }
}
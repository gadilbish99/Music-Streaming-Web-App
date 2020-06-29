import Vue from 'vue'
import Vuex from 'vuex'
import Cookies from "js-cookie";
import Service from '@/service';

Vue.use(Vuex)
const service = new Service();

if (Cookies.get('token')) {
  service.setToken(Cookies.get('token'))
}

export default new Vuex.Store({
  state: {
    status: '',
    token: Cookies.get('token') || '',
    searchResults: [],
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token){
      state.status = 'success'
      state.token = token
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''
      state.searchResults = []
    },
    search(state){
      state.status = 'searching'
    },
    found(state, searchResults){
      state.status = '',
      state.searchResults = searchResults
    },
    no_input(state){
      state.status = '',
      state.searchResults = []
    },

    sent(state){
      state.status = 'sent'
    },
    added(state){
      state.status = ''
    },
    removed(state){
      state.status = ''
    },
  },
  actions: {
    // Login/out
    login({commit}, credentials){
      return new Promise((resolve, reject) => {
          commit('auth_request')
          service.login(credentials)
          .then(resp => {
              const token = resp.token
              Cookies.set('token', token)
              service.setToken(token)
              commit('auth_success', token)
              resolve(resp)
          })
          .catch(err => {
              commit('auth_error')
              Cookies.remove('token')
              reject(err) 
          })
      })
    },
    register({commit}, credentials){
      return new Promise((resolve, reject) => {
          commit('auth_request')
          service.login(credentials)
          .then(resp => {
              const token = resp.token
              Cookies.set('token', token)
              service.setToken(token)
              commit('auth_success', token)
              resolve(resp)
          })
          .catch(err => {
              commit('auth_error')
              Cookies.remove('token')
              reject(err) 
          })
      })
    },
    logout({commit}){
      return new Promise((resolve, reject) => {
          commit('logout')
          service.logout()
          .then(resp => {
              Cookies.remove('token')
              service.removeToken()
              resolve(resp)
          })
          .catch(err => {
              commit('auth_error')
              Cookies.remove('token')
              reject(err) 
          })
          
      })
    },
    // Song actions
    async search({commit}, query){
      commit('search')
      return await service.searchSongs(query)
      .then(result => {
          commit('found', result)
      })
    },
    resetSearchResults({commit}){
      commit('no_input')
    },
    async getSongs(){
      return await service.getSongs()
    },
    async getFavoriteSongs(){
      return await service.getFavoriteSongs()
    },
    async addFavoriteSong({commit}, query){
      commit('sent')
      return await service.addFavoriteSong(query)
      .then(result => {
          commit('added')
          return result
      })
    },

    async removeFavoriteSong({commit}, query){
      commit('sent')
      return await service.removeFavoriteSong(query)
      .then(result => {
          commit('removed')
          return result
      })
    },
  },

  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    feeds: state => state.searchResults,
  }
})

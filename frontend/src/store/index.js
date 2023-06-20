import { createStore } from 'vuex'
import axios from "axios";

const store = createStore({
    state: {
        movies: [],
        movie: null,
        actors: [],
    },

    mutations: {
        setMovies (state, payload) {
            state.movies = payload;
        },

        setMovie (state, payload) {
            state.movie = payload;
        },

        setActors (state, payload) {
            state.actors = payload;
        }
    },

    actions: {
        getMovies({ commit }, endpoint='movies/') {
          axios.get(endpoint).then(
              (response) => {
                  commit('setMovies', response.data);
              }
          );
        },
        getMovie({ commit }, movieId) {
            axios.get(`movies/${movieId}/`).then(
                (response) => {
                    commit('setMovie', response.data)
                }
            )
        },
        editMovie({ commit }, { movieId, data}) {
          axios.patch(
              `movies/${movieId}/`,
              data
          ).then(
              (response) => {
                  commit('setMovie', response.data)
              }
          )
        },
        rateMovie({ commit, dispatch }, {movieId, grade}) {
            axios.post(
                `movies/${movieId}/review/`,
                { grade }
                )
                .then((response) => {
                    dispatch('getMovie', movieId)
                })
        },
        getActors({ commit }) {
          axios.get('actors/')
              .then(
                  (response) => commit('setActors', response.data)
              )
        },
    }
})

export default store;

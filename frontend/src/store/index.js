import { createStore } from 'vuex'
import axios from "axios";

const store = createStore({
    state: {
        movies: null,
        movie: null
    },

    mutations: {
        setMovies (state, payload) {
            state.movies = payload;
        },

        setMovie (state, payload) {
            state.movie = payload;
        }
    },

    actions: {
        getMovies({ commit }, endpoint="http://localhost:8000/rest-api/movies/") {
          axios.get(endpoint).then(
              (response) => {
                  commit('setMovies', response.data);
              }
          );
        },
        getMovie({ commit }, movieId) {
            axios.get(`"http://localhost:8000/rest-api/movies/${movieId}/"`).then(
                (response) => {
                    commit('setMovie', response.data)
                }
            )
        }
    }
})

export default store;

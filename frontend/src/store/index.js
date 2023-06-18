import { createStore } from 'vuex'

const store = createStore({
    state () {
        return {
            movies: null,
            movie: null
        }
    },
})

export default store;

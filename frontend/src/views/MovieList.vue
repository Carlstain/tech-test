<script setup>
import {computed, onMounted, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";

const store = useStore();
const router = useRouter();

const getNextPage = () => {
  store.dispatch('getMovies', store.state.movies.next);
};

const getPreviousPage = () => {
  store.dispatch('getMovies', store.state.movies.previous);
};

const goToMovie = (movieId) => {
  router.push({ name: 'movie', params: { movieId } })
};
onMounted( () => {
  store.dispatch('getMovies')
})
</script>

<template>
  <h1> MovieList </h1>
  <div v-if="store.state.movies">
    <div v-for="movie in store.state.movies.results">
      <p @click="goToMovie(movie.id)">{{ movie.title }}</p>
    </div>
    <button
        @click="getNextPage"
        :disabled="!store.state.movies.next"
    >
      Next
    </button>
    <button
        @click="getPreviousPage"
        :disabled="!store.state.movies.previous"
    >
      Previous
    </button>
    <router-view />
  </div>
</template>

<style scoped>
</style>

<script setup>
import {computed, onMounted, ref} from "vue";
import {useStore} from "vuex";

const store = useStore();

const getNextPage = () => {
  store.dispatch('getMovies', store.state.movies.next)
};

const getPreviousPage = () => {
  store.dispatch('getMovies', store.state.movies.previous)
};
onMounted( () => {
  store.dispatch('getMovies')
})
</script>

<template>
  <h1> MovieList </h1>
  <div v-if="store.state.movies">
    <div v-for="movie in store.state.movies.results">
      <span>{{ movie.title }}</span>
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
  </div>
</template>

<style scoped>
</style>

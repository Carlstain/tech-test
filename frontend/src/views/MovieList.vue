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
  <v-row>
    <v-col class="text-center">
      <h1> Movies </h1>
    </v-col>
  </v-row>
  <v-row v-if="store.state.movies">
    <v-col>
      <v-list lines="one">
        <v-list-item
            v-for="movie in store.state.movies.results"
            :key="movie.id"
            :title="movie.title"
            @click="goToMovie(movie.id)"
        />
      </v-list>
      <v-row>
        <v-col>
          <v-btn
              @click="getPreviousPage"
              :disabled="!store.state.movies.previous"
              class="mr-5"
          >
            Previous
          </v-btn>
          <v-btn
              @click="getNextPage"
              :disabled="!store.state.movies.next"
          >
            Next
          </v-btn>
        </v-col>
      </v-row>
    </v-col>
    <v-col>
      <router-view />
    </v-col>
  </v-row>
</template>

<style scoped>
</style>

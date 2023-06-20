<script setup>
import {onMounted} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";

const store = useStore();
const router = useRouter();

const getPage = (nextOrPreviousUrl) => {
  store.dispatch('getMovies', nextOrPreviousUrl);
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
  <v-row>
    <v-col>
      <v-list>
        <v-list-item
            v-for="{id, title} in store.state.movies.results"
            :key="id"
            :title="title"
            @click="goToMovie(id)"
        />
      </v-list>
      <v-row>
        <v-col>
          <v-btn
              @click="getPage(store.state.movies.previous)"
              :disabled="!store.state.movies.previous"
              class="mr-5"
          >
            Previous
          </v-btn>
          <v-btn
              @click="getPage(store.state.movies.next)"
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

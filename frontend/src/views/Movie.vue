<script setup>
import {onBeforeRouteUpdate, useRoute} from "vue-router";
import {onMounted, watch} from "vue";
import {useStore} from "vuex";
import MovieCard from "../components/MovieCard.vue";

const store = useStore();
const route = useRoute();

onMounted(() => {
  store.dispatch('getMovie', route.params.movieId)
})

watch(() => route.params.movieId,
    (newMovieId) => {
      store.dispatch('getMovie', newMovieId)
    }
)

</script>

<template>
  <div v-if="store.state.movie">
    <movie-card v-bind="store.state.movie" />
  </div>
</template>

<style scoped>

</style>

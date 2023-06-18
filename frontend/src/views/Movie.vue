<script setup>
import {useRoute} from "vue-router";
import {computed, onMounted, ref, watch} from "vue";
import {useStore} from "vuex";
import ShowMovie from "../components/ShowMovie.vue";

const store = useStore();
const route = useRoute();

const grade = ref(null)

const rating = ref({
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5',
})

const review = () => {
  store.dispatch('rateMovie', {
    movieId: route.params.movieId,
    grade: grade.value,
  })
}

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
  <v-card v-if="store.state.movie">
    <v-toolbar>
      <v-toolbar-title class="text-h6">
        {{ store.state.movie.title }}
      </v-toolbar-title>
      <template v-slot:append>
        <v-btn variant="outlined">Edit</v-btn>
      </template>
    </v-toolbar>
    <ShowMovie
        :grade_avg="store.state.movie.grade_avg"
        :actors="store.state.movie.actors"
        :description="store.state.movie.description"
    />
    <v-container>
      <v-row>
        <v-slider
            :ticks="rating"
            :min="1"
            :max="5"
            step="1"
            show-ticks="always"
            tick-size="4"
            v-model="grade"
        />
      </v-row>
      <v-row justify="center">
        <v-btn variant="outlined" @click="review">
          Rate
        </v-btn>
      </v-row>
    </v-container>
  </v-card>
</template>

<style scoped>

</style>

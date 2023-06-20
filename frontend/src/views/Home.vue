<script setup>
import {useRouter} from "vue-router";

const router = useRouter();

const goToMovies = () => router.push({ name: 'movies' });
</script>

<template>
  <h1>Movie Manager</h1>
  <v-btn @click="goToMovies">See movies</v-btn>
</template>

<style scoped>

</style>

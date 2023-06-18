<script setup>
import {useRouter} from "vue-router";

const router = useRouter();

const goToMovies = () => router.push({ name: 'movies' });
</script>

<template>
  <h1>Movie Manager</h1>
  <button @click="goToMovies">See movies</button>
</template>

<style scoped>

</style>

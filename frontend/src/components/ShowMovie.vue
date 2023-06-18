<script setup>
  defineProps({
    actors: {
      type: Array,
      default: () => [],
    },
    grade_avg: Number,
    description: String
  })
</script>

<template>
  <v-card-item>
    <v-card-subtitle>Rating: {{ grade_avg }} / 5</v-card-subtitle>
  </v-card-item>
  <v-card-text>
    <p class="description">{{ description }}</p>
    <p>
      <span class="font-weight-bold">With: </span> {{ actors.toString() }}
    </p>
  </v-card-text>
  <v-card-actions>
  </v-card-actions>
</template>

<style scoped>
  .description {
    margin-bottom: 0.5rem;
    height: 100px;
  }
</style>

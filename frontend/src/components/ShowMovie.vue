<script setup>
  defineProps({
    actors: {
      type: Array,
      default: () => [],
    },
    description: String
  })
</script>

<template>
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

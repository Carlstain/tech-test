<script setup>
  defineProps({
    title: {
      type: String,
      required: true,
    },
    actors: {
      type: Array,
      default: () => [],
    },
    reviews: {
      type: Array,
      default: () => [],
    },
    grade_avg: Number,
    description: String
  })
</script>

<template>
  <v-card>
    <v-toolbar>
      <v-toolbar-title class="text-h6">
        {{ title }}
      </v-toolbar-title>
      <template v-slot:append>
        <v-btn variant="outlined">Edit</v-btn>
      </template>
    </v-toolbar>
    <v-card-item>
      <v-card-subtitle>Rating: {{ grade_avg }} / 5</v-card-subtitle>
    </v-card-item>
    <v-card-text>
      <p class="description">{{ description }}</p>
      <p>
        <span class="font-weight-bold">With: </span> {{ actors.toString() }}
      </p>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn variant="outlined">
        Review
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
  .description {
    margin-bottom: 0.5rem;
    height: 100px;
  }
</style>

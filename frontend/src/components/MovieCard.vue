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
  <div>
    <h2> {{title}} </h2>
    <p> {{actors}} </p>
    <p> {{description}} </p>
    <p> {{reviews}} </p>
    <p> {{grade_avg}} </p>
  </div>
</template>

<style scoped>

</style>

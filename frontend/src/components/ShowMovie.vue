<script setup>
  import {computed} from "vue";
  import {useStore} from "vuex";

  const props = defineProps({
    actors: {
      type: Array,
      default: () => [],
    },
    description: String
  })

  const store = useStore();

  const actor_names = computed(
      () => store.state.actors.filter(({ id }) => props.actors.includes(id))
          .map(({first_name, last_name}) => `${first_name} ${last_name}`)
  );
</script>

<template>
  <v-card-text>
    <p class="description">{{ description }}</p>
    <p>
      <span class="font-weight-bold">With: </span> {{ actor_names.toString() }}
    </p>
  </v-card-text>
</template>

<style scoped>
  .description {
    margin-bottom: 0.5rem;
    height: 100px;
  }
</style>
